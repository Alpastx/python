def calculate_grade(average_marks):
    if average_marks >= 90:
        return "A+"
    elif 80 <= average_marks < 90:
        return "A"
    elif 70 <= average_marks < 80:
        return "B"
    elif 60 <= average_marks < 70:
        return "C"
    elif 50 <= average_marks < 60:
        return "D"
    else:
        return "F"

subject_marks = []
for i in range(5):
    marks = float(input("Enter marks for subject {}: ".format(i + 1)))
    subject_marks.append(marks)

average_marks = sum(subject_marks) / len(subject_marks)

grade = calculate_grade(average_marks)
print("Average Marks:", average_marks)
print("Grade:", grade)
