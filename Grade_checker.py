# ─── Grade Checker ── Single File with Functions ───────────────────────────

def get_score():
    score = float(input("Enter student score: "))
    return score

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

def display_result(score, grade):
    print(f"\nScore : {score}")
    print(f"Grade : {grade}")

def main():
    score = get_score()

    if not validate_score(score):
        print("Invalid score! Please enter a value between 0 and 100.")
        return

    grade = get_grade(score)
    display_result(score, grade)

main()
