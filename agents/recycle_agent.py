# تحويل Shorts → فيديو طويل
SHORTS = []

def add_short(script):
    SHORTS.append(script)

def can_make_long():
    return len(SHORTS) >= 5
