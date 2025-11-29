"""
Troubleshooter Demo - THE BOSS AGENT
Shows how Loly uses the brain to keep all agents healthy!
"""

from troubleshooter.api import loly_api
import json


def print_section(title):
    """Print a fancy section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def demo_troubleshooter():
    """Demonstrate Troubleshooter capabilities"""

    print("\n🧠 TROUBLESHOOTER - THE BRAIN OF THE SYSTEM 🧠")
    print("Monitoring, Diagnosing, and Optimizing All Agents\n")

    # 1. Greeting
    print_section("1. Loly says hello to Troubleshooter")
    greeting = loly_api.hello()
    print(f"Troubleshooter: {greeting}")

    # 2. Quick status check
    print_section("2. Loly asks: What's the quick status?")
    status = loly_api.quick_status()
    print(f"\n  {status}")

    # 3. Full health check
    print_section("3. Loly runs: Complete health check")
    health = loly_api.health_check()
    print(f"\n  Overall Status: {health['overall_status'].upper()}")
    print(f"  Timestamp: {health['timestamp']}")

    print("\n  Agent Status:")
    for agent_name, agent_status in health['agents'].items():
        status_emoji = "✅" if agent_status['status'] == 'healthy' else "⚠️" if agent_status['status'] == 'warning' else "🚨"
        print(f"\n  {status_emoji} {agent_name.upper()}:")
        print(f"    Status: {agent_status['status']}")
        print(f"    Checks: {agent_status.get('checks', {})}")
        if 'warning' in agent_status:
            print(f"    Warning: {agent_status['warning']}")
        if 'error' in agent_status:
            print(f"    Error: {agent_status['error']}")

    # 4. Check specific agent
    print_section("4. Loly checks: Sports Agent health")
    sports_health = loly_api.check_agent('sports')
    print(json.dumps(sports_health, indent=2))

    # 5. Error diagnosis
    print_section("5. Loly tests: Error diagnosis")
    try:
        # Simulate an error
        test_dict = {'key1': 'value1'}
        _ = test_dict['non_existent_key']
    except Exception as e:
        diagnosis = loly_api.diagnose_error(e, {'agent': 'test', 'operation': 'dict_access'})
        print(f"\n  Error Type: {diagnosis['error_type']}")
        print(f"  Severity: {diagnosis['severity']}")
        print(f"\n  Solutions:")
        for i, solution in enumerate(diagnosis['solutions'], 1):
            print(f"    {i}. {solution}")
        print(f"\n  Prevention:")
        for i, prevention in enumerate(diagnosis['prevention'], 1):
            print(f"    {i}. {prevention}")

    # 6. Code quality analysis
    print_section("6. Loly analyzes: Sports Agent code quality")
    code_analysis = loly_api.analyze_code('sports_agent/sports_agent.py')
    print(f"\n  File: {code_analysis['file']}")
    print(f"  Quality Score: {code_analysis.get('quality_score', 'N/A')}/100")
    print(f"\n  Metrics:")
    for metric, value in code_analysis.get('metrics', {}).items():
        print(f"    {metric}: {value}")

    if code_analysis.get('issues'):
        print(f"\n  Issues:")
        for issue in code_analysis['issues']:
            print(f"    - {issue}")

    if code_analysis.get('warnings'):
        print(f"\n  Warnings:")
        for warning in code_analysis['warnings']:
            print(f"    - {warning}")

    if code_analysis.get('suggestions'):
        print(f"\n  Suggestions:")
        for suggestion in code_analysis['suggestions'][:5]:  # Show first 5
            print(f"    - {suggestion}")

    # 7. Security scan
    print_section("7. Loly runs: Security scan on Drift Agent")
    security = loly_api.security_scan('crypto_agent/drift_agent.py')
    print(f"\n  File: {security['file']}")
    print(f"  Overall Severity: {security['severity'].upper()}")

    if security.get('vulnerabilities'):
        print(f"\n  🚨 Vulnerabilities Found: {len(security['vulnerabilities'])}")
        for vuln in security['vulnerabilities']:
            print(f"    - {vuln}")
    else:
        print(f"\n  ✅ No vulnerabilities found!")

    if security.get('warnings'):
        print(f"\n  ⚠️ Warnings: {len(security['warnings'])}")
        for warning in security['warnings'][:3]:
            print(f"    - {warning.get('description', warning)}")

    # 8. Performance profiling
    print_section("8. Loly profiles: Stock Trader performance")
    performance = loly_api.profile_performance('stocks')
    print(f"\n  Agent: {performance['agent']}")
    print(f"\n  Metrics:")
    for metric, value in performance.get('metrics', {}).items():
        print(f"    {metric}: {value}")

    if performance.get('bottlenecks'):
        print(f"\n  Bottlenecks:")
        for bottleneck in performance['bottlenecks']:
            print(f"    - {bottleneck}")

    if performance.get('recommendations'):
        print(f"\n  Recommendations:")
        for rec in performance['recommendations']:
            print(f"    - {rec}")

    # 9. Strategic recommendations
    print_section("9. Loly asks: What are your strategic recommendations?")
    recommendations = loly_api.get_recommendations()
    print(f"\n  Total Recommendations: {len(recommendations)}")

    # Group by priority
    high = [r for r in recommendations if r.get('priority') == 'high']
    medium = [r for r in recommendations if r.get('priority') == 'medium']

    if high:
        print(f"\n  🚨 HIGH PRIORITY ({len(high)}):")
        for rec in high[:3]:  # Show first 3
            print(f"\n    {rec.get('recommendation')}")
            print(f"    Reason: {rec.get('reason')}")
            if 'implementation' in rec:
                print(f"    How: {rec.get('implementation')}")

    if medium:
        print(f"\n  ⚠️ MEDIUM PRIORITY ({len(medium)}):")
        for rec in medium[:2]:  # Show first 2
            print(f"\n    {rec.get('recommendation')}")
            print(f"    Reason: {rec.get('reason')}")

    # 10. Full system report
    print_section("10. Loly generates: Complete system health report")
    report = loly_api.full_report()
    print(f"\n  System Status: {report['system_status'].upper()}")
    print(f"\n  Summary:")
    print(f"    Total Agents: {report['summary']['total_agents']}")
    print(f"    Healthy: {report['summary']['healthy']}")
    print(f"    Warnings: {report['summary']['warnings']}")
    print(f"    Errors: {report['summary']['errors']}")

    print(f"\n  Top Recommendations:")
    for i, rec in enumerate(report['recommendations'][:3], 1):
        print(f"    {i}. [{rec.get('priority', 'N/A').upper()}] {rec.get('recommendation')}")

    # 11. Error log
    print_section("11. Loly reviews: Recent error log")
    errors = loly_api.get_error_log(limit=3)
    if errors:
        print(f"\n  Recent Errors: {len(errors)}")
        for error in errors:
            print(f"\n    Error: {error.get('error_type')}")
            print(f"    Severity: {error.get('severity')}")
            print(f"    Time: {error.get('timestamp')}")
    else:
        print(f"\n  ✅ No recent errors!")

    print("\n" + "=" * 70)
    print("  ✅ TROUBLESHOOTER DEMO COMPLETE!")
    print("  🧠 THE BRAIN IS OPERATIONAL - KEEPING LOLY HEALTHY!")
    print("=" * 70 + "\n")


if __name__ == '__main__':
    demo_troubleshooter()
