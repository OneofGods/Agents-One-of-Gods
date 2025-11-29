"""
Drift Protocol Agent - Solana DEX Trading
Focus: ETH trading on Drift Protocol
NO CENTRALIZED EXCHANGES - Pure DeFi Power!
"""

import json
import os
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import random


class DriftAgent:
    """
    Drift Protocol Agent - Trades ETH on Solana's Drift DEX
    Loly can call this agent at will to trade and manage positions

    Drift Protocol: Decentralized perpetuals and spot exchange on Solana
    """

    def __init__(self):
        self.data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.protocol = "Drift Protocol"
        self.blockchain = "Solana"

        # Supported markets on Drift (starting with ETH)
        self.markets = {
            'ETH-PERP': {
                'name': 'Ethereum Perpetual',
                'symbol': 'ETH-PERP',
                'type': 'Perpetual',
                'base': 'ETH',
                'quote': 'USDC',
                'leverage_max': 20,
            },
            'ETH-SPOT': {
                'name': 'Ethereum Spot',
                'symbol': 'ETH-SPOT',
                'type': 'Spot',
                'base': 'ETH',
                'quote': 'USDC',
                'leverage_max': 1,
            },
        }

        # Mock price data (in production, this would come from Drift API)
        self.current_prices = {
            'ETH': 2280.75,
            'SOL': 98.40,
            'USDC': 1.00,
        }

        # Data storage
        self.positions = {}
        self.orders = {}
        self.trade_history = {}
        self.balances = {}
        self.liquidity_positions = {}

        self._initialize_data()

    def _initialize_data(self):
        """Initialize or load existing Drift trading data"""
        os.makedirs(self.data_dir, exist_ok=True)

        # Load positions
        positions_file = os.path.join(self.data_dir, 'drift_positions.json')
        if os.path.exists(positions_file):
            with open(positions_file, 'r') as f:
                self.positions = json.load(f)

        # Load orders
        orders_file = os.path.join(self.data_dir, 'drift_orders.json')
        if os.path.exists(orders_file):
            with open(orders_file, 'r') as f:
                self.orders = json.load(f)

        # Load trade history
        history_file = os.path.join(self.data_dir, 'drift_history.json')
        if os.path.exists(history_file):
            with open(history_file, 'r') as f:
                self.trade_history = json.load(f)

        # Load balances
        balances_file = os.path.join(self.data_dir, 'drift_balances.json')
        if os.path.exists(balances_file):
            with open(balances_file, 'r') as f:
                self.balances = json.load(f)

        # Load liquidity positions
        lp_file = os.path.join(self.data_dir, 'drift_liquidity.json')
        if os.path.exists(lp_file):
            with open(lp_file, 'r') as f:
                self.liquidity_positions = json.load(f)

    def get_markets(self) -> Dict[str, Dict[str, Any]]:
        """Get all available markets on Drift"""
        return self.markets

    def get_market_info(self, market: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific market"""
        market_data = self.markets.get(market.upper())
        if not market_data:
            return None

        info = market_data.copy()
        base = market_data['base']
        info['current_price'] = self.current_prices.get(base, 0)
        info['24h_volume'] = random.uniform(1000000, 10000000)  # Mock volume
        info['24h_change'] = random.uniform(-5, 5)  # Mock price change
        return info

    def get_price(self, asset: str) -> Optional[float]:
        """Get current price of an asset"""
        return self.current_prices.get(asset.upper())

    def create_user_account(self, user_id: str, initial_usdc: float = 10000) -> Dict[str, Any]:
        """
        Create a Drift user account with initial USDC balance

        Args:
            user_id: User identifier
            initial_usdc: Initial USDC balance

        Returns:
            Account information
        """
        if user_id not in self.balances:
            self.balances[user_id] = {
                'user_id': user_id,
                'USDC': initial_usdc,
                'ETH': 0,
                'SOL': 0,
                'created_at': datetime.now().isoformat()
            }
            self._save_balances()

        return self.balances[user_id]

    def get_balance(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get user balance"""
        return self.balances.get(user_id)

    def place_market_order(self, user_id: str, market: str, side: str,
                          size: float, leverage: int = 1) -> Dict[str, Any]:
        """
        Place a market order on Drift

        Args:
            user_id: User identifier
            market: Market symbol (e.g., 'ETH-PERP', 'ETH-SPOT')
            side: 'buy' or 'sell'
            size: Order size in ETH
            leverage: Leverage (1-20 for perps, 1 for spot)

        Returns:
            Order result
        """
        market = market.upper()
        if market not in self.markets:
            return {'success': False, 'error': 'Market not found'}

        if user_id not in self.balances:
            return {'success': False, 'error': 'User account not found'}

        market_info = self.markets[market]
        base_asset = market_info['base']
        current_price = self.current_prices.get(base_asset, 0)

        # Calculate order value
        order_value = size * current_price
        required_margin = order_value / leverage if leverage > 1 else order_value

        # Check balance
        user_balance = self.balances[user_id]
        if side.lower() == 'buy':
            if user_balance['USDC'] < required_margin:
                return {'success': False, 'error': 'Insufficient USDC balance'}
        elif side.lower() == 'sell':
            if user_balance.get(base_asset, 0) < size:
                return {'success': False, 'error': f'Insufficient {base_asset} balance'}

        # Execute order
        order_id = f"drift_{datetime.now().timestamp()}_{random.randint(1000, 9999)}"

        if side.lower() == 'buy':
            user_balance['USDC'] -= required_margin
            user_balance[base_asset] = user_balance.get(base_asset, 0) + size
        else:  # sell
            user_balance[base_asset] -= size
            user_balance['USDC'] += order_value

        # Create position for perps
        if market_info['type'] == 'Perpetual':
            position_id = f"{user_id}_{market}"
            if position_id not in self.positions:
                self.positions[position_id] = {
                    'position_id': position_id,
                    'user_id': user_id,
                    'market': market,
                    'size': 0,
                    'entry_price': 0,
                    'leverage': leverage,
                    'unrealized_pnl': 0,
                    'opened_at': datetime.now().isoformat()
                }

            position = self.positions[position_id]
            if side.lower() == 'buy':
                position['size'] += size
                position['entry_price'] = current_price
            else:
                position['size'] -= size

        # Record trade
        if user_id not in self.trade_history:
            self.trade_history[user_id] = []

        trade = {
            'order_id': order_id,
            'market': market,
            'side': side.lower(),
            'size': size,
            'price': current_price,
            'value': order_value,
            'leverage': leverage,
            'fee': order_value * 0.001,  # 0.1% fee
            'timestamp': datetime.now().isoformat()
        }

        self.trade_history[user_id].append(trade)

        # Save data
        self._save_balances()
        self._save_positions()
        self._save_history()

        return {
            'success': True,
            'order_id': order_id,
            'message': f"{side.upper()} {size} {base_asset} @ ${current_price:,.2f}",
            'trade': trade
        }

    def get_position(self, user_id: str, market: str) -> Optional[Dict[str, Any]]:
        """Get position for a market"""
        position_id = f"{user_id}_{market.upper()}"
        position = self.positions.get(position_id)

        if not position:
            return None

        # Calculate current PnL
        market_info = self.markets.get(market.upper())
        if market_info:
            base_asset = market_info['base']
            current_price = self.current_prices.get(base_asset, 0)
            entry_price = position['entry_price']
            size = position['size']

            pnl = (current_price - entry_price) * size
            pnl_pct = ((current_price - entry_price) / entry_price * 100) if entry_price > 0 else 0

            position['current_price'] = current_price
            position['unrealized_pnl'] = pnl
            position['unrealized_pnl_pct'] = pnl_pct

        return position

    def get_all_positions(self, user_id: str) -> List[Dict[str, Any]]:
        """Get all positions for a user"""
        user_positions = []

        for position_id, position in self.positions.items():
            if position['user_id'] == user_id and position['size'] != 0:
                updated_position = self.get_position(user_id, position['market'])
                if updated_position:
                    user_positions.append(updated_position)

        return user_positions

    def close_position(self, user_id: str, market: str) -> Dict[str, Any]:
        """Close a position"""
        position = self.get_position(user_id, market)

        if not position:
            return {'success': False, 'error': 'Position not found'}

        size = position['size']
        if size == 0:
            return {'success': False, 'error': 'No open position'}

        # Close position (opposite side of original)
        side = 'sell' if size > 0 else 'buy'
        result = self.place_market_order(user_id, market, side, abs(size), 1)

        if result['success']:
            # Clear position
            position_id = f"{user_id}_{market.upper()}"
            if position_id in self.positions:
                self.positions[position_id]['size'] = 0
                self._save_positions()

            return {
                'success': True,
                'message': f"Position closed: {market}",
                'realized_pnl': position.get('unrealized_pnl', 0)
            }

        return result

    def add_liquidity(self, user_id: str, market: str, usdc_amount: float,
                     eth_amount: float) -> Dict[str, Any]:
        """
        Add liquidity to a Drift market

        Args:
            user_id: User identifier
            market: Market symbol
            usdc_amount: USDC to add
            eth_amount: ETH to add

        Returns:
            Liquidity position info
        """
        if user_id not in self.balances:
            return {'success': False, 'error': 'User account not found'}

        balance = self.balances[user_id]

        if balance['USDC'] < usdc_amount:
            return {'success': False, 'error': 'Insufficient USDC'}

        if balance.get('ETH', 0) < eth_amount:
            return {'success': False, 'error': 'Insufficient ETH'}

        # Deduct from balance
        balance['USDC'] -= usdc_amount
        balance['ETH'] -= eth_amount

        # Create liquidity position
        lp_id = f"{user_id}_{market}_{datetime.now().timestamp()}"

        self.liquidity_positions[lp_id] = {
            'lp_id': lp_id,
            'user_id': user_id,
            'market': market,
            'usdc_amount': usdc_amount,
            'eth_amount': eth_amount,
            'share': 0.001,  # Mock pool share
            'apy': random.uniform(5, 25),  # Mock APY
            'created_at': datetime.now().isoformat()
        }

        self._save_balances()
        self._save_liquidity()

        return {
            'success': True,
            'message': f"Liquidity added to {market}",
            'position': self.liquidity_positions[lp_id]
        }

    def get_liquidity_positions(self, user_id: str) -> List[Dict[str, Any]]:
        """Get all liquidity positions for a user"""
        return [
            lp for lp in self.liquidity_positions.values()
            if lp['user_id'] == user_id
        ]

    def get_trade_history(self, user_id: str, limit: int = 50) -> List[Dict[str, Any]]:
        """Get trade history for a user"""
        history = self.trade_history.get(user_id, [])
        return history[-limit:]

    def get_stats(self) -> Dict[str, Any]:
        """Get Drift Protocol stats"""
        return {
            'protocol': self.protocol,
            'blockchain': self.blockchain,
            'markets': len(self.markets),
            'total_users': len(self.balances),
            'total_positions': len([p for p in self.positions.values() if p['size'] != 0]),
            'total_volume_24h': random.uniform(10000000, 50000000),  # Mock volume
            'tvl': random.uniform(50000000, 200000000),  # Mock TVL
        }

    def _save_positions(self):
        """Save positions to file"""
        with open(os.path.join(self.data_dir, 'drift_positions.json'), 'w') as f:
            json.dump(self.positions, f, indent=2)

    def _save_orders(self):
        """Save orders to file"""
        with open(os.path.join(self.data_dir, 'drift_orders.json'), 'w') as f:
            json.dump(self.orders, f, indent=2)

    def _save_history(self):
        """Save trade history to file"""
        with open(os.path.join(self.data_dir, 'drift_history.json'), 'w') as f:
            json.dump(self.trade_history, f, indent=2)

    def _save_balances(self):
        """Save balances to file"""
        with open(os.path.join(self.data_dir, 'drift_balances.json'), 'w') as f:
            json.dump(self.balances, f, indent=2)

    def _save_liquidity(self):
        """Save liquidity positions to file"""
        with open(os.path.join(self.data_dir, 'drift_liquidity.json'), 'w') as f:
            json.dump(self.liquidity_positions, f, indent=2)


# Loly's Interface - Simple functions for quick access
class LolyInterface:
    """Simplified interface for Loly to call the Drift Agent"""

    def __init__(self):
        self.agent = DriftAgent()

    def get_price(self, asset: str):
        """Quick price lookup"""
        return self.agent.get_price(asset)

    def get_balance(self, user_id: str):
        """Quick balance lookup"""
        return self.agent.get_balance(user_id)

    def get_positions(self, user_id: str):
        """Quick positions lookup"""
        return self.agent.get_all_positions(user_id)

    def get_stats(self):
        """Quick stats"""
        return self.agent.get_stats()
