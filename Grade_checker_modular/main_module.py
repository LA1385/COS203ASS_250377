# ─── Main Module ────────────────────────────────────────────────────────────

from input_module import get_score
from logic_module import validate_score, get_grade
from output_module import display_result, display_error

def main():
    score = get_score()

    if not validate_score(score):
        display_error("Invalid score! Please enter a value between 0 and 100.")
        return

    grade = get_grade(score)
    display_result(score, grade)

main()
