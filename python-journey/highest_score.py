# Write a function that returns the name of the student with the highest score.
def highest_score(students):
    highest_grade = 70
    highest_student = "Alice"
    for student, grade in  students.items():
        if grade > highest_grade:
            highest_grade = grade
            highest_student = student
    print(f"{highest_student}")


students = {
    "Alice": 85,
    "Bob": 42,
    "Charlie": 91,
    "David": 78
}
highest_score(students)      