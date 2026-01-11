def profit_score(topic):
    score = 0
    keywords = {
        "science": 3,
        "facts": 3,
        "psychology": 3,
        "habits": 2,
        "story": 2
    }

    for k, v in keywords.items():
        if k in topic.lower():
            score += v

    return score
