student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student, grade in student_scores.items():
    if grade > 90:
        student_grades[student] = "Outstanding"
    elif grade > 80:
        student_grades[student] = "Exceeds Expectations"
    elif grade > 70:
        student_grades[student] = "Acceptable"
    elif:
        student_grades[student] = "Fail"

print(student_grades)