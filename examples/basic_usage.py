"""
Basic usage examples for the qoery-py SDK.
Shows how to initialize the client and fetch data as DataFrames.
"""

import os
import qoery

def main():
    # 1. Initialize the client
    # By default, reads QOERY_API_KEY from environment variables
    # You can also pass it explicitly: client = qoery.Client(api_key="...")
    client = qoery.Client()
    print("Client initialized successfully.")

    print("\n" + "="*50)
    print("1. Fetch Candles as DataFrame")
    print("="*50)
    
    # Fetch 15-minute candles for ETH-USDC
    candles = client.candles.get(
        symbol="WETH-USDC", 
        interval="15m", 
        limit=5
    )
    
    # Access metadata
    print(f"Credits used: {candles.credits_used}")
    
    # Convert directly to Pandas DataFrame
    df = candles.df
    print("\nDataFrame Head:")
    print(df.head())

    print("\n" + "="*50)
    print("2. Fetch Ticks as DataFrame")
    print("="*50)

    # Fetch raw tick data
    ticks = client.ticks.get(
        symbol="WBTC-USDT", 
        limit=5
    )
    
    # Convert to DataFrame
    ticks_df = ticks.df
    print(f"Got {len(ticks_df)} ticks")
    print("\nTicks DataFrame:")
    print(ticks_df[['timestamp', 'price', 'side', 'amount_usd']])

    print("\n" + "="*50)
    print("3. Check Usage")
    print("="*50)
    
    usage = client.account.usage()
    print(f"Plan: {usage.subscription_plan}")
    print(f"Credits used (month): {usage.credits_month.used:,} / {usage.credits_month.limit:,}")

if __name__ == "__main__":
    try:
        main()
    except qoery.AuthenticationError:
        print("\nError: Authentication failed. Please check your QOERY_API_KEY.")
    except Exception as e:
        print(f"\nError: {e}")
