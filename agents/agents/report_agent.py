from agents.analytics_agent import collect_stats
from utils.emailer import send_email

def generate_report():
    stats = collect_stats()

    report = f"""
📊 Weekly Automation Report

Videos Created: {stats['videos_created']}
System Status: {stats['status']}
Errors: {stats['errors']}

Recommendation:
{stats['recommendation']}
"""
    send_email(report)
