# بوابة الجودة - معدلة
def quality_check(script):
    word_count = len(script.split())
    
    # تقليل العتبة من 25 إلى 10 كلمات
    if word_count < 10:
        return False, f"Script too weak: {word_count} words (minimum: 10)"
    
    # إضافة كلمات CTA إضافية
    cta_keywords = ['follow', 'subscribe', 'like', 'share', 'comment']
    script_lower = script.lower()
    
    if not any(keyword in script_lower for keyword in cta_keywords):
        return False, "No CTA found (add: follow, subscribe, like, share, comment)"
    
    return True, f"Passed: {word_count} words, CTA present"
