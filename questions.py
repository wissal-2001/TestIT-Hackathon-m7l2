# =============================================================
# MODULE : questions.py
# ROLE   : Stores the list of questions for the TestIT application
# AUTHOR : Participant 1
# =============================================================
#
# HOW TO FORMAT A QUESTION:
# "Question text\n1)Option1\n2)Option2\n3)Option3\n4)Option4#CORRECT_ANSWER"
#
# RULES:
# - \n   = new line (to display options on separate lines)
# - #    = separator between the question and the correct answer
# - The number after # = the correct answer (1, 2, 3 or 4)
#
# EXAMPLE:
# "What color is the sky?\n1)Green\n2)Blue\n3)Red\n4)Yellow#2"
#  --> correct answer is option 2 (Blue)
# =============================================================

question1 = "How do you spell the name of the P* programming language?\n1)Piton\n2)Pilon\n3)Python\n4)Pyton#3"

question2 = "In programming, what number is used to indicate the False value for a Boolean variable?\n1)0\n2)1\n3)-1\n4)-1#1"

question3 = "Which tool can be used to repeat the execution of some lines of code a given number of times?\n1)conditional statement\n2)function\n3)variable\n4)loop#4"

question4 = "What command can be used to organize a loop in Python?\n1)for\n2)while\n3)for or while\n4)for, while or if#3"

question5 = "In which version of the code does the variable i take values from 0 to 10 at each step of the loop?\n1)for i in range(0,10)\n2)for i in range(11)\n3)while i <= 10\n4)i='012345678910'#2"
