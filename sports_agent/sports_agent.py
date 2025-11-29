"""
Main Sports Agent Class
Manages rosters across all major sports leagues
"""

import json
import os
from typing import Dict, List, Optional, Any
from datetime import datetime


class SportsAgent:
    """
    Sports Agent that controls entire rosters across all major leagues.
    Loly can call this agent at will to get roster information.
    """

    def __init__(self):
        self.data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.leagues = {
            # American Sports
            'NFL': {'name': 'National Football League', 'teams': 32, 'sport': 'Football'},
            'NBA': {'name': 'National Basketball Association', 'teams': 30, 'sport': 'Basketball'},
            'MLB': {'name': 'Major League Baseball', 'teams': 30, 'sport': 'Baseball'},
            'NHL': {'name': 'National Hockey League', 'teams': 32, 'sport': 'Hockey'},
            'MLS': {'name': 'Major League Soccer', 'teams': 29, 'sport': 'Soccer'},

            # International Soccer
            'EPL': {'name': 'English Premier League', 'teams': 20, 'sport': 'Soccer'},
            'LaLiga': {'name': 'La Liga', 'teams': 20, 'sport': 'Soccer'},
            'Bundesliga': {'name': 'Bundesliga', 'teams': 18, 'sport': 'Soccer'},
            'SerieA': {'name': 'Serie A', 'teams': 20, 'sport': 'Soccer'},
            'Ligue1': {'name': 'Ligue 1', 'teams': 18, 'sport': 'Soccer'},

            # College Sports
            'NCAA_FB': {'name': 'NCAA Football', 'teams': 130, 'sport': 'Football'},
            'NCAA_BB': {'name': 'NCAA Basketball', 'teams': 350, 'sport': 'Basketball'},
        }

        self.rosters = {}
        self._initialize_data()

    def _initialize_data(self):
        """Initialize or load existing roster data"""
        os.makedirs(self.data_dir, exist_ok=True)

        for league_code in self.leagues:
            roster_file = os.path.join(self.data_dir, f'{league_code}_rosters.json')
            if os.path.exists(roster_file):
                with open(roster_file, 'r') as f:
                    self.rosters[league_code] = json.load(f)
            else:
                self.rosters[league_code] = {}

    def get_all_leagues(self) -> Dict[str, Dict[str, Any]]:
        """Get information about all supported leagues"""
        return self.leagues

    def get_league_info(self, league_code: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific league"""
        return self.leagues.get(league_code.upper())

    def get_roster(self, league_code: str, team_name: str) -> Optional[Dict[str, Any]]:
        """
        Get roster for a specific team in a league

        Args:
            league_code: The league code (e.g., 'NFL', 'NBA')
            team_name: The team name

        Returns:
            Roster data or None if not found
        """
        league_code = league_code.upper()
        if league_code not in self.rosters:
            return None

        return self.rosters[league_code].get(team_name)

    def set_roster(self, league_code: str, team_name: str, roster_data: Dict[str, Any]) -> bool:
        """
        Set/update roster for a specific team

        Args:
            league_code: The league code (e.g., 'NFL', 'NBA')
            team_name: The team name
            roster_data: The roster data to set

        Returns:
            True if successful, False otherwise
        """
        league_code = league_code.upper()
        if league_code not in self.leagues:
            return False

        if league_code not in self.rosters:
            self.rosters[league_code] = {}

        self.rosters[league_code][team_name] = {
            'team_name': team_name,
            'league': league_code,
            'roster': roster_data,
            'last_updated': datetime.now().isoformat()
        }

        self._save_league_data(league_code)
        return True

    def add_player(self, league_code: str, team_name: str, player_data: Dict[str, Any]) -> bool:
        """
        Add a player to a team's roster

        Args:
            league_code: The league code
            team_name: The team name
            player_data: Player information (name, position, number, etc.)

        Returns:
            True if successful, False otherwise
        """
        league_code = league_code.upper()
        roster = self.get_roster(league_code, team_name)

        if roster is None:
            # Create new roster
            roster = {'team_name': team_name, 'league': league_code, 'roster': []}
            self.rosters[league_code][team_name] = roster

        roster['roster'].append(player_data)
        roster['last_updated'] = datetime.now().isoformat()

        self._save_league_data(league_code)
        return True

    def remove_player(self, league_code: str, team_name: str, player_name: str) -> bool:
        """
        Remove a player from a team's roster

        Args:
            league_code: The league code
            team_name: The team name
            player_name: Name of player to remove

        Returns:
            True if successful, False otherwise
        """
        league_code = league_code.upper()
        roster = self.get_roster(league_code, team_name)

        if roster is None:
            return False

        original_count = len(roster['roster'])
        roster['roster'] = [p for p in roster['roster'] if p.get('name') != player_name]

        if len(roster['roster']) < original_count:
            roster['last_updated'] = datetime.now().isoformat()
            self._save_league_data(league_code)
            return True

        return False

    def get_all_teams(self, league_code: str) -> List[str]:
        """Get all teams in a league"""
        league_code = league_code.upper()
        if league_code not in self.rosters:
            return []
        return list(self.rosters[league_code].keys())

    def search_player(self, player_name: str, league_code: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Search for a player across leagues

        Args:
            player_name: Name to search for
            league_code: Optional league to search in (searches all if None)

        Returns:
            List of matches with team and league info
        """
        results = []
        leagues_to_search = [league_code.upper()] if league_code else self.rosters.keys()

        for league in leagues_to_search:
            if league not in self.rosters:
                continue

            for team_name, team_data in self.rosters[league].items():
                for player in team_data.get('roster', []):
                    if player_name.lower() in player.get('name', '').lower():
                        results.append({
                            'player': player,
                            'team': team_name,
                            'league': league
                        })

        return results

    def get_league_summary(self, league_code: str) -> Dict[str, Any]:
        """Get summary statistics for a league"""
        league_code = league_code.upper()
        if league_code not in self.rosters:
            return {}

        total_teams = len(self.rosters[league_code])
        total_players = sum(
            len(team.get('roster', []))
            for team in self.rosters[league_code].values()
        )

        return {
            'league': league_code,
            'league_name': self.leagues[league_code]['name'],
            'total_teams': total_teams,
            'total_players': total_players,
            'teams': list(self.rosters[league_code].keys())
        }

    def _save_league_data(self, league_code: str):
        """Save league data to file"""
        roster_file = os.path.join(self.data_dir, f'{league_code}_rosters.json')
        with open(roster_file, 'w') as f:
            json.dump(self.rosters[league_code], f, indent=2)

    def export_all_data(self, output_file: str):
        """Export all roster data to a single file"""
        with open(output_file, 'w') as f:
            json.dump(self.rosters, f, indent=2)

    def import_data(self, input_file: str):
        """Import roster data from a file"""
        with open(input_file, 'r') as f:
            data = json.load(f)
            self.rosters.update(data)

            # Save to individual league files
            for league_code in data.keys():
                self._save_league_data(league_code)


# Loly's Interface - Simple functions for quick access
class LolyInterface:
    """Simplified interface for Loly to call the Sports Agent"""

    def __init__(self):
        self.agent = SportsAgent()

    def get_roster(self, league: str, team: str):
        """Quick roster lookup"""
        return self.agent.get_roster(league, team)

    def find_player(self, player_name: str, league: Optional[str] = None):
        """Quick player search"""
        return self.agent.search_player(player_name, league)

    def league_summary(self, league: str):
        """Quick league summary"""
        return self.agent.get_league_summary(league)

    def all_leagues(self):
        """Get all available leagues"""
        return self.agent.get_all_leagues()
