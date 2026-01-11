def quality_check(script):
    if len(script.split()) < 20:
        return False, "Script too short"

    if "follow" not in script.lower():
        return False, "Weak call to action"

    return True, "Passed"
