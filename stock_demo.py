"""
Stock Trader Demo - Trade stocks in major markets
Shows how Loly can buy/sell stocks and manage portfolios
"""

from stock_trader.api import loly_api
import json


def print_section(title):
    """Print a fancy section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def demo_stock_trading():
    """Demonstrate Loly trading stocks"""

    print("\n📈 STOCK TRADER - TRADE LIKE A PRO 📈\n")

    # 1. Greeting
    print_section("1. Loly says hello to Stock Trader")
    greeting = loly_api.hello()
    print(f"Stock Trader: {greeting}")

    # 2. Check available stocks
    print_section("2. Loly asks: What stocks can I trade?")
    stocks = loly_api.list_stocks()
    print(f"\nTotal Stocks Available: {len(stocks)}")

    # Group by sector
    sectors = {}
    for symbol, stock in stocks.items():
        sector = stock['sector']
        if sector not in sectors:
            sectors[sector] = []
        sectors[sector].append(f"{symbol} - {stock['name']}")

    for sector, stock_list in sectors.items():
        print(f"\n  {sector}:")
        for stock in stock_list[:5]:  # Show first 5 per sector
            print(f"    {stock}")
        if len(stock_list) > 5:
            print(f"    ... and {len(stock_list) - 5} more")

    # 3. Get stock info
    print_section("3. Loly checks AAPL stock info")
    aapl = loly_api.get_stock_info('AAPL')
    print(f"\n  Symbol: {aapl['symbol']}")
    print(f"  Name: {aapl['name']}")
    print(f"  Sector: {aapl['sector']}")
    print(f"  Price: ${aapl['price']:.2f}")
    print(f"  Day Change: {aapl['day_change']:+.2f}%")
    print(f"  Volume: {aapl['volume']:,}")

    # 4. Create trading account
    print_section("4. Loly creates a trading account")
    account = loly_api.create_account("Loly", initial_cash=100000)
    print(json.dumps(account, indent=2))

    # 5. Check balance
    print_section("5. Loly checks her balance")
    balance = loly_api.get_balance("Loly")
    print(f"\n  Cash: ${balance['cash']:,.2f}")

    # 6. Buy AAPL
    print_section("6. Loly buys 50 shares of AAPL")
    buy_aapl = loly_api.buy("Loly", "AAPL", 50)
    print(json.dumps(buy_aapl, indent=2))

    # 7. Buy TSLA
    print_section("7. Loly buys 20 shares of TSLA")
    buy_tsla = loly_api.buy("Loly", "TSLA", 20)
    print(json.dumps(buy_tsla, indent=2))

    # 8. Buy NVDA
    print_section("8. Loly buys 10 shares of NVDA")
    buy_nvda = loly_api.buy("Loly", "NVDA", 10)
    print(json.dumps(buy_nvda, indent=2))

    # 9. Buy MSFT
    print_section("9. Loly buys 15 shares of MSFT")
    buy_msft = loly_api.buy("Loly", "MSFT", 15)
    print(json.dumps(buy_msft, indent=2))

    # 10. Check portfolio
    print_section("10. Loly checks her portfolio")
    portfolio = loly_api.get_portfolio("Loly")
    print(f"\n  Cash: ${portfolio['cash']:,.2f}")
    print(f"  Total Value: ${portfolio['total_value']:,.2f}")
    print(f"  Total Cost: ${portfolio['total_cost']:,.2f}")
    print(f"  Profit/Loss: ${portfolio['total_profit_loss']:,.2f} ({portfolio['total_profit_loss_pct']:+.2f}%)")

    print("\n  Holdings:")
    for symbol, holding in portfolio['holdings'].items():
        print(f"\n  {symbol}:")
        print(f"    Shares: {holding['shares']}")
        print(f"    Avg Price: ${holding['avg_price']:.2f}")
        print(f"    Current Price: ${holding['current_price']:.2f}")
        print(f"    Value: ${holding['current_value']:,.2f}")
        print(f"    P&L: ${holding['profit_loss']:,.2f} ({holding['profit_loss_pct']:+.2f}%)")

    # 11. Get order history
    print_section("11. Loly checks her order history")
    orders = loly_api.get_order_history("Loly")
    print(f"\n  Total Orders: {len(orders)}")
    for order in orders:
        print(f"\n  {order['type'].upper()} {order['shares']} {order['symbol']}")
        print(f"    Price: ${order['price']:.2f}")
        print(f"    Total: ${order['total']:,.2f}")
        print(f"    Fee: ${order['fee']:.2f}")
        print(f"    Time: {order['timestamp']}")

    # 12. Sell some TSLA
    print_section("12. Loly sells 10 shares of TSLA")
    sell_tsla = loly_api.sell("Loly", "TSLA", 10)
    print(json.dumps(sell_tsla, indent=2))

    # 13. Check updated balance
    print_section("13. Loly checks updated balance")
    updated_balance = loly_api.get_balance("Loly")
    print(f"\n  Cash: ${updated_balance['cash']:,.2f}")

    # 14. Get market summary
    print_section("14. Loly asks: How's the market doing?")
    market = loly_api.get_market_summary()
    print(f"\n  Total Stocks: {market['total_stocks']}")
    print(f"\n  Sectors:")
    for sector, count in market['sectors'].items():
        print(f"    {sector}: {count} stocks")

    print(f"\n  Top Gainers:")
    for stock in market['top_gainers']:
        print(f"    {stock['symbol']}: ${stock['price']:.2f} (+{stock['change']:.2f}%)")

    print(f"\n  Top Losers:")
    for stock in market['top_losers']:
        print(f"    {stock['symbol']}: ${stock['price']:.2f} ({stock['change']:.2f}%)")

    # 15. Quick stats
    print_section("15. Loly gets quick overview")
    stats = loly_api.quick_stats("Loly")
    print(json.dumps(stats, indent=2))

    # 16. Final portfolio
    print_section("16. Loly checks final portfolio")
    final_portfolio = loly_api.get_portfolio("Loly")
    print(f"\n  💰 Final Summary 💰")
    print(f"  Cash: ${final_portfolio['cash']:,.2f}")
    print(f"  Portfolio Value: ${final_portfolio['total_value']:,.2f}")
    print(f"  Total Profit/Loss: ${final_portfolio['total_profit_loss']:,.2f}")
    print(f"  Holdings: {len(final_portfolio['holdings'])} stocks")

    print("\n" + "=" * 70)
    print("  ✅ DEMO COMPLETE! Loly is trading stocks like a pro!")
    print("  📈 ALWAYS BUILD TO WIN! 📈")
    print("=" * 70 + "\n")


if __name__ == '__main__':
    demo_stock_trading()
