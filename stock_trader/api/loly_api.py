"""
API Interface for Loly to trade stocks
Simple, clean functions for stock trading
"""

from ..stock_trader import StockTrader, LolyInterface
from typing import Dict, List, Optional, Any


class LolyAPI:
    """
    Loly's dedicated API to the Stock Trader
    Trade stocks like a pro!
    """

    def __init__(self):
        self.interface = LolyInterface()
        self.agent = self.interface.agent

    def hello(self) -> str:
        """Greeting from Stock Trader"""
        return "Stock Trader ready! Trade stocks from major markets. What do you need, Loly?"

    def list_stocks(self) -> Dict[str, Dict[str, Any]]:
        """
        Get all available stocks

        Returns:
            Dictionary of all stocks
        """
        return self.interface.all_stocks()

    def get_stock_info(self, symbol: str) -> Optional[Dict[str, Any]]:
        """
        Get stock information

        Args:
            symbol: Stock symbol (e.g., 'AAPL', 'TSLA')

        Returns:
            Stock info with current price
        """
        return self.agent.get_stock_info(symbol)

    def get_price(self, symbol: str) -> Optional[float]:
        """
        Get current stock price

        Args:
            symbol: Stock symbol

        Returns:
            Current price
        """
        return self.interface.get_price(symbol)

    def create_account(self, user_id: str = "Loly", initial_cash: float = 100000) -> Dict[str, Any]:
        """
        Create a trading account

        Args:
            user_id: User identifier
            initial_cash: Initial cash balance

        Returns:
            Account info
        """
        account = self.agent.create_account(user_id, initial_cash)
        return {
            'success': True,
            'message': f"Trading account created with ${initial_cash:,.0f}",
            'account': account
        }

    def get_balance(self, user_id: str = "Loly") -> Optional[Dict[str, Any]]:
        """
        Get account balance

        Args:
            user_id: User identifier

        Returns:
            Balance info
        """
        return self.interface.get_balance(user_id)

    def buy(self, user_id: str, symbol: str, shares: int) -> Dict[str, Any]:
        """
        Buy stock

        Args:
            user_id: User identifier
            symbol: Stock symbol
            shares: Number of shares

        Returns:
            Order result
        """
        return self.agent.buy_stock(user_id, symbol, shares)

    def sell(self, user_id: str, symbol: str, shares: int) -> Dict[str, Any]:
        """
        Sell stock

        Args:
            user_id: User identifier
            symbol: Stock symbol
            shares: Number of shares

        Returns:
            Order result
        """
        return self.agent.sell_stock(user_id, symbol, shares)

    def get_portfolio(self, user_id: str = "Loly") -> Optional[Dict[str, Any]]:
        """
        Get portfolio with current values

        Args:
            user_id: User identifier

        Returns:
            Portfolio with P&L
        """
        return self.interface.get_portfolio(user_id)

    def get_order_history(self, user_id: str = "Loly", limit: int = 50) -> List[Dict[str, Any]]:
        """
        Get order history

        Args:
            user_id: User identifier
            limit: Number of orders to return

        Returns:
            List of orders
        """
        return self.agent.get_order_history(user_id, limit)

    def get_market_summary(self) -> Dict[str, Any]:
        """
        Get market summary

        Returns:
            Market stats with gainers/losers
        """
        return self.agent.get_market_summary()

    def quick_stats(self, user_id: str = "Loly") -> Dict[str, Any]:
        """
        Get quick overview

        Args:
            user_id: User identifier

        Returns:
            Quick stats
        """
        balance = self.get_balance(user_id)
        portfolio = self.get_portfolio(user_id)
        market = self.get_market_summary()

        return {
            'cash': balance.get('cash', 0) if balance else 0,
            'portfolio_value': portfolio.get('total_value', 0) if portfolio else 0,
            'total_profit_loss': portfolio.get('total_profit_loss', 0) if portfolio else 0,
            'holdings_count': len(portfolio.get('holdings', {})) if portfolio else 0,
            'market': market
        }


# Quick access instance for Loly
loly_api = LolyAPI()
