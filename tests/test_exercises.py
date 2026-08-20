from scripts.exercise_doctor import main


def test_question_driven_exercise_contract() -> None:
    assert main() == 0
