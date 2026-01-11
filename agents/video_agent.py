from moviepy.editor import ImageClip
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

def create_video(script):
    os.makedirs("assets/videos", exist_ok=True)

    # إنشاء صورة
    img = Image.new("RGB", (1080, 1920), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 48)
    except:
        font = ImageFont.load_default()

    text = script.strip()
    draw.multiline_text(
        (540, 960),
        text,
        fill=(255, 255, 255),
        font=font,
        anchor="mm",
        align="center"
    )

    image_path = "assets/videos/frame.png"
    img.save(image_path)

    clip = ImageClip(image_path).set_duration(15)

    filename = f"assets/videos/video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    clip.write_videofile(filename, fps=24, audio=False)

    return filename
