class Student:
    def __init__(self, student_id, name, program):
        self.student_id = student_id
        self.name = name
        self.program = program
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def transcript(self):
        lines = [f"{course}: {grade}" for course, grade in self.grades.items()]
        return f"{self.name} ({self.student_id}) - {self.program}\n" + "\n".join(lines)


if __name__ == "__main__":
    s = Student("A00123", "Alex Kim", "ITEC 1505")
    s.add_grade("Python Programming", 88)
    s.add_grade("Databases", 91)
    s.add_grade("Networking", 79)

    print(s.transcript())
    print(f"Average: {s.average():.2f}")
