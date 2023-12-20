student_scores = input("Input a list of student scores: ").split()
highest = 0

student_scores = [int(score) for score in student_scores]

print(f"All the scores {student_scores}")

for score in student_scores:
    if score > highest:
        highest = score

print(f"The highest score is {highest}")

print(max(student_scores))
print(min(student_scores))