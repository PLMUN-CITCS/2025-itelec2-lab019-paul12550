def get_student_score():
    """
    Handles user input to obtain the student's score.
    Returns:
        float: The student's score as a float.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            return score
        except ValueError:
            print("Please enter a valid numerical score.")

def calculate_grade(score):
    """
    Determines the letter grade based on the given score and grading scale.
    
    Args:
        score (float): The student's score.
    
    Returns:
        str: The corresponding letter grade.
    """
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

# Main program flow
score = get_student_score()
grade = calculate_grade(score)
print(f"Your Grade is: {grade}")