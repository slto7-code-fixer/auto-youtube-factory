import sys
import os

# 🔹 إضافة المسارات عشان GitHub Actions يعرف الموديولات
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

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
    
    # تقييم الربحية
    if profit_score(topic) < 4:
        print("Rejected: Not profitable")
        return

    # توليد السكريبت
    script = generate_script(topic)
    
    # الفلتر الشرعي
    if not halal_check(script):
        print("Rejected: Not halal")
        return

    # Quality Gate
    ok, msg = quality_check(script)
    if not ok:
        print(f"Rejected: {msg}")
        return

    # إنشاء الفيديو
    video = create_video(script)

    # رفع على يوتيوب
    upload(video)

    # جمع الإحصائيات
    stats = get_stats()

    # حفظ في الذاكرة
    remember(topic, stats)

    # إضافة للفيديوهات القصيرة → تجميع الفيديو الطويل
    add_short(script)

    # مراجعة CEO Agent
    decision = review(stats)
    print(f"CEO Decision: {decision}")

    # إرسال تقرير على الإيميل
    send_email(decision)

if __name__ == "__main__":
    run()
