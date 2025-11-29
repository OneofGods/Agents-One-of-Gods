# Agents One of Gods ⚡

**Powerful AI agents that Loly can call at will!**

## 🏆 Sports Agent - Complete Roster Management System

**The Sports Agent controls ALL rosters across ALL major sports leagues!**
Loly can call this agent at will to get any roster information instantly.

## 💎 Drift Crypto Agent - ETH Trading on Solana DEX

**Trade ETH on Drift Protocol - NO CENTRALIZED EXCHANGES!**
Loly can trade ETH with leverage, add liquidity, and manage positions on Solana's premier DEX.

---

# 🏆 Sports Agent

## Supported Leagues

### American Sports
- **NFL** - National Football League (32 teams)
- **NBA** - National Basketball Association (30 teams)
- **MLB** - Major League Baseball (30 teams)
- **NHL** - National Hockey League (32 teams)
- **MLS** - Major League Soccer (29 teams)

### International Soccer
- **EPL** - English Premier League (20 teams)
- **La Liga** - Spanish La Liga (20 teams)
- **Bundesliga** - German Bundesliga (18 teams)
- **Serie A** - Italian Serie A (20 teams)
- **Ligue 1** - French Ligue 1 (18 teams)

### College Sports
- **NCAA Football** (130 teams)
- **NCAA Basketball** (350 teams)

---

## 🚀 Quick Start for Loly

### Installation

```bash
# No dependencies needed! Pure Python 3.6+
python --version  # Make sure you have Python 3.6 or higher
```

### Run the Demo

```bash
python loly_demo.py
```

This will:
1. Populate sample data across all leagues
2. Show Loly how to interact with the Sports Agent
3. Demonstrate all available functions

---

## 📖 How Loly Uses the Sports Agent

### Import the API

```python
from sports_agent.api import loly_api
```

### Basic Operations

```python
# Say hello
greeting = loly_api.hello()

# Get all available leagues
leagues = loly_api.list_leagues()

# Get a team's roster
roster = loly_api.get_team_roster('NBA', 'Los Angeles Lakers')

# Find a player anywhere
results = loly_api.find_player('LeBron James')

# Get league summary
info = loly_api.get_league_info('NFL')

# Get all teams in a league
teams = loly_api.get_all_teams_in_league('NBA')

# Get overall statistics
stats = loly_api.quick_stats()
```

### Managing Rosters

```python
# Add a new player to a team
loly_api.add_player_to_team('NBA', 'Los Angeles Lakers', {
    'name': 'New Player',
    'position': 'G',
    'number': 99
})

# Add an entire team
loly_api.add_team('NFL', 'Green Bay Packers', [
    {'name': 'Aaron Rodgers', 'position': 'QB', 'number': 12},
    {'name': 'Davante Adams', 'position': 'WR', 'number': 17}
])

# Remove a player
loly_api.remove_player_from_team('NBA', 'Los Angeles Lakers', 'Player Name')
```

### Export Data

```python
# Export all rosters to a file
loly_api.export_everything('my_rosters.json')
```

---

## 🗂️ Project Structure

```
Agents-One-of-Gods/
├── sports_agent/
│   ├── __init__.py           # Main package init
│   ├── sports_agent.py       # Core Sports Agent class
│   ├── sample_data.py        # Sample data generator
│   ├── api/
│   │   ├── __init__.py
│   │   └── loly_api.py       # Loly's API interface
│   └── data/                 # JSON storage for rosters
│       ├── NFL_rosters.json
│       ├── NBA_rosters.json
│       └── ... (auto-generated)
├── loly_demo.py              # Demo script
├── index.html                # Web interface
└── README.md                 # This file
```

---

## 🎯 Features

✅ **12 Major Sports Leagues** - NFL, NBA, MLB, NHL, MLS, EPL, La Liga, Bundesliga, Serie A, Ligue 1, NCAA Football, NCAA Basketball
✅ **Complete Roster Control** - Add, remove, update players and teams
✅ **Fast Search** - Find any player across all leagues instantly
✅ **Persistent Storage** - All data saved to JSON files
✅ **Simple API** - Clean interface designed specifically for Loly
✅ **League Statistics** - Get summaries and stats for any league
✅ **Export/Import** - Backup and restore all roster data

---

## 💡 API Reference

### LolyAPI Methods

| Method | Description |
|--------|-------------|
| `hello()` | Get greeting from Sports Agent |
| `list_leagues()` | Get all available leagues |
| `get_team_roster(league, team)` | Get complete roster for a team |
| `find_player(name, league=None)` | Search for a player |
| `get_league_info(league)` | Get league summary and stats |
| `get_all_teams_in_league(league)` | List all teams in a league |
| `add_team(league, team_name, players)` | Add a new team |
| `add_player_to_team(league, team, player)` | Add player to team |
| `remove_player_from_team(league, team, name)` | Remove player |
| `quick_stats()` | Get overall statistics |
| `export_everything(filename)` | Export all data |

---

## 🎉 Ready to Roll!

The Sports Agent is ready for Loly to call at will!

**Try it out:**
```bash
python loly_demo.py
```

**Happy Days!! Yippie Kay Yay!! 🎊**

---

# 💎 Drift Crypto Agent

## ETH Trading on Solana's Drift Protocol

**NO CENTRALIZED EXCHANGES - Pure DeFi Power!**

### 🚀 Quick Start

```bash
python drift_demo.py
```

### 📖 How Loly Trades on Drift

```python
from crypto_agent.api import loly_api

# Create Drift account
loly_api.create_account("Loly", initial_usdc=10000)

# Check ETH price
eth_price = loly_api.get_price('ETH')

# Buy ETH (spot)
loly_api.buy_eth("Loly", amount=2.0, market="ETH-SPOT")

# Open leveraged position
loly_api.buy_eth("Loly", amount=1.5, leverage=5, market="ETH-PERP")

# Check positions
positions = loly_api.get_all_positions("Loly")

# Add liquidity
loly_api.add_liquidity("Loly", "ETH-SPOT", usdc_amount=1000, eth_amount=0.5)

# Close position
loly_api.close_position("Loly", "ETH-PERP")
```

### 🎯 Drift Features

✅ **Spot Trading** - Buy and sell ETH directly
✅ **Perpetual Futures** - Trade with up to 20x leverage
✅ **Liquidity Pools** - Add liquidity and earn APY
✅ **Position Management** - Track PnL in real-time
✅ **Trade History** - Complete transaction records
✅ **100% DeFi** - Runs on Solana, no CEX needed!

### 💡 Drift API Reference

| Method | Description |
|--------|-------------|
| `create_account(user_id, initial_usdc)` | Create Drift account with USDC |
| `get_balance(user_id)` | Get account balances |
| `buy_eth(user_id, amount, leverage, market)` | Buy ETH (spot or perp) |
| `sell_eth(user_id, amount, leverage, market)` | Sell ETH (spot or perp) |
| `get_position(user_id, market)` | Get position with PnL |
| `get_all_positions(user_id)` | Get all open positions |
| `close_position(user_id, market)` | Close a position |
| `add_liquidity(user_id, market, usdc, eth)` | Add liquidity to pool |
| `get_trade_history(user_id)` | Get trade history |
| `get_drift_stats()` | Get protocol statistics |

---

## 🗂️ Complete Project Structure

```
Agents-One-of-Gods/
├── sports_agent/              # Sports roster management
│   ├── __init__.py
│   ├── sports_agent.py
│   ├── sample_data.py
│   ├── api/
│   │   └── loly_api.py
│   └── data/
│       ├── NFL_rosters.json
│       └── ... (auto-generated)
├── crypto_agent/              # Drift Protocol trading
│   ├── __init__.py
│   ├── drift_agent.py        # Core Drift agent
│   ├── api/
│   │   └── loly_api.py       # Trading API
│   └── data/
│       ├── drift_positions.json
│       ├── drift_balances.json
│       └── ... (auto-generated)
├── loly_demo.py              # Sports agent demo
├── drift_demo.py             # Drift trading demo
├── test_sports_agent.py      # Sports tests
├── index.html
└── README.md
```

---

## 🎉 Ready to Roll!

**Try the demos:**
```bash
# Sports Agent
python loly_demo.py

# Drift Protocol Crypto Agent
python drift_demo.py
```

**Happy Days!! Yippie Kay Yay!! 🎊**
