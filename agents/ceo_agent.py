def decision(report):
    if "Rejected" in report:
        return "Fix content quality"
    return "Keep scaling"
