"""
Demo script showing how Loly can interact with the Crypto Agent
Run this to see all the crypto capabilities!
"""

from crypto_agent.api import loly_api
import json


def print_section(title):
    """Print a fancy section header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def demo_loly_crypto():
    """Demonstrate Loly calling the Crypto Agent"""

    print("\n💎 CRYPTO AGENT - LOLY DEMO 💎\n")

    # 1. Greeting
    print_section("1. Loly says hello to Crypto Agent")
    greeting = loly_api.hello()
    print(f"Crypto Agent: {greeting}")

    # 2. List all cryptos
    print_section("2. Loly asks: What cryptos do you support?")
    cryptos = loly_api.list_cryptos()
    print(f"Total Cryptocurrencies: {len(cryptos)}")
    for symbol, info in list(cryptos.items())[:10]:
        print(f"  • {symbol}: {info['name']} ({info['type']})")
    print(f"  ... and {len(cryptos) - 10} more!")

    # 3. Get quick stats
    print_section("3. Loly asks: Give me quick stats")
    stats = loly_api.quick_stats()
    print(json.dumps(stats, indent=2))

    # 4. Check some prices
    print_section("4. Loly asks: What are BTC and ETH prices?")
    btc_info = loly_api.get_crypto_info('BTC')
    eth_info = loly_api.get_crypto_info('ETH')
    print(f"Bitcoin (BTC): ${btc_info['current_price']:,.2f}")
    print(f"Ethereum (ETH): ${eth_info['current_price']:,.2f}")

    # 5. Get multiple prices
    print_section("5. Loly asks: Get me prices for my watchlist")
    prices = loly_api.get_prices(['BTC', 'ETH', 'SOL', 'ADA', 'MATIC'])
    for symbol, price in prices.items():
        print(f"  {symbol}: ${price:,.2f}")

    # 6. Create a portfolio
    print_section("6. Loly creates a new portfolio")
    result = loly_api.create_portfolio("My Main Portfolio", "Loly")
    print(json.dumps(result, indent=2))
    portfolio_id = result['portfolio']['portfolio_id']

    # 7. Add crypto to portfolio
    print_section("7. Loly adds crypto to portfolio")
    result1 = loly_api.add_to_portfolio(portfolio_id, 'BTC', 0.5)
    print(json.dumps(result1, indent=2))
    result2 = loly_api.add_to_portfolio(portfolio_id, 'ETH', 10)
    print(json.dumps(result2, indent=2))
    result3 = loly_api.add_to_portfolio(portfolio_id, 'SOL', 100)
    print(json.dumps(result3, indent=2))

    # 8. Get portfolio value
    print_section("8. Loly asks: What's my portfolio worth?")
    portfolio = loly_api.get_portfolio(portfolio_id)
    print(f"\nPortfolio: {portfolio['name']}")
    print(f"Owner: {portfolio['owner']}")
    print(f"Total Value: ${portfolio['total_value']:,.2f}")
    print(f"Total Cost: ${portfolio['total_cost']:,.2f}")
    print(f"Profit/Loss: ${portfolio['total_profit_loss']:,.2f} ({portfolio['total_profit_loss_pct']:.2f}%)")
    print("\nHoldings:")
    for symbol, holding in portfolio['holdings'].items():
        print(f"  {symbol}:")
        print(f"    Amount: {holding['amount']}")
        print(f"    Value: ${holding['current_value']:,.2f}")
        print(f"    P/L: ${holding['profit_loss']:,.2f} ({holding['profit_loss_pct']:.2f}%)")

    # 9. Add a wallet
    print_section("9. Loly adds a wallet to track")
    wallet_result = loly_api.add_wallet(
        "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",
        "Ethereum",
        "My Main Wallet"
    )
    print(json.dumps(wallet_result, indent=2))
    wallet_id = wallet_result['wallet']['wallet_id']

    # 10. Add transactions
    print_section("10. Loly records some transactions")
    tx1 = loly_api.add_transaction(wallet_id, 'buy', 'ETH', 5, 2250.00)
    print(json.dumps(tx1, indent=2))
    tx2 = loly_api.add_transaction(wallet_id, 'swap', 'UNI', 100, 6.50)
    print(json.dumps(tx2, indent=2))

    # 11. Get wallet transactions
    print_section("11. Loly asks: Show my wallet transactions")
    txs = loly_api.get_wallet_transactions(wallet_id)
    print(f"Total Transactions: {len(txs)}")
    for tx in txs:
        print(f"  {tx['type'].upper()}: {tx['amount']} {tx['symbol']} @ ${tx['price']:,.2f}")
        print(f"    Hash: {tx['tx_hash']}")
        print(f"    Time: {tx['timestamp']}")

    # 12. Add NFTs
    print_section("12. Loly adds NFTs to track")
    nft1 = loly_api.add_nft(
        "Bored Ape Yacht Club",
        "1234",
        "Ethereum",
        "Loly",
        {"rarity": "Rare", "attributes": ["Gold Fur", "Laser Eyes"]}
    )
    print(json.dumps(nft1, indent=2))

    # 13. Get NFTs
    print_section("13. Loly asks: Show my NFTs")
    nfts = loly_api.get_nfts("Loly")
    print(f"Total NFTs: {len(nfts)}")
    for nft in nfts:
        print(f"  {nft['collection']} #{nft['token_id']}")
        print(f"    Blockchain: {nft['blockchain']}")
        print(f"    Metadata: {nft['metadata']}")

    # 14. Add DeFi positions
    print_section("14. Loly adds DeFi positions")
    defi1 = loly_api.add_defi_position(
        "Aave",
        "lending",
        {"USDC": 10000, "DAI": 5000},
        5.5,
        "Loly"
    )
    print(json.dumps(defi1, indent=2))

    defi2 = loly_api.add_defi_position(
        "Uniswap",
        "liquidity_pool",
        {"ETH": 2, "USDC": 4560},
        12.3,
        "Loly"
    )
    print(json.dumps(defi2, indent=2))

    # 15. Get DeFi positions
    print_section("15. Loly asks: Show my DeFi positions")
    positions = loly_api.get_defi_positions("Loly")
    print(f"Total DeFi Positions: {len(positions)}")
    for pos in positions:
        print(f"\n  {pos['protocol']} - {pos['type']}")
        print(f"    APY: {pos['apy']}%")
        print(f"    Current Value: ${pos['current_value']:,.2f}")
        print(f"    Tokens:")
        for token, amount in pos['tokens'].items():
            print(f"      {token}: {amount}")

    # 16. Market summary
    print_section("16. Loly asks: How's the market?")
    market = loly_api.get_market_summary()
    print(f"\nTotal Market Cap: ${market['total_market_cap']:,.0f}")
    print(f"BTC Dominance: {market['btc_dominance']}%")
    print(f"ETH Dominance: {market['eth_dominance']}%")

    print("\nTop Gainers (24h):")
    for coin in market['top_gainers']:
        print(f"  {coin['symbol']}: ${coin['price']:,.4f} (+{coin['change_24h']:.2f}%)")

    print("\nTop Losers (24h):")
    for coin in market['top_losers']:
        print(f"  {coin['symbol']}: ${coin['price']:,.4f} ({coin['change_24h']:.2f}%)")

    print("\n" + "=" * 60)
    print("  ✅ DEMO COMPLETE! Crypto Agent is ready for Loly!")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    demo_loly_crypto()
