student_heights = input("Input everyone's height to calculate average height: ").split()
total_height = 0
total_students = 0

for n in range(0, len(student_heights)):
    try:
        student_heights[n] = int(student_heights[n])
        total_height += student_heights[n]
        total_students += 1
        print(f"Student {n + 1} height: {student_heights[n]}")
    except ValueError:
        print(f"Invalid height: {student_heights[n]}. Please enter a valid integer.")

if total_students > 0:
    avg_height = total_height / total_students
    print(f"Total students: {total_students}, Total height: {total_height}, Average height: {avg_height}")
else:
    print("No valid heights entered.")
