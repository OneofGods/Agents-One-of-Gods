"""
Drift Protocol Demo - ETH Trading on Solana DEX
NO CENTRALIZED EXCHANGES! Pure DeFi Power!

Shows how Loly can trade ETH on Drift Protocol
"""

from crypto_agent.api import loly_api
import json


def print_section(title):
    """Print a fancy section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def demo_drift_trading():
    """Demonstrate Loly trading ETH on Drift Protocol"""

    print("\n💎 DRIFT PROTOCOL - ETH TRADING ON SOLANA 💎")
    print("NO CENTRALIZED EXCHANGES - Pure DeFi!\n")

    # 1. Greeting
    print_section("1. Loly says hello to Drift Agent")
    greeting = loly_api.hello()
    print(f"Drift Agent: {greeting}")

    # 2. Check available markets
    print_section("2. Loly asks: What markets are available?")
    markets = loly_api.get_markets()
    for market, info in markets.items():
        print(f"\n  {market}:")
        print(f"    Name: {info['name']}")
        print(f"    Type: {info['type']}")
        print(f"    Base: {info['base']}")
        print(f"    Quote: {info['quote']}")
        print(f"    Max Leverage: {info['leverage_max']}x")

    # 3. Get market info with price
    print_section("3. Loly asks: What's the ETH-PERP market looking like?")
    eth_perp = loly_api.get_market_info('ETH-PERP')
    print(f"\n  Market: {eth_perp['name']}")
    print(f"  Current Price: ${eth_perp['current_price']:,.2f}")
    print(f"  24h Volume: ${eth_perp['24h_volume']:,.0f}")
    print(f"  24h Change: {eth_perp['24h_change']:+.2f}%")

    # 4. Check ETH price
    print_section("4. Loly asks: What's the current ETH price?")
    eth_price = loly_api.get_price('ETH')
    print(f"  ETH Price: ${eth_price:,.2f}")

    # 5. Create Drift account
    print_section("5. Loly creates a Drift account")
    account_result = loly_api.create_account("Loly", initial_usdc=10000)
    print(json.dumps(account_result, indent=2))

    # 6. Check balance
    print_section("6. Loly checks her balance")
    balance = loly_api.get_balance("Loly")
    print(f"\n  User: {balance['user_id']}")
    print(f"  USDC: ${balance['USDC']:,.2f}")
    print(f"  ETH: {balance['ETH']} ETH")
    print(f"  SOL: {balance['SOL']} SOL")

    # 7. Buy ETH (Spot)
    print_section("7. Loly buys 2 ETH on spot market")
    buy_result = loly_api.buy_eth("Loly", 2.0, leverage=1, market="ETH-SPOT")
    print(json.dumps(buy_result, indent=2))

    # 8. Check balance after purchase
    print_section("8. Loly checks balance after buying")
    balance = loly_api.get_balance("Loly")
    print(f"\n  USDC: ${balance['USDC']:,.2f}")
    print(f"  ETH: {balance['ETH']} ETH")

    # 9. Open leveraged long position (Perps)
    print_section("9. Loly opens 5x leveraged long on ETH-PERP")
    long_result = loly_api.buy_eth("Loly", 1.5, leverage=5, market="ETH-PERP")
    print(json.dumps(long_result, indent=2))

    # 10. Check open positions
    print_section("10. Loly checks her open positions")
    positions = loly_api.get_all_positions("Loly")
    print(f"\n  Total Open Positions: {len(positions)}")
    for pos in positions:
        print(f"\n  Position: {pos['market']}")
        print(f"    Size: {pos['size']} ETH")
        print(f"    Entry Price: ${pos['entry_price']:,.2f}")
        print(f"    Current Price: ${pos['current_price']:,.2f}")
        print(f"    Leverage: {pos['leverage']}x")
        print(f"    Unrealized PnL: ${pos['unrealized_pnl']:,.2f} ({pos['unrealized_pnl_pct']:+.2f}%)")

    # 11. Get trade history
    print_section("11. Loly checks her trade history")
    history = loly_api.get_trade_history("Loly")
    print(f"\n  Total Trades: {len(history)}")
    for trade in history:
        print(f"\n  {trade['side'].upper()} {trade['size']} {trade['market']}")
        print(f"    Price: ${trade['price']:,.2f}")
        print(f"    Value: ${trade['value']:,.2f}")
        print(f"    Leverage: {trade['leverage']}x")
        print(f"    Fee: ${trade['fee']:,.2f}")
        print(f"    Time: {trade['timestamp']}")

    # 12. Add liquidity to pool
    print_section("12. Loly adds liquidity to ETH-SPOT pool")
    liq_result = loly_api.add_liquidity("Loly", "ETH-SPOT", usdc_amount=1000, eth_amount=0.5)
    print(json.dumps(liq_result, indent=2))

    # 13. Check liquidity positions
    print_section("13. Loly checks her liquidity positions")
    liq_positions = loly_api.get_liquidity_positions("Loly")
    print(f"\n  Total Liquidity Positions: {len(liq_positions)}")
    for lp in liq_positions:
        print(f"\n  Market: {lp['market']}")
        print(f"    USDC: ${lp['usdc_amount']:,.2f}")
        print(f"    ETH: {lp['eth_amount']} ETH")
        print(f"    Pool Share: {lp['share']*100:.3f}%")
        print(f"    APY: {lp['apy']:.2f}%")

    # 14. Get Drift Protocol stats
    print_section("14. Loly asks: How's Drift doing?")
    drift_stats = loly_api.get_drift_stats()
    print(f"\n  Protocol: {drift_stats['protocol']}")
    print(f"  Blockchain: {drift_stats['blockchain']}")
    print(f"  Markets: {drift_stats['markets']}")
    print(f"  Total Users: {drift_stats['total_users']}")
    print(f"  Open Positions: {drift_stats['total_positions']}")
    print(f"  24h Volume: ${drift_stats['total_volume_24h']:,.0f}")
    print(f"  TVL: ${drift_stats['tvl']:,.0f}")

    # 15. Get quick stats
    print_section("15. Loly gets quick overview")
    quick = loly_api.quick_stats("Loly")
    print(json.dumps(quick, indent=2))

    # 16. Close leveraged position
    print_section("16. Loly closes her ETH-PERP position")
    close_result = loly_api.close_position("Loly", "ETH-PERP")
    print(json.dumps(close_result, indent=2))

    # 17. Final balance
    print_section("17. Loly checks final balance")
    final_balance = loly_api.get_balance("Loly")
    print(f"\n  USDC: ${final_balance['USDC']:,.2f}")
    print(f"  ETH: {final_balance['ETH']} ETH")
    print(f"  SOL: {final_balance['SOL']} SOL")

    print("\n" + "=" * 70)
    print("  ✅ DEMO COMPLETE! Loly traded ETH on Drift Protocol!")
    print("  💎 NO CENTRALIZED EXCHANGES - Pure DeFi Power! 💎")
    print("=" * 70 + "\n")


if __name__ == '__main__':
    demo_drift_trading()
