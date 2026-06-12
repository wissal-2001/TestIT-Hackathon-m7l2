# =============================================================
# MODULE : test.py
# ROLE   : Contains the testing and evaluation functions
# AUTHOR : Participant 2
# =============================================================
#
# FUNCTIONS IN THIS MODULE:
#   - check_question(question) --> returns 1 (correct) or 0 (wrong)
#   - estimation(point)        --> returns a result message (string)
#
# IMPORTANT: This module is imported by main.py
# To call a function from main.py:
#   test.check_question(...)
#   test.estimation(...)
# =============================================================


def check_question(question):
    """
    Displays a question, gets the user's answer, and checks if it is correct.

    Parameter:
        question (str): a question string in the format:
                        "Question text\n1)opt1\n2)opt2\n3)opt3\n4)opt4#CORRECT"

    Returns:
        1 if the answer is correct
        0 if the answer is wrong
    """

    # Step 1: Find the position of the '#' character in the string
    last_letter = question.find("#")

    # Step 2: Extract only the visible part (question + options), without the answer
    cut_question = question[0:last_letter]

    # Step 3: Extract the correct answer (the character just after '#')
    right_answer = question[last_letter + 1]

    # Step 4: Display the question and get the user's input
    answer = input(cut_question)

    # Step 5: Compare and return the result
    if answer == right_answer:
        return 1
    else:
        return 0


def estimation(point):
    """
    Evaluates the candidate's final score and returns a result message.

    Parameter:
        point (int): total number of correct answers (0 to 5)

    Returns:
        A string message describing the result
    """

    if point < 2:
        return "At this time, we are not ready to consider you as a potential candidate for the position."
    elif point > 4:
        return "You have passed the test!! We'll be waiting for you at the next stage of the interview!"
    else:
        return "Get some extra training and come back!"
