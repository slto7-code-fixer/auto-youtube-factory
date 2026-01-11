HARAM = ["music", "dating", "alcohol", "gambling"]

def halal_check(text):
    return not any(word in text.lower() for word in HARAM)
