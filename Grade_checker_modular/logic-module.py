# ─── Logic Module ───────────────────────────────────────────────────────────

def validate_score(score):
    if score < 0 or score > 100:
        return False
    return True

def get_grade(score):
    if score < 40:
        return "F"
    elif score < 45:
        return "E"
    elif score < 50:
        return "D"
    elif score < 60:
        return "C"
    elif score < 70:
        return "B"
    else:
        return "A"
