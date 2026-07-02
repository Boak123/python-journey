def grade_checker(students):
    for k, v in students.items():
        if v >= 50:
           print(f"{k}: passed" "/n")
        else:
            print(f"{k}: failed")

students = {
    "Alice": 85,
    "Bob": 42,
    "Charlie": 50,
    "David": 19
}
grade = grade_checker(students)
print(grade)