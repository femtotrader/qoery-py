# API Comparison: Auto-Generated vs. Clean Wrapper

This document shows the difference between using the auto-generated OpenAPI client and our clean wrapper.

## Auto-Generated API (verbose and clunky)

```python
import os
import qoery
from qoery.rest import ApiException
from pprint import pprint

# Verbose configuration
configuration = qoery.Configuration(
    host = "https://api.qoery.com/v0"
)
configuration.api_key['ApiKeyAuthHeader'] = os.environ["API_KEY"]

# Need to manage context manually
with qoery.ApiClient(configuration) as api_client:
    # Create instance for each API
    api_instance = qoery.MarketDataApi(api_client)
    
    try:
        # Verbose method names, unclear parameters
        api_response = api_instance.candles_get(
            interval='15m',
            symbol='ETH-USDC',
            limit=10
        )
        
        # Response is not iterable, must access .data
        for candle in api_response.data:
            # Access through object properties
            print(f"{candle.time}: ${candle.close}")
            
    except ApiException as e:
        # Generic exception handling
        print(f"Exception: {e}")
```

## Clean Wrapper (simple and intuitive)

```python
import qoery

# Simple initialization - API key from env automatically
client = qoery.Client()

# Intuitive, resource-based API
candles = client.candles.get(
    symbol="ETH-USDC",
    interval="15m",
    limit=10
)

#Response is directly iterable
for candle in candles:
    print(f"{candle.time}: ${candle.close}")

# Clean access to metadata
print(f"Credits used: {candles.credits_used}")
```

## Key Improvements

### 1. **Simpler Initialization**

**Before:**
```python
configuration = qoery.Configuration(host="https://api.qoery.com/v0")
configuration.api_key['ApiKeyAuthHeader'] = os.environ["API_KEY"]
api_client = qoery.ApiClient(configuration)
api = qoery.MarketDataApi(api_client)
```

**After:**
```python
client = qoery.Client()  # That's it!
```

### 2. **Resource-Based Organization**

**Before:**
```python
market_data_api = qoery.MarketDataApi(api_client)
discovery_api = qoery.DiscoveryApi(api_client)
account_api = qoery.AccountApi(api_client)
```

**After:**
```python
client.candles.get(...)
client.ticks.get(...)
client.pools.find(...)
client.account.usage()
```

### 3. **Better Error Handling**

**Before:**
```python
from qoery.rest import ApiException

try:
    response = api.candles_get(...)
except ApiException as e:
    # Generic error, unclear what went wrong
    print(f"Error: {e}")
```

**After:**
```python
try:
    candles = client.candles.get(...)
except qoery.AuthenticationError:
    print("Invalid API key")
except qoery.InvalidRequestError as e:
    print(f"Bad request: {e}")
except qoery.RateLimitError:
    print("Rate limited")
```

### 4. **Pythonic Naming**

**Before:**
```python
# Method names with underscores
api.candles_get()
api.pools_get()
api.usage_get()

# Parameter names don't match Python conventions
var_from  # Reserved word workaround
```

**After:**
```python
# Clean, readable method names
client.candles.get()
client.pools.find()
client.account.usage()

# Pythonic parameter names
from_time
to_time
```

### 5. **Clean Data Models**

**Before:**
```python
# Generic Pydantic models with unclear structure
response = api.candles_get(...)
# response is CandlesResponse object
# Must access response.data to get list
# Individual items are Candle Pydantic models
```

**After:**
```python
# Clean dataclasses with clear attributes
candles = client.candles.get(...)
# candles is Response object with .data and .credits_used
# Directly iterable: for candle in candles
# Each candle is a clean dataclass
```

### 6. **Built-in Data Analysis**

**Now:**
```python
# Direct Pandas support
df = client.candles.get(symbol="ETH-USDC", interval="15m").df
print(df.head())
#    time                  open    high    low     close   volume
# 0  2024-01-01 00:00:00  2281.5  2282.1  2280.9  2281.2  124.5
```

### 7. **Context Manager Support**

**Before:**
```python
# Must use context manager or manually close
with qoery.ApiClient(configuration) as api_client:
    api = qoery.MarketDataApi(api_client)
    # Use api...
```

**After:**
```python
# Optional context manager
with qoery_sdk.Client() as client:
    candles = client.candles.get(...)
# Automatic cleanup

# Or use without context manager
client = qoery_sdk.Client()
candles = client.candles.get(...)
client.close()  # Optional cleanup
```

### 7. **Default Values**

**Before:**
```python
# Must specify all required parameters
api.candles_get(
    interval='15m',  # Required
    symbol='ETH-USDC'  # One of symbol/pool required
)
```

**After:**
```python
# Sensible defaults
client.candles.get(
    symbol="ETH-USDC"
    # interval defaults to "15m"
    # limit defaults to 10
)
```

### 8. **Better Documentation**

**Before:**
```python
# Auto-generated docstrings
def candles_get(self, interval, symbol=None, pool=None, var_from=None, to=None, networks=None, limit=None):
    """Get OHLCV Candles"""
    # Unclear what parameters do
```

**After:**
```python
def get(
    self,
    *,
    symbol: Optional[str] = None,
    pool: Optional[str] = None,
    interval: str = "15m",
    limit: int = 10,
    from_time: Optional[datetime] = None,
    to_time: Optional[datetime] = None,
    networks: Optional[str] = None,
) -> Response:
    """
    Get OHLCV candles for a trading pair
    
    Args:
        symbol: Trading pair symbol (e.g., "ETH-USDC")
        pool: Pool contract address (faster, cheaper)
        interval: Candle interval (e.g., "1m", "5m", "15m", "1h")
        ...
    
    Returns:
        Response containing list of Candle objects
        
    Example:
        >>> candles = client.candles.get(symbol="ETH-USDC", interval="15m")
    """
```

## Summary

| Feature | Auto-Generated | Clean Wrapper |
|---------|---------------|---------------|
| Lines of code | ~15 | ~3 |
| Readability | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Type safety | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Error handling | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Documentation | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| IDE support | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Pythonic | ⭐⭐ | ⭐⭐⭐⭐⭐ |

The clean wrapper provides a **much better developer experience** while maintaining the same functionality.
