# الفلتر الشرعي
HARAM_WORDS = ["music", "sex", "dating", "gambling"]

def halal_check(script):
    for word in HARAM_WORDS:
        if word in script.lower():
            return False
    return True
