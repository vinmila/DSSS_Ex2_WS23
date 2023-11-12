import random

def QuizInput(minimum, maximum):
    """
    This function returns a random integer within the specified range [minimum, maximum].
    """
    return random.randint(minimum, maximum)

def MathOperator():
    """
    This function returns a random mathematical operator for the quiz.
    """
    return random.choice(['+', '-', '*'])

def QuizCalc(n1, n2, o):
    """
    This function receives two numbers and a mathematical operator, performs the mathematical operation, and returns the question and result.
    """
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a

def math_quiz():
    """
    This function conducts the quiz by calling sub-functions to get random inputs and mathematical operators.
    It also gets the user's answer, evaluates the user's answer with the computed answer, and declares the result.
    """
    # Counter for tracking correct answers
    score = 0
    # Total number of questions
    total_questions = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Functions for getting random inputs and operators
        n1 = QuizInput(1, 10)
        n2 = QuizInput(1, 5)
        o = MathOperator()

        # Function call for performing QuizCalc
        problem, answer = QuizCalc(n1, n2, o)
        print(f"\nQuestion: {problem}")

        # Entry of User Response and Handling user input error
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        # Verification of User Answer with Computed Answer
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
