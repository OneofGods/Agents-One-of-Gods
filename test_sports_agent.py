"""
Quick test script to verify Sports Agent functionality
"""

from sports_agent.api import loly_api


def test_sports_agent():
    """Run quick tests"""
    print("\n🧪 Testing Sports Agent...\n")

    # Test 1: Hello
    print("✓ Test 1: Greeting")
    response = loly_api.hello()
    assert "Sports Agent" in response
    print(f"  {response}")

    # Test 2: List leagues
    print("\n✓ Test 2: List leagues")
    leagues = loly_api.list_leagues()
    assert len(leagues) == 12
    print(f"  Found {len(leagues)} leagues")

    # Test 3: Get stats
    print("\n✓ Test 3: Quick stats")
    stats = loly_api.quick_stats()
    assert 'total_leagues' in stats
    print(f"  Total leagues: {stats['total_leagues']}")

    # Test 4: Add a team
    print("\n✓ Test 4: Add a team")
    result = loly_api.add_team('NBA', 'Test Team', [
        {'name': 'Test Player', 'position': 'G', 'number': 99}
    ])
    assert result['success'] == True
    print(f"  {result['message']}")

    # Test 5: Get team roster
    print("\n✓ Test 5: Get team roster")
    roster = loly_api.get_team_roster('NBA', 'Test Team')
    assert roster is not None
    assert roster['team_name'] == 'Test Team'
    print(f"  Team: {roster['team_name']}, Players: {len(roster['roster'])}")

    # Test 6: Add player
    print("\n✓ Test 6: Add player to team")
    result = loly_api.add_player_to_team('NBA', 'Test Team', {
        'name': 'Another Player',
        'position': 'F',
        'number': 88
    })
    assert result['success'] == True
    print(f"  {result['message']}")

    # Test 7: Find player
    print("\n✓ Test 7: Find player")
    results = loly_api.find_player('Test Player')
    assert len(results) > 0
    print(f"  Found {len(results)} result(s)")

    # Test 8: Get all teams
    print("\n✓ Test 8: Get all NBA teams")
    teams = loly_api.get_all_teams_in_league('NBA')
    assert 'Test Team' in teams
    print(f"  Total NBA teams: {len(teams)}")

    # Test 9: Remove player
    print("\n✓ Test 9: Remove player")
    result = loly_api.remove_player_from_team('NBA', 'Test Team', 'Test Player')
    assert result['success'] == True
    print(f"  {result['message']}")

    # Test 10: League info
    print("\n✓ Test 10: Get league info")
    info = loly_api.get_league_info('NBA')
    assert info['league'] == 'NBA'
    print(f"  League: {info['league_name']}, Teams: {info['total_teams']}")

    print("\n" + "=" * 60)
    print("  ✅ ALL TESTS PASSED! Sports Agent is fully operational!")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    test_sports_agent()
