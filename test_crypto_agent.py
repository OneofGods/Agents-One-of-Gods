"""
Quick test script to verify Crypto Agent functionality
"""

from crypto_agent.api import loly_api


def test_crypto_agent():
    """Run quick tests"""
    print("\n🧪 Testing Crypto Agent...\n")

    # Test 1: Hello
    print("✓ Test 1: Greeting")
    response = loly_api.hello()
    assert "Crypto Agent" in response
    print(f"  {response}")

    # Test 2: List cryptos
    print("\n✓ Test 2: List cryptocurrencies")
    cryptos = loly_api.list_cryptos()
    assert len(cryptos) >= 20
    print(f"  Found {len(cryptos)} cryptocurrencies")

    # Test 3: Get price
    print("\n✓ Test 3: Get BTC price")
    btc_price = loly_api.get_price('BTC')
    assert btc_price is not None
    assert btc_price > 0
    print(f"  BTC Price: ${btc_price:,.2f}")

    # Test 4: Get crypto info
    print("\n✓ Test 4: Get crypto info")
    eth_info = loly_api.get_crypto_info('ETH')
    assert eth_info is not None
    assert 'current_price' in eth_info
    print(f"  ETH: {eth_info['name']} - ${eth_info['current_price']:,.2f}")

    # Test 5: Create portfolio
    print("\n✓ Test 5: Create portfolio")
    result = loly_api.create_portfolio("Test Portfolio", "TestUser")
    assert result['success'] == True
    portfolio_id = result['portfolio']['portfolio_id']
    print(f"  {result['message']}")

    # Test 6: Add to portfolio
    print("\n✓ Test 6: Add crypto to portfolio")
    result = loly_api.add_to_portfolio(portfolio_id, 'BTC', 0.1)
    assert result['success'] == True
    print(f"  {result['message']}")

    # Test 7: Get portfolio
    print("\n✓ Test 7: Get portfolio value")
    portfolio = loly_api.get_portfolio(portfolio_id)
    assert portfolio is not None
    assert 'total_value' in portfolio
    print(f"  Portfolio Value: ${portfolio['total_value']:,.2f}")

    # Test 8: Add wallet
    print("\n✓ Test 8: Add wallet")
    result = loly_api.add_wallet("0xABC123", "Ethereum", "Test Wallet")
    assert result['success'] == True
    wallet_id = result['wallet']['wallet_id']
    print(f"  {result['message']}")

    # Test 9: Add transaction
    print("\n✓ Test 9: Add transaction")
    result = loly_api.add_transaction(wallet_id, 'buy', 'ETH', 1, 2280.00)
    assert result['success'] == True
    print(f"  {result['message']}")

    # Test 10: Get transactions
    print("\n✓ Test 10: Get wallet transactions")
    txs = loly_api.get_wallet_transactions(wallet_id)
    assert len(txs) > 0
    print(f"  Found {len(txs)} transaction(s)")

    # Test 11: Add NFT
    print("\n✓ Test 11: Add NFT")
    result = loly_api.add_nft("Test Collection", "1", "Ethereum", "TestUser")
    assert result['success'] == True
    print(f"  {result['message']}")

    # Test 12: Get NFTs
    print("\n✓ Test 12: Get NFTs")
    nfts = loly_api.get_nfts("TestUser")
    assert len(nfts) > 0
    print(f"  Found {len(nfts)} NFT(s)")

    # Test 13: Add DeFi position
    print("\n✓ Test 13: Add DeFi position")
    result = loly_api.add_defi_position("Aave", "staking", {"ETH": 1}, 5.0, "TestUser")
    assert result['success'] == True
    print(f"  {result['message']}")

    # Test 14: Get DeFi positions
    print("\n✓ Test 14: Get DeFi positions")
    positions = loly_api.get_defi_positions("TestUser")
    assert len(positions) > 0
    print(f"  Found {len(positions)} DeFi position(s)")

    # Test 15: Market summary
    print("\n✓ Test 15: Get market summary")
    market = loly_api.get_market_summary()
    assert 'total_market_cap' in market
    assert 'top_gainers' in market
    print(f"  Market Cap: ${market['total_market_cap']:,.0f}")

    # Test 16: Quick stats
    print("\n✓ Test 16: Quick stats")
    stats = loly_api.quick_stats()
    assert 'total_cryptocurrencies' in stats
    print(f"  Total Cryptos: {stats['total_cryptocurrencies']}")
    print(f"  Portfolios: {stats['total_portfolios']}")
    print(f"  Wallets: {stats['total_wallets']}")

    print("\n" + "=" * 60)
    print("  ✅ ALL TESTS PASSED! Crypto Agent is fully operational!")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    test_crypto_agent()
