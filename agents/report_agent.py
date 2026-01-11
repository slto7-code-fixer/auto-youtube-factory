from agents.analytics_agent import collect_stats
from utils.emailer import send_email

def generate_report():
    stats = collect_stats()
    report = f"Videos: {stats['videos']}\nStatus: {stats['status']}"
    send_email(report)
