"""
API Interface for Loly to interact with Troubleshooter
The brain that keeps everything running smooth!
"""

from ..troubleshooter import Troubleshooter, LolyInterface
from typing import Dict, List, Optional, Any
from datetime import datetime
import os


class LolyAPI:
    """
    Loly's dedicated API to the Troubleshooter
    The BOSS agent - keeps system healthy and optimized!
    """

    def __init__(self):
        self.interface = LolyInterface()
        self.agent = self.interface.agent

    def hello(self) -> str:
        """Greeting from Troubleshooter"""
        return "Troubleshooter ready! I'm the brain - monitoring, diagnosing, and optimizing all agents. What do you need, Loly?"

    def health_check(self) -> Dict[str, Any]:
        """
        Run complete health check on all agents

        Returns:
            Comprehensive health status report
        """
        return self.interface.health_check()

    def quick_status(self) -> str:
        """
        Get quick status summary

        Returns:
            Simple status string
        """
        health = self.health_check()
        status = health['overall_status']

        if status == 'healthy':
            return "✅ All systems operational!"
        elif status == 'degraded':
            return "⚠️ Some systems have warnings"
        else:
            return "🚨 Critical issues detected!"

    def diagnose_error(self, error: Exception, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Diagnose an error and get detailed solutions

        Args:
            error: The exception to analyze
            context: Additional context

        Returns:
            Detailed diagnosis with solutions
        """
        return self.interface.diagnose(error, context)

    def analyze_code(self, file_path: str) -> Dict[str, Any]:
        """
        Analyze code quality of a file

        Args:
            file_path: Path to Python file

        Returns:
            Code quality report
        """
        return self.agent.analyze_code_quality(file_path)

    def security_scan(self, file_path: str) -> Dict[str, Any]:
        """
        Scan file for security vulnerabilities

        Args:
            file_path: Path to file

        Returns:
            Security scan report
        """
        return self.agent.security_scan(file_path)

    def profile_performance(self, agent_name: str) -> Dict[str, Any]:
        """
        Profile performance of an agent

        Args:
            agent_name: Name of agent (sports, crypto, stocks)

        Returns:
            Performance profile
        """
        return self.agent.profile_agent_performance(agent_name)

    def get_recommendations(self) -> List[Dict[str, Any]]:
        """
        Get strategic recommendations for system improvement

        Returns:
            List of recommendations
        """
        return self.interface.get_recommendations()

    def full_report(self) -> Dict[str, Any]:
        """
        Generate comprehensive system health report

        Returns:
            Complete health report with all diagnostics
        """
        return self.interface.full_report()

    def check_agent(self, agent_name: str) -> Dict[str, Any]:
        """
        Check health of a specific agent

        Args:
            agent_name: Name of agent (sports, crypto, stocks)

        Returns:
            Agent health status
        """
        health = self.health_check()
        return health['agents'].get(agent_name, {'error': 'Agent not found'})

    def get_error_log(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get recent error log

        Args:
            limit: Number of recent errors to return

        Returns:
            List of recent errors
        """
        return self.agent.error_log[-limit:]

    def scan_all_agents(self) -> Dict[str, Any]:
        """
        Run complete scan of all agents

        Returns:
            Complete scan results
        """
        results = {
            'timestamp': datetime.now().isoformat(),
            'health': self.health_check(),
            'security': {},
            'performance': {},
            'code_quality': {}
        }

        # Security scan for each agent
        for agent_name, module_name in self.agent.agents.items():
            main_file = f"{module_name}/{module_name}.py"
            if os.path.exists(main_file):
                results['security'][agent_name] = self.security_scan(main_file)
                results['code_quality'][agent_name] = self.analyze_code(main_file)

            results['performance'][agent_name] = self.profile_performance(agent_name)

        return results


# Quick access instance for Loly
loly_api = LolyAPI()
