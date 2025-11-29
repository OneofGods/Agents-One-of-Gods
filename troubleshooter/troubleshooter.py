"""
Troubleshooting & Strategy Agent - Senior Developer Grade
The brain that keeps all agents healthy, optimized, and secure
"""

import json
import os
import sys
import traceback
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
import importlib
import inspect


class Troubleshooter:
    """
    Enterprise-grade Troubleshooting & Strategy Agent

    This agent:
    - Monitors all other agents for health and performance
    - Diagnoses errors and provides detailed solutions
    - Analyzes code quality and security
    - Provides strategic recommendations
    - Auto-heals common issues

    THE BOSS AGENT - Critical for system reliability!
    """

    def __init__(self):
        self.data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.agents = {
            'sports': 'sports_agent',
            'crypto': 'crypto_agent',
            'stocks': 'stock_trader'
        }

        self.health_status = {}
        self.error_log = []
        self.performance_metrics = {}
        self.recommendations = []

        self._initialize_data()

    def _initialize_data(self):
        """Initialize troubleshooting data storage"""
        os.makedirs(self.data_dir, exist_ok=True)

        # Load health status
        health_file = os.path.join(self.data_dir, 'health_status.json')
        if os.path.exists(health_file):
            with open(health_file, 'r') as f:
                self.health_status = json.load(f)

        # Load error log
        error_file = os.path.join(self.data_dir, 'error_log.json')
        if os.path.exists(error_file):
            with open(error_file, 'r') as f:
                self.error_log = json.load(f)

        # Load recommendations
        rec_file = os.path.join(self.data_dir, 'recommendations.json')
        if os.path.exists(rec_file):
            with open(rec_file, 'r') as f:
                self.recommendations = json.load(f)

    # ==================== SYSTEM HEALTH MONITORING ====================

    def check_all_agents(self) -> Dict[str, Any]:
        """
        Comprehensive health check of all agents

        Returns:
            Health status report for all agents
        """
        report = {
            'timestamp': datetime.now().isoformat(),
            'overall_status': 'healthy',
            'agents': {},
            'issues': [],
            'warnings': []
        }

        for agent_name, module_name in self.agents.items():
            agent_status = self._check_agent_health(agent_name, module_name)
            report['agents'][agent_name] = agent_status

            if agent_status['status'] == 'error':
                report['overall_status'] = 'critical'
                report['issues'].append(f"{agent_name}: {agent_status.get('error', 'Unknown error')}")
            elif agent_status['status'] == 'warning':
                if report['overall_status'] == 'healthy':
                    report['overall_status'] = 'degraded'
                report['warnings'].append(f"{agent_name}: {agent_status.get('warning', 'Warning')}")

        self.health_status = report
        self._save_health_status()

        return report

    def _check_agent_health(self, agent_name: str, module_name: str) -> Dict[str, Any]:
        """Check health of a specific agent"""
        status = {
            'agent': agent_name,
            'status': 'healthy',
            'checks': {}
        }

        try:
            # Check 1: Module import
            try:
                module = importlib.import_module(module_name)
                status['checks']['import'] = 'pass'
            except Exception as e:
                status['checks']['import'] = 'fail'
                status['status'] = 'error'
                status['error'] = f"Import failed: {str(e)}"
                return status

            # Check 2: Data directory exists
            data_path = os.path.join(module_name, 'data')
            if os.path.exists(data_path):
                status['checks']['data_dir'] = 'pass'

                # Check data files
                data_files = os.listdir(data_path)
                status['checks']['data_files'] = len(data_files)

                if len(data_files) == 0:
                    status['warning'] = 'No data files found'
                    status['status'] = 'warning'
            else:
                status['checks']['data_dir'] = 'warning'
                status['warning'] = 'Data directory not found'

            # Check 3: API availability
            api_path = os.path.join(module_name, 'api', 'loly_api.py')
            if os.path.exists(api_path):
                status['checks']['api'] = 'pass'
            else:
                status['checks']['api'] = 'fail'
                status['status'] = 'warning'
                status['warning'] = 'API not found'

            # Check 4: Try to instantiate API
            try:
                api_module = importlib.import_module(f"{module_name}.api.loly_api")
                if hasattr(api_module, 'loly_api'):
                    api = api_module.loly_api
                    status['checks']['instantiation'] = 'pass'

                    # Check API methods
                    methods = [m for m in dir(api) if not m.startswith('_')]
                    status['checks']['api_methods'] = len(methods)
                else:
                    status['checks']['instantiation'] = 'fail'
                    status['warning'] = 'API instance not found'

            except Exception as e:
                status['checks']['instantiation'] = 'fail'
                status['warning'] = f"API instantiation failed: {str(e)}"
                if status['status'] == 'healthy':
                    status['status'] = 'warning'

        except Exception as e:
            status['status'] = 'error'
            status['error'] = f"Health check failed: {str(e)}"

        return status

    # ==================== ERROR DIAGNOSIS ====================

    def diagnose_error(self, error: Exception, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Diagnose an error and provide detailed analysis

        Args:
            error: The exception to analyze
            context: Additional context about where error occurred

        Returns:
            Detailed diagnosis with solutions
        """
        diagnosis = {
            'timestamp': datetime.now().isoformat(),
            'error_type': type(error).__name__,
            'error_message': str(error),
            'context': context or {},
            'stack_trace': traceback.format_exc(),
            'severity': self._assess_severity(error),
            'solutions': [],
            'prevention': []
        }

        # Analyze error type and provide specific solutions
        error_type = type(error).__name__

        if error_type == 'ImportError' or error_type == 'ModuleNotFoundError':
            diagnosis['solutions'] = [
                "Check that the module is installed: pip install <module>",
                "Verify the module path is correct",
                "Check for circular imports",
                "Ensure __init__.py files exist in package directories"
            ]
            diagnosis['prevention'] = [
                "Use virtual environments to manage dependencies",
                "Keep requirements.txt updated",
                "Run import tests in CI/CD pipeline"
            ]

        elif error_type == 'KeyError':
            diagnosis['solutions'] = [
                f"Key '{str(error)}' not found in dictionary",
                "Use .get() method with default value instead of direct access",
                "Validate dictionary keys before access",
                "Check if data structure matches expected format"
            ]
            diagnosis['prevention'] = [
                "Use type hints and validation",
                "Implement schema validation for data",
                "Add defensive checks for optional keys"
            ]

        elif error_type == 'FileNotFoundError':
            diagnosis['solutions'] = [
                "Verify file path is correct",
                "Check if file exists before opening",
                "Use absolute paths instead of relative",
                "Ensure data directories are created"
            ]
            diagnosis['prevention'] = [
                "Use os.path.exists() before file operations",
                "Create directories with os.makedirs(exist_ok=True)",
                "Handle file operations in try-except blocks"
            ]

        elif error_type == 'TypeError':
            diagnosis['solutions'] = [
                "Check function arguments match expected types",
                "Verify None values are handled",
                "Ensure proper type conversions",
                "Check operator compatibility with operands"
            ]
            diagnosis['prevention'] = [
                "Use type hints throughout codebase",
                "Add input validation",
                "Use mypy or similar type checker",
                "Write unit tests for type edge cases"
            ]

        else:
            diagnosis['solutions'] = [
                "Review stack trace for root cause",
                "Add detailed logging around error point",
                "Check input data validity",
                "Review recent code changes"
            ]

        # Log the error
        self.error_log.append(diagnosis)
        self._save_error_log()

        return diagnosis

    def _assess_severity(self, error: Exception) -> str:
        """Assess error severity"""
        critical_errors = ['SystemExit', 'KeyboardInterrupt', 'MemoryError']
        high_errors = ['AttributeError', 'ImportError', 'ModuleNotFoundError']
        medium_errors = ['ValueError', 'TypeError', 'KeyError']

        error_type = type(error).__name__

        if error_type in critical_errors:
            return 'critical'
        elif error_type in high_errors:
            return 'high'
        elif error_type in medium_errors:
            return 'medium'
        else:
            return 'low'

    # ==================== CODE ANALYSIS ====================

    def analyze_code_quality(self, file_path: str) -> Dict[str, Any]:
        """
        Analyze code quality of a file

        Args:
            file_path: Path to Python file to analyze

        Returns:
            Code quality report
        """
        report = {
            'file': file_path,
            'timestamp': datetime.now().isoformat(),
            'issues': [],
            'warnings': [],
            'suggestions': [],
            'metrics': {}
        }

        if not os.path.exists(file_path):
            report['issues'].append(f"File not found: {file_path}")
            return report

        try:
            with open(file_path, 'r') as f:
                code = f.read()
                lines = code.split('\n')

            # Metric 1: Lines of code
            report['metrics']['total_lines'] = len(lines)
            report['metrics']['code_lines'] = len([l for l in lines if l.strip() and not l.strip().startswith('#')])
            report['metrics']['comment_lines'] = len([l for l in lines if l.strip().startswith('#')])

            # Metric 2: Function count
            functions = [l for l in lines if l.strip().startswith('def ')]
            report['metrics']['functions'] = len(functions)

            # Metric 3: Class count
            classes = [l for l in lines if l.strip().startswith('class ')]
            report['metrics']['classes'] = len(classes)

            # Check 1: Line length
            long_lines = [(i+1, len(l)) for i, l in enumerate(lines) if len(l) > 120]
            if long_lines:
                report['warnings'].append(f"Found {len(long_lines)} lines exceeding 120 characters")

            # Check 2: Missing docstrings
            func_no_doc = 0
            for i, line in enumerate(lines):
                if line.strip().startswith('def '):
                    # Check if next non-empty line is a docstring
                    next_lines = lines[i+1:i+4]
                    has_docstring = any('"""' in l or "'''" in l for l in next_lines)
                    if not has_docstring:
                        func_no_doc += 1

            if func_no_doc > 0:
                report['suggestions'].append(f"Add docstrings to {func_no_doc} functions")

            # Check 3: TODO comments
            todos = [(i+1, l.strip()) for i, l in enumerate(lines) if 'TODO' in l.upper()]
            if todos:
                report['suggestions'].append(f"Found {len(todos)} TODO comments to address")
                report['metrics']['todos'] = len(todos)

            # Check 4: Print statements (should use logging)
            prints = [(i+1, l.strip()) for i, l in enumerate(lines) if 'print(' in l]
            if prints:
                report['suggestions'].append(f"Replace {len(prints)} print statements with logging")

            # Check 5: Hardcoded values
            magic_numbers = 0
            for line in lines:
                if '= ' in line and not line.strip().startswith('#'):
                    # Simple heuristic for magic numbers
                    if any(f'= {i}' in line for i in range(10, 1000)):
                        magic_numbers += 1

            if magic_numbers > 5:
                report['suggestions'].append("Consider using constants instead of magic numbers")

            # Overall quality score
            score = 100
            score -= len(report['issues']) * 10
            score -= len(report['warnings']) * 5
            score -= len(report['suggestions']) * 2
            report['quality_score'] = max(0, score)

        except Exception as e:
            report['issues'].append(f"Analysis failed: {str(e)}")

        return report

    # ==================== PERFORMANCE PROFILING ====================

    def profile_agent_performance(self, agent_name: str) -> Dict[str, Any]:
        """Profile performance of an agent"""
        profile = {
            'agent': agent_name,
            'timestamp': datetime.now().isoformat(),
            'metrics': {},
            'bottlenecks': [],
            'recommendations': []
        }

        try:
            # Check data file sizes
            data_path = os.path.join(self.agents.get(agent_name, ''), 'data')
            if os.path.exists(data_path):
                data_files = os.listdir(data_path)
                total_size = sum(os.path.getsize(os.path.join(data_path, f)) for f in data_files)
                profile['metrics']['data_size_bytes'] = total_size
                profile['metrics']['data_files'] = len(data_files)

                if total_size > 10 * 1024 * 1024:  # > 10MB
                    profile['bottlenecks'].append("Large data files may slow down loading")
                    profile['recommendations'].append("Consider implementing data pagination or lazy loading")

            # Check code complexity
            main_file = os.path.join(self.agents.get(agent_name, ''), f"{self.agents.get(agent_name, '')}.py")
            if os.path.exists(main_file):
                with open(main_file, 'r') as f:
                    lines = len(f.readlines())
                    profile['metrics']['code_lines'] = lines

                    if lines > 500:
                        profile['recommendations'].append("Consider splitting into smaller modules")

        except Exception as e:
            profile['error'] = str(e)

        return profile

    # ==================== SECURITY SCANNING ====================

    def security_scan(self, file_path: str) -> Dict[str, Any]:
        """
        Scan file for common security issues

        Args:
            file_path: Path to file to scan

        Returns:
            Security scan report
        """
        report = {
            'file': file_path,
            'timestamp': datetime.now().isoformat(),
            'vulnerabilities': [],
            'warnings': [],
            'severity': 'low'
        }

        if not os.path.exists(file_path):
            report['vulnerabilities'].append(f"File not found: {file_path}")
            return report

        try:
            with open(file_path, 'r') as f:
                code = f.read()
                lines = code.split('\n')

            # Check 1: Hardcoded credentials
            dangerous_patterns = ['password =', 'api_key =', 'secret =', 'token =']
            for i, line in enumerate(lines):
                for pattern in dangerous_patterns:
                    if pattern in line.lower() and '=' in line:
                        # Check if it's actually a hardcoded value (not None or variable)
                        if not ('None' in line or 'os.environ' in line or 'input(' in line):
                            report['vulnerabilities'].append({
                                'line': i + 1,
                                'type': 'Hardcoded Credential',
                                'severity': 'high',
                                'description': f"Possible hardcoded credential on line {i+1}"
                            })
                            report['severity'] = 'high'

            # Check 2: SQL injection vulnerabilities
            if 'execute(' in code and '%s' in code:
                report['warnings'].append({
                    'type': 'SQL Injection Risk',
                    'severity': 'medium',
                    'description': 'Use parameterized queries to prevent SQL injection'
                })

            # Check 3: eval() usage
            if 'eval(' in code:
                report['vulnerabilities'].append({
                    'type': 'Dangerous eval() Usage',
                    'severity': 'critical',
                    'description': 'eval() can execute arbitrary code - avoid using it'
                })
                report['severity'] = 'critical'

            # Check 4: Pickle usage
            if 'pickle.loads(' in code:
                report['warnings'].append({
                    'type': 'Unsafe Deserialization',
                    'severity': 'high',
                    'description': 'pickle.loads() can execute arbitrary code - use JSON instead'
                })

        except Exception as e:
            report['error'] = str(e)

        return report

    # ==================== STRATEGIC RECOMMENDATIONS ====================

    def generate_recommendations(self) -> List[Dict[str, Any]]:
        """
        Generate strategic recommendations for system improvement

        Returns:
            List of recommendations
        """
        recommendations = []

        # Run health check
        health = self.check_all_agents()

        # Recommendation 1: Agent health
        for agent_name, status in health['agents'].items():
            if status['status'] != 'healthy':
                recommendations.append({
                    'priority': 'high',
                    'category': 'reliability',
                    'agent': agent_name,
                    'recommendation': f"Fix {agent_name} agent - currently {status['status']}",
                    'reason': status.get('error', status.get('warning', 'Unknown issue'))
                })

        # Recommendation 2: Testing
        recommendations.append({
            'priority': 'high',
            'category': 'quality',
            'recommendation': 'Add comprehensive unit tests for all agents',
            'reason': 'Improve reliability and catch bugs early',
            'implementation': 'Use pytest framework with minimum 80% code coverage'
        })

        # Recommendation 3: Logging
        recommendations.append({
            'priority': 'medium',
            'category': 'observability',
            'recommendation': 'Implement structured logging across all agents',
            'reason': 'Better debugging and monitoring',
            'implementation': 'Use Python logging module with JSON formatting'
        })

        # Recommendation 4: Documentation
        recommendations.append({
            'priority': 'medium',
            'category': 'maintainability',
            'recommendation': 'Add comprehensive API documentation',
            'reason': 'Easier onboarding and maintenance',
            'implementation': 'Use Sphinx or similar to generate docs from docstrings'
        })

        # Recommendation 5: Error handling
        recommendations.append({
            'priority': 'high',
            'category': 'reliability',
            'recommendation': 'Implement centralized error handling',
            'reason': 'Consistent error responses and better user experience',
            'implementation': 'Create custom exception classes and global error handlers'
        })

        self.recommendations = recommendations
        self._save_recommendations()

        return recommendations

    # ==================== DATA PERSISTENCE ====================

    def _save_health_status(self):
        """Save health status to file"""
        with open(os.path.join(self.data_dir, 'health_status.json'), 'w') as f:
            json.dump(self.health_status, f, indent=2)

    def _save_error_log(self):
        """Save error log to file"""
        with open(os.path.join(self.data_dir, 'error_log.json'), 'w') as f:
            json.dump(self.error_log[-100:], f, indent=2)  # Keep last 100 errors

    def _save_recommendations(self):
        """Save recommendations to file"""
        with open(os.path.join(self.data_dir, 'recommendations.json'), 'w') as f:
            json.dump(self.recommendations, f, indent=2)

    # ==================== REPORTING ====================

    def generate_health_report(self) -> Dict[str, Any]:
        """Generate comprehensive health report"""
        health = self.check_all_agents()

        report = {
            'timestamp': datetime.now().isoformat(),
            'system_status': health['overall_status'],
            'agents': health['agents'],
            'summary': {
                'total_agents': len(health['agents']),
                'healthy': sum(1 for a in health['agents'].values() if a['status'] == 'healthy'),
                'warnings': sum(1 for a in health['agents'].values() if a['status'] == 'warning'),
                'errors': sum(1 for a in health['agents'].values() if a['status'] == 'error')
            },
            'recent_errors': self.error_log[-10:],
            'recommendations': self.generate_recommendations()
        }

        return report


# Loly's Interface
class LolyInterface:
    """Simplified interface for Loly to call the Troubleshooter"""

    def __init__(self):
        self.agent = Troubleshooter()

    def health_check(self):
        """Quick health check"""
        return self.agent.check_all_agents()

    def diagnose(self, error: Exception, context: Dict = None):
        """Quick error diagnosis"""
        return self.agent.diagnose_error(error, context)

    def get_recommendations(self):
        """Quick recommendations"""
        return self.agent.generate_recommendations()

    def full_report(self):
        """Quick full report"""
        return self.agent.generate_health_report()
