# WEEK2
# Student Grade Calculator
# Week 2 Project - Python Basics

def calculate_grade(marks):
    """Returns grade and message based on marks."""
    if marks >= 90:
        return "A", "Excellent work! Keep shining! 🌟"
    elif marks >= 80:
        return "B", "Great job! You're doing really well! 👍"
    elif marks >= 70:
        return "C", "Good effort! Keep practicing! 🙂"
    elif marks >= 60:
        return "D", "You passed, but there's room for improvement! 💪"
    else:
        return "F", "Don't worry! Keep trying, and you'll improve! 🚀"

def main():
    print("📘 Student Grade Calculator")
    print("------------------------------")

    try:
        marks = float(input("Enter your marks (0-100): "))

        # Basic error handling
        if marks < 0 or marks > 100:
            print("❗ Please enter marks between 0 and 100.")
            return

        grade, message = calculate_grade(marks)

        print("\n🎓 Your Grade:", grade)
        print("💬 Message:", message)

    except ValueError:
        print("❗ Invalid input! Please enter numbers only.")

# Program execution starts here
if __name__ == "__main__":
    main()
