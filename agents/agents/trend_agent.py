import random

HALAL_TOPICS = [
    "Amazing facts about the human body",
    "Mind blowing space facts",
    "Psychological facts about success",
    "Habits that change your life",
    "Inspiring real life stories",
    "Scientific discoveries that will surprise you",
    "How the brain really works",
    "Daily facts that make you smarter"
]

def get_trends():
    topic = random.choice(HALAL_TOPICS)
    return {
        "topic": topic,
        "platform": "YouTube Shorts",
        "length": "30-45 seconds"
    }
