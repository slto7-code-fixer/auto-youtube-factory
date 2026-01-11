# بوابة الجودة
def quality_check(script):
    if len(script.split()) < 25:
        return False, "Script too weak"
    if "follow" not in script.lower():
        return False, "No CTA"
    return True, "Passed"
