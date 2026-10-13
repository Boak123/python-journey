class Student:
    def __init__(self, student_id: str, name: str, course: str):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __repr__(self):
        return f"Student(student_id='{self.student_id}', name='{self.name}', course='{self.course}')"

class StudentRegistry:
    def __init__(self, students: list[Student] | None = None) -> None:
        # Added a default value so StudentRegistry() works with no arguments
        self.students = students if students is not None else []

    def register_student(self, student: Student):
        # Changed from register_students() to accept a single student to register
        if student is not None:
            self.students.append(student)
        return None

    def get_student_count(self):
        # Renamed to match the get_student_count() call in your test block
        return len(self.students)


# --- Test Cases ---

# Initialize registry
registry = StudentRegistry()

# Verify initial count is 0
print(registry.get_student_count())  
# Output: 0

# Register students
registry.register_student(Student("S001", "Alice", "Computer Science"))
registry.register_student(Student("S002", "Bob", "Mathematics"))

# Verify updated count
print(registry.get_student_count())  
# Output: 2

# Inspect registered students
print(registry.students)  
# Output: [Student(student_id='S001', name='Alice', course='Computer Science'), Student(student_id='S002', name='Bob', course='Mathematics')]