import json
import os

BASE_DIR = os.path.dirname(__file__)
json_path = os.path.join(BASE_DIR, "students.json")

with open(json_path, "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    grades = student["grades"]
    student["average_grade"] = sum(grades) / len(grades)


