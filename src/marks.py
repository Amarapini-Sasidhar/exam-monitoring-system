import json
import os

MARKS_FILE = '../data/marks.json'

def load_marks():
    if not os.path.exists(MARKS_FILE):
        return {}
    with open(MARKS_FILE, 'r') as f:
        return json.load(f)

def save_marks(marks):
    with open(MARKS_FILE, 'w') as f:
        json.dump(marks, f, indent=4)

def update_student_marks(student, subject, score):
    marks = load_marks()
    if student not in marks:
        marks[student] = {}
    marks[student][subject] = score
    save_marks(marks)

def view_student_marks(student):
    marks = load_marks()
    student_marks = marks.get(student, {})
    if not student_marks:
        print("No marks available.")
    else:
        for subject, score in student_marks.items():
            print(f"{subject}: {score}")
