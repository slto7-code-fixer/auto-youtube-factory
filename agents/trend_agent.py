import random

TOPICS = [
    "Amazing science facts",
    "Psychological facts about success",
    "Mind blowing space facts",
    "Habits that change your life",
    "Inspiring real stories"
]

def get_trends():
    return random.choice(TOPICS)
