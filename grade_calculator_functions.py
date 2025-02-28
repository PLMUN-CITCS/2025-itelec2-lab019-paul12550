def get_student_score():
    """
    Handles user input to obtain the student's score.
    No parameters.
    Prompts the user to enter their score.
    Reads and converts the input to a numerical type (integer or float).
    Returns the numerical score.
    """
    score = input("Enter your score: ")
    try:
        # Convert the input to a numerical type
        numerical_score = float(score)
    except ValueError:
        # Handle the case where the input is not a number
        print("Invalid input. Please enter a valid numerical score.")
        return None
    return numerical_score
def calculate_grade(score):
    """
    Determines the letter grade based on the given score and grading scale.
    Takes one parameter: score (numeric).
    Uses conditional statements (if, elif, else) to check the score against the grading scale.
    Returns the corresponding letter grade ('A', 'B', 'C', 'D', or 'F') as a string.
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

def get_student_score():
    """
    Handles user input to obtain the student's score.
    No parameters.
    Prompts the user to enter their score.
    Reads and converts the input to a numerical type (integer or float).
    Returns the numerical score.
    """
    score = input("Enter your score: ")
    try:
        # Convert the input to a numerical type
        numerical_score = float(score)
    except ValueError:
        # Handle the case where the input is not a number
        print("Invalid input. Please enter a valid numerical score.")
        return None
    return numerical_score

def calculate_grade(score):
    """
    Determines the letter grade based on the given score and grading scale.
    Takes one parameter: score (numeric).
    Uses conditional statements (if, elif, else) to check the score against the grading scale.
    Returns the corresponding letter grade ('A', 'B', 'C', 'D', or 'F') as a string.
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
def main():
    score = get_student_score()
    if score is not None:
        grade = calculate_grade(score)
        print(f"Your letter grade is: {grade}")

# Run the main program
if __name__ == "__main__":
    main()