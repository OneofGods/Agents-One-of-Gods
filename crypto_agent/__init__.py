"""
Crypto Agent - Drift Protocol Trading on Solana
Trades ETH on Drift Protocol (Solana DEX)
NO CENTRALIZED EXCHANGES - Pure DeFi!

Loly can call this agent at will to trade and manage positions
"""

from .drift_agent import DriftAgent

__version__ = "1.0.0"
__all__ = ["DriftAgent"]
