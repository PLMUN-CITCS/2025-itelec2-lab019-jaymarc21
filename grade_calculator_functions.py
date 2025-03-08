def get_student_score():
    """Handles user input to obtain the student's score."""
    score = float(input("86: "))  # Get user input and convert to float
    return score  # Return the score

def calculate_grade(score):
    """Determines the letter grade based on the given score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Main program execution
student_score = get_student_score()  # Get the score from user
grade = calculate_grade(student_score)  # Determine the grade

# Display the output
print(f"Your Grade is: {grade}")