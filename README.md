# Agents One of Gods ⚡

## Sports Agent - Complete Roster Management System

**The Sports Agent controls ALL rosters across ALL major sports leagues!**
Loly can call this agent at will to get any roster information instantly.

---

## 🏆 Supported Leagues

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
