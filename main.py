# =============================================================
# MODULE : main.py
# ROLE   : Main program — runs the full TestIT application
# AUTHOR : Participant 3
# =============================================================
#
# THIS FILE:
#   - Imports the 'time' module (standard Python library)
#   - Imports the 'questions' module (questions.py)
#   - Imports the 'test' module (test.py)
#   - Runs all 5 questions and accumulates the score
#   - Measures the total time spent on the test
#   - Displays the final results
#
# IMPORTANT: questions.py, test.py and main.py must all be
#            in the SAME FOLDER for the imports to work.
# =============================================================

import time       # standard Python module for time measurement
import questions  # our questions module (questions.py)
import test       # our test module (test.py)


# --- Get candidate information ---
name = input("Enter name: ")

# --- Start the timer ---
start_time = time.time()   # saves the current timestamp (in seconds)

# --- Run all 5 questions and accumulate the score ---
# check_question() returns 1 (correct) or 0 (wrong)
# We add each result to the total score

point = test.check_question(questions.question1)
point = point + test.check_question(questions.question2)
point = point + test.check_question(questions.question3)
point = point + test.check_question(questions.question4)
point = point + test.check_question(questions.question5)

# --- Stop the timer ---
end_time = time.time()     # saves the end timestamp

# --- Calculate the time spent ---
result_time = end_time - start_time      # duration in seconds (float)
result_time = round(result_time, 2)      # round to 2 decimal places

# --- Get the result message ---
estimation = test.estimation(point)      # returns a string based on the score

# --- Display the final results ---
print("\n========== TEST RESULTS ==========")
print("Candidate:", name)
print("Time for test completion:", result_time, "sec")
print("Points scored:", point, "/ 5")
print(estimation)
print("===================================")
