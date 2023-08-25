#!/usr/bin/env python3
# Day 47

import random

# List of trivia questions and their corresponding answers
trivia_questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris"]
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
    user_answer = input(f"Question: {question}\nYour Answer: ").strip()

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
By calling the strip() method on user_answer, any leading or trailing whitespace will be removed before comparing it with the correct answers. This way, the script will be more forgiving with regards to input containing trailing spaces.
"""
