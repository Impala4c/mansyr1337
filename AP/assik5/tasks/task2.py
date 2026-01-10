import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    grades = student["grades"]
    student["average_grade"] = sum(grades) / len(grades)

with open("students_with_average.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4)
