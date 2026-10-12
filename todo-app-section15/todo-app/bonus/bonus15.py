# 148. Bonus Example (Section 15): a quiz app that reads JSON.
#
# questions.json (same folder) is a LIST of DICTIONARIES. Each dict is
# one question with 3 keys: "question_text", "alternatives" (a list of
# choices) and "correct_answer" (a NUMBER: 3 means the 3rd choice).
# Run this file from the bonus folder (PyCharm: right-click > Run).

import json     # standard module: turns JSON text into Python data

# Read the whole file as ONE string.
with open("questions.json", 'r') as file:
    content = file.read()

# json.loads = "load string": the JSON text becomes a Python list of dicts.
data = json.loads(content)

# LOOP 1: ask every question and store the answer.
for question in data:                       # question = one dictionary
    print(question["question_text"])        # the value of that key
    # Nested loop: print the choices as 1 - ..., 2 - ...
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)  # index + 1: start at 1, not 0
    # int(): the answer must be a NUMBER, like correct_answer (3, not "3")
    user_choice = int(input("Enter your answer: "))
    # Add a NEW key to this dictionary, next to the correct answer.
    question["user_choice"] = user_choice


# LOOP 2: check the answers and show the results.
score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1                   # one point per right answer
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    # Single quotes inside the f-string because it uses double quotes
    # outside. The \ at the end continues the line on the next line.
    message = f"{index + 1} {result}  - Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['correct_answer']}"
    print(message)

print(score, "/", len(data))                # e.g. 1 / 2
