#!/usr/bin/env python3
# Day 47

import random

# List of trivia questions and their corresponding answers
trivia_questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars"
    },
    {
        "question": "Where do Luton Town play their home games?",
        "answer": "Kenilworth Road"
    },
    {
        "question": "What is the largest mammal?",
        "answer": "Blue whale"
    }
    # Add more questions here
]

def ask_question(question_dict):
    question = question_dict["question"]
    answer = question_dict["answer"]
    user_answer = input(f"Question: {question}\nYour Answer: ")

    if user_answer.lower() == answer.lower():
        print("Correct! Great job!")
    else:
        print(f"Oops! The correct answer is: {answer}")

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

