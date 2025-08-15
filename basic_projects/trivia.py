"""
This is questions and answer game where user will be presented with list
of random questions with multichoice answers. You will need to select
correct answer. Based on the weightage of each question, final score will
be shared with the user. Overall score would be out of 100.
"""
import random
from itertools import combinations

PASSING_PERCENTAGE = 72
MAX_PERCENTAGE = 100
QUESTION_LIST = [
    {
        "id": 1,
        "question": "What is the output of print(type([]))?",
        "answers": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"],
        "correct_answer": "<class 'list'>",
        "weightage": 20
    },
    {
        "id": 2,
        "question": "Which keyword is used to define a function in Python?",
        "answers": ["function", "def", "define", "func"],
        "correct_answer": "def",
        "weightage": 15
    },
    {
        "id": 3,
        "question": "What is the output of 3 * 'Python'?",
        "answers": ["PythonPythonPython", "3Python", "Error", "Python3"],
        "correct_answer": "PythonPythonPython",
        "weightage": 25
    },
    {
        "id": 4,
        "question": "Which module in Python supports regular expressions?",
        "answers": ["regex", "pyregex", "re", "express"],
        "correct_answer": "re",
        "weightage": 30
    },
    {
        "id": 5,
        "question": "What does the 'len()' function return?",
        "answers": ["Length of an object", "Memory usage", "Data type", "Number of variables"],
        "correct_answer": "Length of an object",
        "weightage": 10
    },
    {
        "id": 6,
        "question": "What is a correct way to start a class definition in Python?",
        "answers": ["def MyClass:", "class MyClass()", "create class MyClass", "class MyClass:"],
        "correct_answer": "class MyClass:",
        "weightage": 35
    },
    {
        "id": 7,
        "question": "Which of these is a mutable type?",
        "answers": ["tuple", "str", "list", "int"],
        "correct_answer": "list",
        "weightage": 40
    },
    {
        "id": 8,
        "question": "How do you install external packages in Python?",
        "answers": ["python get", "install.py", "pip install", "setup package"],
        "correct_answer": "pip install",
        "weightage": 30
    },
    {
        "id": 9,
        "question": "What is the purpose of the 'pass' statement?",
        "answers": ["Exits a loop", "Skips iteration", "Placeholder", "Throws exception"],
        "correct_answer": "Placeholder",
        "weightage": 30
    },
    {
        "id": 10,
        "question": "Which built-in function returns the memory address of an object?",
        "answers": ["mem()", "address()", "id()", "loc()"],
        "correct_answer": "id()",
        "weightage": 45
    },
    {
        "id": 11,
        "question": "What is the output of bool('False')?",
        "answers": ["False", "True", "0", "None"],
        "correct_answer": "True",
        "weightage": 50
    },
    {
        "id": 12,
        "question": "What is the scope of variables declared inside a function?",
        "answers": ["Global", "Shared", "Local", "Module"],
        "correct_answer": "Local",
        "weightage": 30
    },
    {
        "id": 13,
        "question": "Which keyword is used to handle exceptions?",
        "answers": ["raise", "catch", "try", "except"],
        "correct_answer": "except",
        "weightage": 30
    },
    {
        "id": 14,
        "question": "Which Python statement is used to iterate over a sequence?",
        "answers": ["repeat", "loop", "for", "while"],
        "correct_answer": "for",
        "weightage": 20
    },
    {
        "id": 15,
        "question": "Which of the following is a Python tuple?",
        "answers": ["(1, 2)", "[1, 2]", "{1, 2}", "<1, 2>"],
        "correct_answer": "(1, 2)",
        "weightage": 20
    },
    {
        "id": 16,
        "question": "What does the 'is' keyword test?",
        "answers": ["Equality", "Type match", "Identity", "Assignment"],
        "correct_answer": "Identity",
        "weightage": 40
    },
    {
        "id": 17,
        "question": "Which of these is not a core data type in Python?",
        "answers": ["int", "list", "dict", "class"],
        "correct_answer": "class",
        "weightage": 35
    },
    {
        "id": 18,
        "question": "Which keyword is used to create a generator?",
        "answers": ["yield", "return", "generate", "pass"],
        "correct_answer": "yield",
        "weightage": 60
    },
    {
        "id": 19,
        "question": "Which function can convert a string to an integer?",
        "answers": ["int()", "str()", "float()", "bool()"],
        "correct_answer": "int()",
        "weightage": 15
    },
    {
        "id": 20,
        "question": "How do you declare a virtual environment in Python?",
        "answers": ["venv create", "python -m venv env", "virtualenv new", "env python"],
        "correct_answer": "python -m venv env",
        "weightage": 65
    }
]


def find_weighted_subset(questions, target_weightage):
    random.shuffle(questions)
    n = len(questions)

    for r in range(1, n + 1):
        for combo in combinations(questions, r):
            total = sum(q['weightage'] for q in combo)
            if total == target_weightage:
                return combo
    return []


def show_question_answers(idx, question):
  print(f"\n🧠 Question {idx} (Weightage: {question['weightage']})")
  print(f"{question['question']}\n")
  correct_option = 0
  for idx, option in enumerate(question['answers'], 1):
    print(f"  {idx}. {option}")
    if option == question['correct_answer']:
      correct_option = idx
  user_answer = input('Answer:')
  if user_answer == question['correct_answer'] or int(user_answer) == correct_option:
    return True
  else:
    return False


def start_game(user_name):
    random.shuffle(QUESTION_LIST)
    questions = find_weighted_subset(QUESTION_LIST, MAX_PERCENTAGE)
    total_answers = 0
    for idx, question in enumerate(questions, 1):
        if show_question_answers(idx, question):
            total_answers += question["weightage"]
    if total_answers >= PASSING_PERCENTAGE:
        print("*" * 143)
        print(f"Congratulations \033[1m{user_name}\033[0m, you have passed the Quiz! Your Passing score if {total_answers}")
        print("*" * 143)
    else:
        print("*" * 143)
        print(f"Sorry {user_name}, you don't have enough right answers! Your Passing score if {total_answers}. Please retry it again.")
        print("*" * 143)
    return total_answers


if __name__ == '__main__':
    print("*" * 143)
    print("Hello There. Well come to game of Python.")
    username = input("What is your name? ").capitalize().strip()
    print(
        f"Hello,{username}! Welcome to the Python Quiz. Here we will present you list of few questions and possible answers.\nYou will Need to select correct answer.At the end of the game we will present you the score. Passing score is 72%.")
    print("*" * 143)

    answer = input(f"Are you ready to play, {username}? (Y/N) :").lower().strip()
    if answer == "Y" or answer == "y":
        start_game(username)
    else:
        print(f"Looks like you need some time to prepare, {username}. Never mind. We can start once you are ready. Thank you.")
