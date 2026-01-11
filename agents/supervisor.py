from agents.trend_agent import get_trend
from agents.profit_agent import profit_score
from agents.script_agent import generate_script
from agents.halal_guard import halal_check
from agents.quality_gate import quality_check
from agents.video_agent import create_video
from agents.upload_agent import upload
from agents.analytics_agent import get_stats
from agents.memory_agent import remember
from agents.recycle_agent import add_short
from agents.ceo_agent import review
from utils.emailer import send_email

def run():
    topic = get_trend()
    if profit_score(topic) < 4:
        return

    script = generate_script(topic)
    if not halal_check(script):
        return

    ok, _ = quality_check(script)
    if not ok:
        return

    video = create_video(script)
    upload(video)

    stats = get_stats()
    remember(topic, stats)
    add_short(script)

    decision = review(stats)
    send_email(decision)

run()
