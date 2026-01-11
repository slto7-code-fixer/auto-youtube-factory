from agents.trend_agent import get_trends
from agents.script_agent import generate_script
from agents.video_agent import create_video
from agents.halal_guard import halal_check
from utils.logger import log

def run_pipeline():
    log("🚀 Pipeline started")

    trend = get_trends()
    script = generate_script(trend)

    if not halal_check(script):
        log("❌ Content rejected by halal guard")
        return

    video = create_video(script)
    log("✅ Video created successfully")

if __name__ == "__main__":
    run_pipeline()
