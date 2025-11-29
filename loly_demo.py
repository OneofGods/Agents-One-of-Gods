"""
Demo script showing how Loly can interact with the Sports Agent
Run this to see all the capabilities!
"""

from sports_agent.api import loly_api
import json


def print_section(title):
    """Print a fancy section header"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def demo_loly_interactions():
    """Demonstrate Loly calling the Sports Agent"""

    print("\n🏆 SPORTS AGENT - LOLY DEMO 🏆\n")

    # 1. Greeting
    print_section("1. Loly says hello to Sports Agent")
    greeting = loly_api.hello()
    print(f"Sports Agent: {greeting}")

    # 2. List all leagues
    print_section("2. Loly asks: What leagues do you control?")
    leagues = loly_api.list_leagues()
    print(f"Total Leagues: {len(leagues)}")
    for code, info in leagues.items():
        print(f"  • {code}: {info['name']} ({info['teams']} teams)")

    # 3. Get quick stats
    print_section("3. Loly asks: Give me quick stats")
    stats = loly_api.quick_stats()
    print(json.dumps(stats, indent=2))

    # 4. Get specific team roster
    print_section("4. Loly asks: Show me the Lakers roster")
    lakers = loly_api.get_team_roster('NBA', 'Los Angeles Lakers')
    if lakers:
        print(f"Team: {lakers['team_name']}")
        print(f"League: {lakers['league']}")
        print("\nPlayers:")
        for player in lakers['roster']:
            print(f"  #{player['number']} {player['name']} - {player['position']}")

    # 5. Find a player
    print_section("5. Loly asks: Where is LeBron James?")
    results = loly_api.find_player('LeBron')
    for result in results:
        print(f"Found: {result['player']['name']}")
        print(f"  Team: {result['team']}")
        print(f"  League: {result['league']}")
        print(f"  Position: {result['player']['position']}")
        print(f"  Number: {result['player']['number']}")

    # 6. Add a new player
    print_section("6. Loly adds a new player")
    new_player = {
        'name': 'Austin Reaves',
        'position': 'G',
        'number': 15
    }
    result = loly_api.add_player_to_team('NBA', 'Los Angeles Lakers', new_player)
    print(json.dumps(result, indent=2))

    # 7. Get league information
    print_section("7. Loly asks: Tell me about the NFL")
    nfl_info = loly_api.get_league_info('NFL')
    print(json.dumps(nfl_info, indent=2))

    # 8. Get all teams in a league
    print_section("8. Loly asks: What NBA teams do we have?")
    nba_teams = loly_api.get_all_teams_in_league('NBA')
    print(f"NBA Teams ({len(nba_teams)}):")
    for team in nba_teams:
        print(f"  • {team}")

    # 9. Add a new team
    print_section("9. Loly adds a new team")
    new_team_roster = [
        {'name': 'Nikola Jokic', 'position': 'C', 'number': 15},
        {'name': 'Jamal Murray', 'position': 'G', 'number': 27},
        {'name': 'Michael Porter Jr.', 'position': 'F', 'number': 1},
    ]
    result = loly_api.add_team('NBA', 'Denver Nuggets', new_team_roster)
    print(json.dumps(result, indent=2))

    # 10. Search across all leagues
    print_section("10. Loly searches for 'James' across all leagues")
    results = loly_api.find_player('James')
    print(f"Found {len(results)} results:")
    for result in results:
        print(f"  • {result['player']['name']} - {result['team']} ({result['league']})")

    print("\n" + "=" * 60)
    print("  ✅ DEMO COMPLETE! Sports Agent is ready for Loly!")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    # First populate sample data
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

    print("Setting up sample data...")
    from sports_agent.sample_data import populate_sample_data
    populate_sample_data()

    # Then run the demo
    demo_loly_interactions()
