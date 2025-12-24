# Student Grade Calculator
# Author: Swathi
# Description: Calculates student grade based on marks with validation

def calculate_grade(marks):
    """Returns grade and message based on marks"""
    if 90 <= marks <= 100:
        return "A", "Excellent work! Keep shining 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up 👍"
    elif 70 <= marks <= 79:
        return "C", "Good effort! You can do even better 😊"
    elif 60 <= marks <= 69:
        return "D", "You passed. Keep practicing 💪"
    else:
        return "F", "Don't give up! Work harder next time 🚀"


# Main Program
print("🎓 STUDENT GRADE CALCULATOR 🎓")

student_name = input("Enter student name: ")

while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Invalid marks! Please enter marks between 0 and 100.")
    except ValueError:
        print("❌ Please enter numeric values only.")

grade, message = calculate_grade(marks)

print("\n📊 RESULT FOR", student_name.upper())
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
