"""
Clean, modern examples using the qoery SDK

This demonstrates the developer-friendly API
"""

import qoery


def main():
    # Initialize client - automatically loads API key from .env or environment variables
    client = qoery.Client()
    
    print("=" * 60)
    print("Qoery SDK - Clean & Simple Examples")
    print("=" * 60)
    
    # Example 1: Get OHLCV Candles (as DataFrame)
    print("\n[CANDLES] Getting ETH-USDC 15-minute candles...")
    candles = client.candles.get(
        symbol="ETH-USDC",
        interval="15m",
        limit=5
    )
    
    # Built-in Pandas support!
    df = candles.df
    if not df.empty:
        print(df[["time", "close", "volume"]].to_string(index=False))
    else:
        print("  (No data returned)")
    print(f"  Credits used: {candles.credits_used}")
    
    # Example 2: Get Raw Ticks
    print("\n[TICKS] Getting WBTC-USDT tick data...")
    ticks = client.ticks.get(
        symbol="WBTC-USDT",
        limit=5
    )
    
    for tick in ticks:
        side_indicator = "BUY " if tick.side == "buy" else "SELL"
        print(f"  {side_indicator} {tick.timestamp} | ${tick.price:.2f} | {tick.side.upper()}")
    print(f"  Credits used: {ticks.credits_used}")
    
    # Example 3: Find Pools
    print("\n[POOLS] Finding ETH-USDC pools...")
    pools = client.pools.find(symbol="ETH-USDC")
    
    for i, pool in enumerate(pools.data[:3], 1):
        print(f"  {i}. {pool.network.upper()}")
        print(f"     Address: {pool.id}")
        print(f"     Protocol: {pool.protocol_version}")
        print(f"     TVL: ${float(pool.tvl_usd):,.2f}")
        print()
    print(f"  Credits used: {pools.credits_used}")
    
    # Example 4: Check Usage
    print("\n[USAGE] Checking API usage...")
    usage = client.account.usage()
    
    print(f"  Plan: {usage.subscription_plan.upper()}")
    print(f"  Credits (month): {usage.credits_month.used:,}/{usage.credits_month.limit:,}")
    print(f"  Remaining: {usage.credits_month.remaining:,}")
    print(f"  API calls (month): {usage.api_calls_month_used:,}")
    
    # Example 5: Health Check
    print("\n[HEALTH] API Health Check...")
    try:
        health = client.health_check()
        print(f"  Status: {health['status']}")
        print(f"  Timestamp: {health['timestamp']}")
    except qoery.UnauthorizedException:
        print("  (Health check requires valid API key permissions)")
    
    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)


def example_with_context_manager():
    """
    You can also use the client as a context manager
    for automatic cleanup
    """
    with qoery.Client() as client:
        candles = client.candles.get(
            symbol="ETH-USDC",
            interval="1h",
            limit=10
        )
        print(f"Got {len(candles.data)} candles")


def example_using_pool_address():
    """
    Using pool address is faster and uses fewer credits
    than using symbol
    """
    client = qoery.Client()
    
    # First find the pool
    pools = client.pools.find(symbol="ETH-USDC")
    best_pool = pools.data[0]  # Sorted by liquidity
    
    print(f"Using pool: {best_pool.id}")
    
    # Now use the pool address directly
    candles = client.candles.get(
        pool=best_pool.id,
        interval="15m",
        limit=10
    )
    
    print(f"Got {len(candles.data)} candles using {candles.credits_used} credits")


def example_error_handling():
    """
    Proper error handling with custom exceptions
    """
    try:
        client = qoery.Client()  # Will raise if no API key
        
        # This will raise InvalidRequestError
        candles = client.candles.get(interval="15m", limit=10)
        
    except qoery.AuthenticationError as e:
        print(f"Auth error: {e}")
    except qoery.InvalidRequestError as e:
        print(f"Invalid request: {e}")
    except qoery.RateLimitError as e:
        print(f"Rate limited: {e}")
    except qoery.APIError as e:
        print(f"API error (status {e.status_code}): {e}")


if __name__ == "__main__":
    main()
