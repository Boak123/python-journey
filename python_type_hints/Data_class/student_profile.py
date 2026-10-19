from dataclasses import dataclass

@dataclass
class StudentProfile:
    course_code: str
    course_name: str
    credit_units: int
    is_compulsory: bool

student = StudentProfile(course_code="CSC101", course_name="Introduction to Computing", credit_units=3, is_compulsory=True)

print(student)