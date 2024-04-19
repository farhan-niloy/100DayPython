student_scores = {
    "Harry": 91,
    "Ron": 78,
    "Octavian": 94,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 73,
}

grade_dictionary = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        grade_dictionary[student] = "Outstanding"
    elif score > 80:
        grade_dictionary[student] = "Exceeds Expectations"
    elif score > 70:
        grade_dictionary[student] = "Acceptable"
    elif score > 60:
        grade_dictionary[student] = "Rejected"

print(grade_dictionary)