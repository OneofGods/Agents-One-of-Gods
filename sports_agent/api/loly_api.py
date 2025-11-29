"""
API Interface for Loly to interact with the Sports Agent
Simple, clean functions that Loly can call at will
"""

from ..sports_agent import SportsAgent, LolyInterface
from typing import Dict, List, Optional, Any
import json


class LolyAPI:
    """
    Loly's dedicated API to the Sports Agent
    All roster control at your fingertips!
    """

    def __init__(self):
        self.interface = LolyInterface()
        self.agent = self.interface.agent

    def hello(self) -> str:
        """Greeting from Sports Agent"""
        return "Sports Agent ready! I control all the rosters. What do you need, Loly?"

    def list_leagues(self) -> Dict[str, Dict[str, Any]]:
        """
        Get all available leagues

        Returns:
            Dictionary of all leagues with their info
        """
        return self.interface.all_leagues()

    def get_team_roster(self, league: str, team: str) -> Optional[Dict[str, Any]]:
        """
        Get a team's complete roster

        Args:
            league: League code (e.g., 'NFL', 'NBA')
            team: Team name

        Returns:
            Team roster data or None
        """
        return self.interface.get_roster(league, team)

    def find_player(self, player_name: str, league: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Find a player across all leagues or in a specific league

        Args:
            player_name: Player name to search for
            league: Optional league to search in

        Returns:
            List of matching players with team and league info
        """
        return self.interface.find_player(player_name, league)

    def add_team(self, league: str, team_name: str, players: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Add a new team with its roster

        Args:
            league: League code
            team_name: Name of the team
            players: List of player dictionaries

        Returns:
            Status message
        """
        success = self.agent.set_roster(league, team_name, players)
        return {
            'success': success,
            'message': f"Team {team_name} added to {league}" if success else "Failed to add team",
            'league': league,
            'team': team_name
        }

    def add_player_to_team(self, league: str, team: str, player: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add a player to an existing team

        Args:
            league: League code
            team: Team name
            player: Player data (name, position, number, etc.)

        Returns:
            Status message
        """
        success = self.agent.add_player(league, team, player)
        return {
            'success': success,
            'message': f"Player {player.get('name')} added to {team}" if success else "Failed to add player",
            'league': league,
            'team': team,
            'player': player.get('name')
        }

    def remove_player_from_team(self, league: str, team: str, player_name: str) -> Dict[str, Any]:
        """
        Remove a player from a team

        Args:
            league: League code
            team: Team name
            player_name: Name of player to remove

        Returns:
            Status message
        """
        success = self.agent.remove_player(league, team, player_name)
        return {
            'success': success,
            'message': f"Player {player_name} removed from {team}" if success else "Player not found",
            'league': league,
            'team': team,
            'player': player_name
        }

    def get_league_info(self, league: str) -> Dict[str, Any]:
        """
        Get detailed information about a league

        Args:
            league: League code

        Returns:
            League summary and statistics
        """
        return self.interface.league_summary(league)

    def get_all_teams_in_league(self, league: str) -> List[str]:
        """
        Get all teams in a specific league

        Args:
            league: League code

        Returns:
            List of team names
        """
        return self.agent.get_all_teams(league)

    def quick_stats(self) -> Dict[str, Any]:
        """
        Get quick stats across all leagues

        Returns:
            Overall statistics
        """
        stats = {
            'total_leagues': len(self.agent.leagues),
            'leagues': {}
        }

        for league_code in self.agent.leagues.keys():
            league_summary = self.interface.league_summary(league_code)
            if league_summary:
                stats['leagues'][league_code] = league_summary

        return stats

    def export_everything(self, filename: str = 'all_rosters.json') -> Dict[str, Any]:
        """
        Export all roster data

        Args:
            filename: Output filename

        Returns:
            Status message
        """
        try:
            self.agent.export_all_data(filename)
            return {
                'success': True,
                'message': f'All data exported to {filename}',
                'file': filename
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'Export failed: {str(e)}'
            }


# Quick access instance for Loly
loly_api = LolyAPI()
