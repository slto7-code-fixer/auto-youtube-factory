# المدير العام
def review(stats):
    if stats["views"] < 500:
        return "Improve hooks"
    return "Keep scaling"
