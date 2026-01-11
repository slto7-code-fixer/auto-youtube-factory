HARAM_KEYWORDS = [
    "music",
    "sexual",
    "gambling",
    "alcohol",
    "dating",
]

def halal_check(script):
    for word in HARAM_KEYWORDS:
        if word.lower() in script.lower():
            return False
    return True
