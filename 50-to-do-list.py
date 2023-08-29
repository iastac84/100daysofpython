#!/usr/bin/env python3
# Day 50

'''
Generate a simple to-do list. The script allows you to add tasks, view the current tasks, and mark tasks as completed
The script provides a simple menu-driven interface for managing a to-do list. You can add tasks, view tasks, mark tasks as completed, and exit the program.
'''

# Initialize an empty list to store tasks
tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print("Task added:", task)

def view_tasks():
    if tasks:
        print("Current tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else " "
            print(f"{idx}. [{status}] {task['task']}")
    else:
        print("No tasks yet.")

def mark_completed(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed:", tasks[task_number - 1]["task"])
    else:
        print("Invalid task number.")

# Main loop
while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        task_number = int(input("Enter the task number to mark as completed: "))
        mark_completed(task_number)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

