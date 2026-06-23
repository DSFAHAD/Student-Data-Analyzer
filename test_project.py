from project import count_students, calculate_average

def test_count_students():
    students = [
        {"name":"Ali"},
        {"name":"Sara"}
    ]
    assert count_students(students) == 2

def test_calculate_average():
    students = [
        {"average":80},
        {"average":90}
    ]
    assert calculate_average(students) == 85
from project import get_grade

def test_get_grade():
    assert get_grade(85) == "A"
    assert get_grade(75) == "B"
    assert get_grade(65) == "C"
    assert get_grade(55) == "D"
    assert get_grade(40) == "F"     