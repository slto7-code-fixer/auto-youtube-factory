def profit_score(topic):
    score = 0
    keywords = ["science", "facts", "psychology", "brain", "mind"]
    for k in keywords:
        if k in topic.lower():
            score += 2
    return score
