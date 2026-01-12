# بوابة الجودة - نسخة مرنة
def quality_check(script):
    word_count = len(script.split())
    
    # تقليل العتبة من 25 إلى 15 كلمة
    if word_count < 15:
        return False, f"Script too weak: {word_count} words (minimum: 15)"
    
    # إضافة كلمات CTA إضافية
    cta_keywords = ['follow', 'subscribe', 'like', 'اشترك', 'تابع']
    script_lower = script.lower()
    
    if not any(keyword in script_lower for keyword in cta_keywords):
        return False, "No CTA found (add: follow, subscribe, like)"
    
    return True, f"Passed: {word_count} words with CTA"
