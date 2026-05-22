import re

class Student:
    def __init__(self, name, email, grades):
        self.name = name

        if self.validate_email(email):
            self.email = email
        else:
            print(f"Warning: '{email} is not a valid email format.")
            self.email = email
        
        self.grades = [grades] if isinstance(grades, int) else list(grades)

    def add_grade(self, grades):
        if 0 <= grades <= 100:
            self.grades.append(grades)
        else:
            return "Please enter a valid grade between 0 and 100."
    
    def average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        print(f"Student Name:{self.name}")
        print(f"Student Email: {self.email}")
        print(f"Grades: {self.grades}.")
        print(f"Average Grade: {self.average_grade():.2f}")
        print("-" *30)

    def grades_tuple(self):
        return tuple(self.grades)
    
    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$"
        return bool(re.match(pattern, email))
    
student1 = Student("Alice", "alice@gmail.com", 92)
student2 = Student("Craig", "craig@gmail.com", 99)
student3 = Student("Jules", "jules@gmail.com", 82)

student1.add_grade(87)
student2.add_grade(100)
student3.add_grade(82)
student1.add_grade(90)
student2.add_grade(50)
student3.add_grade(100)


student1.display_info()
student2.display_info()
student3.display_info()

student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

def get_student_by_email(email):
    return student_dict.get(email, "Student not found.")

print(f"Lookup Alice: {get_student_by_email('alice@gmail.com').name}")

unique_grades = set()
for student in student_dict.values():
    unique_grades.update(student.grades)

print(f"Unique grades across everyone: {unique_grades}")

alice_tuple = student1.grades_tuple()
print(f"Alice's grades as a tuple: {alice_tuple}")

try:
    alice_tuple[0] = 100
except TypeError as e:
    print(f"Caught unexpected exception! Tuples are immutable. Error: {e}")

for student in [student1, student2, student3]:
    print(f"\nModifying grades for {student.name}...")

    removed = student.grades.pop()
    print(f"Removed last grade: {removed}")

    print(f"First grade: {student.grades[0]}")
    print(f"Last grade: {student.grades[-1]}")

    print(f"Total grades remaining: {len(student.grades)}")

above_90_count = 0
for student in [student1, student2, student3]:
    for grade in student.grades:
        if grade > 90:
            above_90_count += 1

print(f"Total remaining grades strictly above 90: {above_90_count}")