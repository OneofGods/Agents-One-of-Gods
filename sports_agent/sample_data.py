"""
Sample data generator for Sports Agent
Populates the system with example teams and rosters
"""

from sports_agent import SportsAgent


def populate_sample_data():
    """Populate the Sports Agent with sample data"""
    agent = SportsAgent()

    # NFL Teams
    nfl_teams = {
        'Kansas City Chiefs': [
            {'name': 'Patrick Mahomes', 'position': 'QB', 'number': 15},
            {'name': 'Travis Kelce', 'position': 'TE', 'number': 87},
            {'name': 'Chris Jones', 'position': 'DT', 'number': 95},
        ],
        'San Francisco 49ers': [
            {'name': 'Brock Purdy', 'position': 'QB', 'number': 13},
            {'name': 'George Kittle', 'position': 'TE', 'number': 85},
            {'name': 'Nick Bosa', 'position': 'DE', 'number': 97},
        ],
        'Dallas Cowboys': [
            {'name': 'Dak Prescott', 'position': 'QB', 'number': 4},
            {'name': 'CeeDee Lamb', 'position': 'WR', 'number': 88},
            {'name': 'Micah Parsons', 'position': 'LB', 'number': 11},
        ],
    }

    for team, players in nfl_teams.items():
        agent.set_roster('NFL', team, players)

    # NBA Teams
    nba_teams = {
        'Los Angeles Lakers': [
            {'name': 'LeBron James', 'position': 'F', 'number': 23},
            {'name': 'Anthony Davis', 'position': 'F-C', 'number': 3},
            {'name': "D'Angelo Russell", 'position': 'G', 'number': 1},
        ],
        'Boston Celtics': [
            {'name': 'Jayson Tatum', 'position': 'F', 'number': 0},
            {'name': 'Jaylen Brown', 'position': 'G-F', 'number': 7},
            {'name': 'Kristaps Porzingis', 'position': 'F-C', 'number': 8},
        ],
        'Golden State Warriors': [
            {'name': 'Stephen Curry', 'position': 'G', 'number': 30},
            {'name': 'Klay Thompson', 'position': 'G', 'number': 11},
            {'name': 'Draymond Green', 'position': 'F', 'number': 23},
        ],
    }

    for team, players in nba_teams.items():
        agent.set_roster('NBA', team, players)

    # MLB Teams
    mlb_teams = {
        'New York Yankees': [
            {'name': 'Aaron Judge', 'position': 'OF', 'number': 99},
            {'name': 'Gerrit Cole', 'position': 'P', 'number': 45},
            {'name': 'Anthony Volpe', 'position': 'SS', 'number': 11},
        ],
        'Los Angeles Dodgers': [
            {'name': 'Mookie Betts', 'position': 'OF', 'number': 50},
            {'name': 'Freddie Freeman', 'position': '1B', 'number': 5},
            {'name': 'Clayton Kershaw', 'position': 'P', 'number': 22},
        ],
    }

    for team, players in mlb_teams.items():
        agent.set_roster('MLB', team, players)

    # NHL Teams
    nhl_teams = {
        'Vegas Golden Knights': [
            {'name': 'Jack Eichel', 'position': 'C', 'number': 9},
            {'name': 'Mark Stone', 'position': 'RW', 'number': 61},
            {'name': 'Adin Hill', 'position': 'G', 'number': 33},
        ],
        'Toronto Maple Leafs': [
            {'name': 'Auston Matthews', 'position': 'C', 'number': 34},
            {'name': 'Mitch Marner', 'position': 'RW', 'number': 16},
            {'name': 'William Nylander', 'position': 'RW', 'number': 88},
        ],
    }

    for team, players in nhl_teams.items():
        agent.set_roster('NHL', team, players)

    # Premier League Teams
    epl_teams = {
        'Manchester City': [
            {'name': 'Erling Haaland', 'position': 'FW', 'number': 9},
            {'name': 'Kevin De Bruyne', 'position': 'MF', 'number': 17},
            {'name': 'Ederson', 'position': 'GK', 'number': 31},
        ],
        'Arsenal': [
            {'name': 'Bukayo Saka', 'position': 'FW', 'number': 7},
            {'name': 'Martin Odegaard', 'position': 'MF', 'number': 8},
            {'name': 'Gabriel Jesus', 'position': 'FW', 'number': 9},
        ],
    }

    for team, players in epl_teams.items():
        agent.set_roster('EPL', team, players)

    # La Liga Teams
    laliga_teams = {
        'Real Madrid': [
            {'name': 'Vinicius Junior', 'position': 'FW', 'number': 7},
            {'name': 'Jude Bellingham', 'position': 'MF', 'number': 5},
            {'name': 'Thibaut Courtois', 'position': 'GK', 'number': 1},
        ],
        'Barcelona': [
            {'name': 'Robert Lewandowski', 'position': 'FW', 'number': 9},
            {'name': 'Gavi', 'position': 'MF', 'number': 6},
            {'name': 'Pedri', 'position': 'MF', 'number': 8},
        ],
    }

    for team, players in laliga_teams.items():
        agent.set_roster('LaLiga', team, players)

    print("✅ Sample data populated successfully!")
    print(f"✅ NFL: {len(nfl_teams)} teams")
    print(f"✅ NBA: {len(nba_teams)} teams")
    print(f"✅ MLB: {len(mlb_teams)} teams")
    print(f"✅ NHL: {len(nhl_teams)} teams")
    print(f"✅ EPL: {len(epl_teams)} teams")
    print(f"✅ La Liga: {len(laliga_teams)} teams")
    print("\n🎉 Sports Agent is ready for Loly!")


if __name__ == '__main__':
    populate_sample_data()
