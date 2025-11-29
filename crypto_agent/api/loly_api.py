"""
API Interface for Loly to interact with Drift Protocol
Simple, clean functions for ETH trading on Solana's Drift DEX
NO CENTRALIZED EXCHANGES - Pure DeFi!
"""

from ..drift_agent import DriftAgent, LolyInterface
from typing import Dict, List, Optional, Any


class LolyAPI:
    """
    Loly's dedicated API to Drift Protocol
    Trade ETH on Solana's premier DEX!
    """

    def __init__(self):
        self.interface = LolyInterface()
        self.agent = self.interface.agent

    def hello(self) -> str:
        """Greeting from Drift Agent"""
        return "Drift Protocol Agent ready! Trade ETH on Solana DEX. NO CENTRALIZED EXCHANGES! What do you need, Loly?"

    def get_markets(self) -> Dict[str, Dict[str, Any]]:
        """
        Get all available markets on Drift

        Returns:
            Dictionary of all markets
        """
        return self.agent.get_markets()

    def get_market_info(self, market: str) -> Optional[Dict[str, Any]]:
        """
        Get market information

        Args:
            market: Market symbol (e.g., 'ETH-PERP', 'ETH-SPOT')

        Returns:
            Market info with current price and volume
        """
        return self.agent.get_market_info(market)

    def get_price(self, asset: str) -> Optional[float]:
        """
        Get current price

        Args:
            asset: Asset symbol (e.g., 'ETH', 'SOL')

        Returns:
            Current price
        """
        return self.interface.get_price(asset)

    def create_account(self, user_id: str = "Loly", initial_usdc: float = 10000) -> Dict[str, Any]:
        """
        Create a Drift account

        Args:
            user_id: User identifier
            initial_usdc: Initial USDC balance

        Returns:
            Account info
        """
        account = self.agent.create_user_account(user_id, initial_usdc)
        return {
            'success': True,
            'message': f"Account created with ${initial_usdc:,.0f} USDC",
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

    def buy_eth(self, user_id: str, amount: float, leverage: int = 1,
                market: str = "ETH-SPOT") -> Dict[str, Any]:
        """
        Buy ETH on Drift

        Args:
            user_id: User identifier
            amount: Amount of ETH to buy
            leverage: Leverage (1 for spot, up to 20 for perps)
            market: Market to trade ('ETH-SPOT' or 'ETH-PERP')

        Returns:
            Trade result
        """
        return self.agent.place_market_order(user_id, market, 'buy', amount, leverage)

    def sell_eth(self, user_id: str, amount: float, leverage: int = 1,
                 market: str = "ETH-SPOT") -> Dict[str, Any]:
        """
        Sell ETH on Drift

        Args:
            user_id: User identifier
            amount: Amount of ETH to sell
            leverage: Leverage (1 for spot, up to 20 for perps)
            market: Market to trade ('ETH-SPOT' or 'ETH-PERP')

        Returns:
            Trade result
        """
        return self.agent.place_market_order(user_id, market, 'sell', amount, leverage)

    def get_position(self, user_id: str, market: str = "ETH-PERP") -> Optional[Dict[str, Any]]:
        """
        Get position for a market

        Args:
            user_id: User identifier
            market: Market symbol

        Returns:
            Position info with PnL
        """
        return self.agent.get_position(user_id, market)

    def get_all_positions(self, user_id: str = "Loly") -> List[Dict[str, Any]]:
        """
        Get all positions

        Args:
            user_id: User identifier

        Returns:
            List of positions
        """
        return self.interface.get_positions(user_id)

    def close_position(self, user_id: str, market: str = "ETH-PERP") -> Dict[str, Any]:
        """
        Close a position

        Args:
            user_id: User identifier
            market: Market symbol

        Returns:
            Close result with realized PnL
        """
        return self.agent.close_position(user_id, market)

    def add_liquidity(self, user_id: str, market: str, usdc_amount: float,
                     eth_amount: float) -> Dict[str, Any]:
        """
        Add liquidity to Drift pool

        Args:
            user_id: User identifier
            market: Market symbol
            usdc_amount: USDC amount
            eth_amount: ETH amount

        Returns:
            Liquidity position info
        """
        return self.agent.add_liquidity(user_id, market, usdc_amount, eth_amount)

    def get_liquidity_positions(self, user_id: str = "Loly") -> List[Dict[str, Any]]:
        """
        Get liquidity positions

        Args:
            user_id: User identifier

        Returns:
            List of liquidity positions
        """
        return self.agent.get_liquidity_positions(user_id)

    def get_trade_history(self, user_id: str = "Loly", limit: int = 50) -> List[Dict[str, Any]]:
        """
        Get trade history

        Args:
            user_id: User identifier
            limit: Number of trades to return

        Returns:
            List of trades
        """
        return self.agent.get_trade_history(user_id, limit)

    def get_drift_stats(self) -> Dict[str, Any]:
        """
        Get Drift Protocol statistics

        Returns:
            Protocol stats
        """
        return self.interface.get_stats()

    def quick_stats(self, user_id: str = "Loly") -> Dict[str, Any]:
        """
        Get quick overview

        Args:
            user_id: User identifier

        Returns:
            Quick stats
        """
        balance = self.get_balance(user_id)
        positions = self.get_all_positions(user_id)
        drift_stats = self.get_drift_stats()

        return {
            'protocol': drift_stats['protocol'],
            'blockchain': drift_stats['blockchain'],
            'eth_price': self.get_price('ETH'),
            'user_balance': balance,
            'open_positions': len(positions),
            'protocol_stats': drift_stats
        }


# Quick access instance for Loly
loly_api = LolyAPI()
