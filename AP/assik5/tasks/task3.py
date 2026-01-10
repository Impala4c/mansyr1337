class Person:
    def __init__(self, name):
        self._name = name  # Encapsulation

    def get_role(self):
        return "Person"


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def get_role(self):
        return "Student"  # Polymorphism


people = [
    Person("Alex"),
    Student("Maria", 101)
]

for p in people:
    print(p.get_role())
