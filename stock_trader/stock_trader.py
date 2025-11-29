"""
Stock Trader Agent - Trade stocks and manage portfolios
"""

import json
import os
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import random


class StockTrader:
    """
    Stock Trader Agent - Buy/sell stocks and manage portfolios
    Loly can call this agent at will to trade stocks
    """

    def __init__(self):
        self.data_dir = os.path.join(os.path.dirname(__file__), 'data')

        # Major stocks with mock prices
        self.stocks = {
            # Tech Giants
            'AAPL': {'name': 'Apple Inc.', 'sector': 'Technology', 'price': 178.50},
            'MSFT': {'name': 'Microsoft Corporation', 'sector': 'Technology', 'price': 378.90},
            'GOOGL': {'name': 'Alphabet Inc.', 'sector': 'Technology', 'price': 140.25},
            'AMZN': {'name': 'Amazon.com Inc.', 'sector': 'Consumer', 'price': 151.75},
            'META': {'name': 'Meta Platforms Inc.', 'sector': 'Technology', 'price': 352.80},
            'NVDA': {'name': 'NVIDIA Corporation', 'sector': 'Technology', 'price': 495.20},
            'TSLA': {'name': 'Tesla Inc.', 'sector': 'Automotive', 'price': 242.80},

            # Finance
            'JPM': {'name': 'JPMorgan Chase', 'sector': 'Finance', 'price': 158.30},
            'BAC': {'name': 'Bank of America', 'sector': 'Finance', 'price': 33.45},
            'GS': {'name': 'Goldman Sachs', 'sector': 'Finance', 'price': 384.60},
            'V': {'name': 'Visa Inc.', 'sector': 'Finance', 'price': 258.70},
            'MA': {'name': 'Mastercard', 'sector': 'Finance', 'price': 432.50},

            # Consumer
            'WMT': {'name': 'Walmart Inc.', 'sector': 'Retail', 'price': 163.20},
            'HD': {'name': 'Home Depot', 'sector': 'Retail', 'price': 345.80},
            'NKE': {'name': 'Nike Inc.', 'sector': 'Consumer', 'price': 107.30},
            'SBUX': {'name': 'Starbucks', 'sector': 'Consumer', 'price': 95.40},
            'MCD': {'name': 'McDonalds', 'sector': 'Consumer', 'price': 296.50},

            # Healthcare
            'JNJ': {'name': 'Johnson & Johnson', 'sector': 'Healthcare', 'price': 157.80},
            'UNH': {'name': 'UnitedHealth Group', 'sector': 'Healthcare', 'price': 524.30},
            'PFE': {'name': 'Pfizer Inc.', 'sector': 'Healthcare', 'price': 27.85},
            'LLY': {'name': 'Eli Lilly', 'sector': 'Healthcare', 'price': 588.40},

            # Entertainment & Media
            'DIS': {'name': 'Walt Disney', 'sector': 'Entertainment', 'price': 112.50},
            'NFLX': {'name': 'Netflix Inc.', 'sector': 'Entertainment', 'price': 485.30},
            'SPOT': {'name': 'Spotify', 'sector': 'Entertainment', 'price': 189.20},

            # Other
            'KO': {'name': 'Coca-Cola', 'sector': 'Consumer', 'price': 60.80},
            'PG': {'name': 'Procter & Gamble', 'sector': 'Consumer', 'price': 153.70},
            'XOM': {'name': 'Exxon Mobil', 'sector': 'Energy', 'price': 102.50},
            'CVX': {'name': 'Chevron', 'sector': 'Energy', 'price': 147.30},
        }

        # Data storage
        self.portfolios = {}
        self.orders = {}
        self.balances = {}

        self._initialize_data()

    def _initialize_data(self):
        """Initialize or load existing trading data"""
        os.makedirs(self.data_dir, exist_ok=True)

        # Load portfolios
        portfolio_file = os.path.join(self.data_dir, 'portfolios.json')
        if os.path.exists(portfolio_file):
            with open(portfolio_file, 'r') as f:
                self.portfolios = json.load(f)

        # Load orders
        orders_file = os.path.join(self.data_dir, 'orders.json')
        if os.path.exists(orders_file):
            with open(orders_file, 'r') as f:
                self.orders = json.load(f)

        # Load balances
        balances_file = os.path.join(self.data_dir, 'balances.json')
        if os.path.exists(balances_file):
            with open(balances_file, 'r') as f:
                self.balances = json.load(f)

    def get_all_stocks(self) -> Dict[str, Dict[str, Any]]:
        """Get all available stocks"""
        return self.stocks

    def get_stock_info(self, symbol: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific stock"""
        symbol = symbol.upper()
        if symbol not in self.stocks:
            return None

        stock = self.stocks[symbol].copy()
        stock['symbol'] = symbol
        stock['day_change'] = random.uniform(-5, 5)  # Mock daily change %
        stock['volume'] = random.randint(1000000, 100000000)  # Mock volume
        return stock

    def get_price(self, symbol: str) -> Optional[float]:
        """Get current price of a stock"""
        symbol = symbol.upper()
        if symbol not in self.stocks:
            return None
        return self.stocks[symbol]['price']

    def create_account(self, user_id: str, initial_cash: float = 100000) -> Dict[str, Any]:
        """
        Create a trading account

        Args:
            user_id: User identifier
            initial_cash: Initial cash balance

        Returns:
            Account information
        """
        if user_id not in self.balances:
            self.balances[user_id] = {
                'user_id': user_id,
                'cash': initial_cash,
                'created_at': datetime.now().isoformat()
            }
            self._save_balances()

        if user_id not in self.portfolios:
            self.portfolios[user_id] = {
                'user_id': user_id,
                'holdings': {},
                'created_at': datetime.now().isoformat()
            }
            self._save_portfolios()

        return self.balances[user_id]

    def get_balance(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get account balance"""
        return self.balances.get(user_id)

    def buy_stock(self, user_id: str, symbol: str, shares: int) -> Dict[str, Any]:
        """
        Buy stock

        Args:
            user_id: User identifier
            symbol: Stock symbol
            shares: Number of shares to buy

        Returns:
            Order result
        """
        symbol = symbol.upper()

        if symbol not in self.stocks:
            return {'success': False, 'error': 'Stock not found'}

        if user_id not in self.balances:
            return {'success': False, 'error': 'Account not found'}

        price = self.stocks[symbol]['price']
        total_cost = price * shares
        fee = total_cost * 0.001  # 0.1% fee
        total_with_fee = total_cost + fee

        # Check balance
        balance = self.balances[user_id]
        if balance['cash'] < total_with_fee:
            return {'success': False, 'error': 'Insufficient funds'}

        # Execute order
        balance['cash'] -= total_with_fee

        # Update portfolio
        portfolio = self.portfolios[user_id]
        if symbol in portfolio['holdings']:
            holding = portfolio['holdings'][symbol]
            old_shares = holding['shares']
            old_avg = holding['avg_price']
            new_shares = old_shares + shares
            new_avg = ((old_shares * old_avg) + (shares * price)) / new_shares

            holding['shares'] = new_shares
            holding['avg_price'] = new_avg
        else:
            portfolio['holdings'][symbol] = {
                'symbol': symbol,
                'shares': shares,
                'avg_price': price,
                'purchased_at': datetime.now().isoformat()
            }

        # Record order
        order_id = f"order_{datetime.now().timestamp()}_{random.randint(1000, 9999)}"
        if user_id not in self.orders:
            self.orders[user_id] = []

        order = {
            'order_id': order_id,
            'type': 'buy',
            'symbol': symbol,
            'shares': shares,
            'price': price,
            'total': total_cost,
            'fee': fee,
            'timestamp': datetime.now().isoformat()
        }

        self.orders[user_id].append(order)

        self._save_balances()
        self._save_portfolios()
        self._save_orders()

        return {
            'success': True,
            'order_id': order_id,
            'message': f"Bought {shares} shares of {symbol} @ ${price:.2f}",
            'order': order
        }

    def sell_stock(self, user_id: str, symbol: str, shares: int) -> Dict[str, Any]:
        """
        Sell stock

        Args:
            user_id: User identifier
            symbol: Stock symbol
            shares: Number of shares to sell

        Returns:
            Order result
        """
        symbol = symbol.upper()

        if symbol not in self.stocks:
            return {'success': False, 'error': 'Stock not found'}

        if user_id not in self.portfolios:
            return {'success': False, 'error': 'Portfolio not found'}

        portfolio = self.portfolios[user_id]
        if symbol not in portfolio['holdings']:
            return {'success': False, 'error': 'Stock not in portfolio'}

        holding = portfolio['holdings'][symbol]
        if holding['shares'] < shares:
            return {'success': False, 'error': 'Insufficient shares'}

        price = self.stocks[symbol]['price']
        total_value = price * shares
        fee = total_value * 0.001  # 0.1% fee
        total_with_fee = total_value - fee

        # Execute order
        balance = self.balances[user_id]
        balance['cash'] += total_with_fee

        # Update portfolio
        holding['shares'] -= shares
        if holding['shares'] == 0:
            del portfolio['holdings'][symbol]

        # Record order
        order_id = f"order_{datetime.now().timestamp()}_{random.randint(1000, 9999)}"
        if user_id not in self.orders:
            self.orders[user_id] = []

        order = {
            'order_id': order_id,
            'type': 'sell',
            'symbol': symbol,
            'shares': shares,
            'price': price,
            'total': total_value,
            'fee': fee,
            'timestamp': datetime.now().isoformat()
        }

        self.orders[user_id].append(order)

        self._save_balances()
        self._save_portfolios()
        self._save_orders()

        return {
            'success': True,
            'order_id': order_id,
            'message': f"Sold {shares} shares of {symbol} @ ${price:.2f}",
            'order': order
        }

    def get_portfolio(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get portfolio with current values"""
        if user_id not in self.portfolios:
            return None

        portfolio = self.portfolios[user_id].copy()
        balance = self.balances.get(user_id, {})

        total_value = balance.get('cash', 0)
        total_cost = 0

        for symbol, holding in portfolio['holdings'].items():
            current_price = self.stocks.get(symbol, {}).get('price', 0)
            shares = holding['shares']
            avg_price = holding['avg_price']

            current_value = current_price * shares
            cost_basis = avg_price * shares

            holding['current_price'] = current_price
            holding['current_value'] = current_value
            holding['cost_basis'] = cost_basis
            holding['profit_loss'] = current_value - cost_basis
            holding['profit_loss_pct'] = ((current_value - cost_basis) / cost_basis * 100) if cost_basis > 0 else 0

            total_value += current_value
            total_cost += cost_basis

        portfolio['cash'] = balance.get('cash', 0)
        portfolio['total_value'] = total_value
        portfolio['total_cost'] = total_cost
        portfolio['total_profit_loss'] = total_value - total_cost
        portfolio['total_profit_loss_pct'] = ((total_value - total_cost) / total_cost * 100) if total_cost > 0 else 0

        return portfolio

    def get_order_history(self, user_id: str, limit: int = 50) -> List[Dict[str, Any]]:
        """Get order history"""
        history = self.orders.get(user_id, [])
        return history[-limit:]

    def get_market_summary(self) -> Dict[str, Any]:
        """Get market summary"""
        sectors = {}
        for symbol, stock in self.stocks.items():
            sector = stock['sector']
            if sector not in sectors:
                sectors[sector] = []
            sectors[sector].append(symbol)

        return {
            'total_stocks': len(self.stocks),
            'sectors': {sector: len(stocks) for sector, stocks in sectors.items()},
            'top_gainers': self._get_top_movers('gainers'),
            'top_losers': self._get_top_movers('losers'),
        }

    def _get_top_movers(self, mover_type: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Get top gaining or losing stocks"""
        movers = []
        symbols = list(self.stocks.keys())
        random.shuffle(symbols)

        for symbol in symbols[:limit]:
            stock = self.stocks[symbol]
            change_pct = random.uniform(-8, 15) if mover_type == 'gainers' else random.uniform(-15, -3)
            movers.append({
                'symbol': symbol,
                'name': stock['name'],
                'price': stock['price'],
                'change': change_pct
            })

        movers.sort(key=lambda x: x['change'], reverse=(mover_type == 'gainers'))
        return movers[:limit]

    def _save_portfolios(self):
        """Save portfolios to file"""
        with open(os.path.join(self.data_dir, 'portfolios.json'), 'w') as f:
            json.dump(self.portfolios, f, indent=2)

    def _save_orders(self):
        """Save orders to file"""
        with open(os.path.join(self.data_dir, 'orders.json'), 'w') as f:
            json.dump(self.orders, f, indent=2)

    def _save_balances(self):
        """Save balances to file"""
        with open(os.path.join(self.data_dir, 'balances.json'), 'w') as f:
            json.dump(self.balances, f, indent=2)


# Loly's Interface
class LolyInterface:
    """Simplified interface for Loly to call the Stock Trader"""

    def __init__(self):
        self.agent = StockTrader()

    def get_price(self, symbol: str):
        """Quick price lookup"""
        return self.agent.get_price(symbol)

    def get_portfolio(self, user_id: str):
        """Quick portfolio lookup"""
        return self.agent.get_portfolio(user_id)

    def get_balance(self, user_id: str):
        """Quick balance lookup"""
        return self.agent.get_balance(user_id)

    def all_stocks(self):
        """Get all available stocks"""
        return self.agent.get_all_stocks()
