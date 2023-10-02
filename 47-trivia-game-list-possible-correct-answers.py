#!/usr/bin/env python3
# Day 47

import random

# List of trivia questions and their corresponding answers
trivia_questions = [
    {
        "question": "What is the capital of Spain?",
        "answers": ["Madrid"]
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answers": ["Mars"]
    },
    {
        "question": "Where do Luton Town play their home games?",
        "answers": ["Kenilworth Road", "The Kenny"]
    },
    {
        "question": "Who did Luton Town beat in the Championship play off final to gain promotion to the Premier League?",
        "answers": ["Coventry City", "Coventry"]
    },
]

def ask_question(question_dict):
    question = question_dict["question"]
    answers = question_dict["answers"]
    user_answer = input(f"Question: {question}\nYour Answer: ")

    if any(user_answer.lower() == answer.lower() for answer in answers):
        print("Correct! Great job!")
    else:
        correct_answers = " or ".join(answers)
        print(f"Oops! The correct answer is: {correct_answers}")

def main():
    print("Welcome to Random Trivia!")

    while True:
        selected_question = random.choice(trivia_questions)
        ask_question(selected_question)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Have a great day!")
            break

if __name__ == "__main__":
    main()


"""
In this modified code, I've changed the "answer" key in the question dictionary to "answers" and provided a list of possible correct answers. The ask_question function now checks if the user's input matches any of the answers in the list using a generator expression and the any() function.

Now, both "Coventry City" and "Coventry" will be accepted as correct answers for the Luton Town question. You can use this approach to handle more flexible answers for other questions as well.

"""
