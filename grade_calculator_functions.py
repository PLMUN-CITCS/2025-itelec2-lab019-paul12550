def calculate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

while True:
    try:
        score = int(input("Enter your score: "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(f"Your Grade is: {grade}")
        else:
            print("Please enter a valid score between 0 and 100.")
    except ValueError:
        print("Please enter a valid integer.")
        continue