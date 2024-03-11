import os
def reg_user():
    # Function to register a new user
    username = input("Enter username: ")

    try:
        with open('user.txt', 'r') as file:
            existing_users = file.readlines()
            if any(username in user for user in existing_users):
                print(f"Username {username} already exists. Please choose a different username.")
            else:
                with open('user.txt', 'a') as user_file:
                    user_file.write(username + '\n')
                print(f"User {username} registered successfully!")
    except FileNotFoundError:
        with open('user.txt', 'w') as user_file:
            user_file.write(username + '\n')
        print(f"User {username} registered successfully!")


def add_task():
    # Get task details from user input
    task_description = input("Enter task description: ")
    assigned_to = input("Assign task to (username): ")
    # Additional task creation logic if needed
    with open('tasks.txt', 'a') as file:
         # Write task details to 'tasks.txt'
        file.write(f"{task_description} - Assigned to: {assigned_to}\n")
    print("Task added successfully!")

def view_all():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            if tasks:
                 # Display all tasks in a user-friendly format
                for task in tasks:
                    print(task.strip())
            else:
                print("No tasks available.")
    except FileNotFoundError:
        print("No tasks available.")

def view_mine():
    # Get the username for which tasks should be displayed
    assigned_to = input("Enter your username: ")
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            user_tasks = [task.strip() for task in tasks if f"Assigned to: {assigned_to}" in task]
            if user_tasks:
                for task in user_tasks:
                    print(task)
            else:
                print(f"No tasks assigned to {assigned_to}.")
    except FileNotFoundError:
        print(f"No tasks assigned to {assigned_to}.")
#update main menu
while True:
    command = input("Enter command (r/a/va/vm/q to quit): ").lower()

    if command == 'r':
        reg_user()
    elif command == 'a':
        add_task()
    elif command == 'va':
        view_all()
    elif command == 'vm':
        view_mine()
    elif command == 'q':
        print("Exiting program.")
        break
    else:
        print("Invalid command. Try again.")

def mark_task_as_complete(task_to_modify):
    # Implement logic to mark the task as complete in 'tasks.txt'
    # Update the 'Yes/No' value to 'Yes'
    # Example:
    # task_to_modify = task_to_modify.replace("No", "Yes")
    print(f"Task {task_to_modify} marked as complete.")

def edit_task(task_to_modify):
    # Implement logic to edit the task in 'tasks.txt'
    # Allow editing of assigned username or due date (if the task is not yet completed)
    # Example:
    # new_assigned_to = input("Enter the new assigned username: ")
    # new_due_date = input("Enter the new due date: ")
    # task_to_modify = f"{new_description} - Assigned to: {new_assigned_to} - Due: {new_due_date}\n"
    print(f"Task edited successfully: {task_to_modify}")

def generate_reports():
    # Implement logic to generate reports in 'task_overview.txt' and 'user_overview.txt'
    # Output relevant data in a user-friendly, easy-to-read manner
    # Example:
    # with open('task_overview.txt', 'w') as task_file:
    #     task_file.write("Task Overview Report:\n")
    #     # Write task-related data to the file
    # with open('user_overview.txt', 'w') as user_file:
    #     user_file.write("User Overview Report:\n")
    #     # Write user-related data to the file
    print("Reports generated successfully.")


def reg_user():
    username = input("Enter username: ")

    try:
        with open('user.txt', 'r') as file:
            existing_users = file.readlines()
            if any(username in user for user in existing_users):
                print(f"Username {username} already exists. Please choose a different username.")
            else:
                with open('user.txt', 'a') as user_file:
                    user_file.write(username + '\n')
                print(f"User {username} registered successfully!")
    except FileNotFoundError:
        with open('user.txt', 'w') as user_file:
            user_file.write(username + '\n')
        print(f"User {username} registered successfully!")


def view_mine():
    assigned_to = input("Enter your username: ")

    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            user_tasks = [task.strip() for task in tasks if f"Assigned to: {assigned_to}" in task]

            if user_tasks:
                print("Your tasks:")
                for i, task in enumerate(user_tasks, 1):
                    print(f"{i}. {task}")

                while True:
                    choice = input("Enter the task number to mark as complete, 'e' to edit, or '-1' to return to the main menu: ")
                    
                    if choice == '-1':
                        break
                    elif choice.isdigit() and 1 <= int(choice) <= len(user_tasks):
                        task_index = int(choice) - 1
                        task_to_modify = user_tasks[task_index]
                        edit_or_complete = input("Enter 'c' to mark as complete or 'e' to edit: ")

                        if edit_or_complete == 'c':
                            mark_task_as_complete(task_to_modify)
                        elif edit_or_complete == 'e':
                            edit_task(task_to_modify)
                        else:
                            print("Invalid option. Please enter 'c' to mark as complete, 'e' to edit, or '-1' to return to the main menu.")
                    else:
                        print("Invalid task number. Please enter a valid task number or '-1' to return to the main menu.")
            else:
                print(f"No tasks assigned to {assigned_to}.")
    except FileNotFoundError:
        print(f"No tasks assigned to {assigned_to}.")

def add_task():
    task_description = input("Enter task description: ")
    assigned_to = input("Assign task to (username): ")
    # Additional task creation logic if needed
    with open('tasks.txt', 'a') as file:
        file.write(f"{task_description} - Assigned to: {assigned_to}\n")
    print("Task added successfully!")

def mark_task_as_complete(task_to_modify):
    # Implement logic to mark the task as complete in 'tasks.txt'
    # Update the 'No' value to 'Yes'
    # Example:
    # task_to_modify = task_to_modify.replace("No", "Yes")
    print(f"Task {task_to_modify} marked as complete.")

def edit_task(task_to_modify):
    # Implement logic to edit the task in 'tasks.txt'
    # Allow editing of assigned username or due date (if the task is not yet completed)
    # Example:
    # new_assigned_to = input("Enter the new assigned username: ")
    # new_due_date = input("Enter the new due date: ")
    # task_to_modify = f"{new_description} - Assigned to: {new_assigned_to} - Due: {new_due_date}\n"
    print(f"Task edited successfully: {task_to_modify}")

def generate_reports():
    # Ensure 'tasks.txt' and 'user.txt' files exist
    for filename in ['tasks.txt', 'user.txt']:
        if not os.path.exists(filename):
            with open(filename, 'w'):
                pass  # Create an empty file if it doesn't exist

    tasks = []  # Define tasks outside the try block

    try:
        # Read tasks data from 'tasks.txt'
        with open('tasks.txt', 'r') as task_file:
            tasks = task_file.readlines()

        # Calculate task-related statistics
        total_tasks = len(tasks)
        completed_tasks = sum("Yes" in task for task in tasks)
        uncompleted_tasks = sum("No" in task for task in tasks)
        overdue_tasks = sum("No" in task and "Due: overdue" in task for task in tasks)
        incomplete_percentage = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        overdue_percentage = (overdue_tasks / uncompleted_tasks) * 100 if uncompleted_tasks > 0 else 0

        # Write task-related data to 'task_overview.txt'
        with open('task_overview.txt', 'w') as task_overview_file:
            task_overview_file.write("Task Overview Report:\n")
            task_overview_file.write(f"Total tasks: {total_tasks}\n")
            task_overview_file.write(f"Completed tasks: {completed_tasks}\n")
            task_overview_file.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
            task_overview_file.write(f"Overdue tasks: {overdue_tasks}\n")
            task_overview_file.write(f"Incomplete task percentage: {incomplete_percentage:.2f}%\n")
            task_overview_file.write(f"Overdue task percentage: {overdue_percentage:.2f}%\n")

    except FileNotFoundError:
        print("No tasks available for generating task overview report.")

    try:
        # Read users data from 'user.txt'
        with open('user.txt', 'r') as user_file:
            users = user_file.readlines()

        # Write user-related data to 'user_overview.txt'
        with open('user_overview.txt', 'w') as user_overview_file:
            user_overview_file.write("User Overview Report:\n")
            user_overview_file.write(f"Total users: {len(users)}\n")

            for user in users:
                assigned_tasks = [task for task in tasks if f"Assigned to: {user.strip()}" in task]
                total_assigned_tasks = len(assigned_tasks)
                assigned_percentage = (total_assigned_tasks / total_tasks) * 100 if total_tasks > 0 else 0
                completed_assigned_tasks = sum("Yes" in task for task in assigned_tasks)
                completed_assigned_percentage = (completed_assigned_tasks / total_assigned_tasks) * 100 if total_assigned_tasks > 0 else 0

                user_overview_file.write(f"\nUser: {user.strip()}\n")
                user_overview_file.write(f"Total tasks assigned: {total_assigned_tasks}\n")
                user_overview_file.write(f"Percentage of total tasks: {assigned_percentage:.2f}%\n")
                user_overview_file.write(f"Percentage of completed tasks: {completed_assigned_percentage:.2f}%\n")

    except FileNotFoundError:
        print("No users available for generating user overview report.")

    print("Reports generated successfully.")

def display_statistics():
    try:
        # Read tasks data from 'tasks.txt'
        with open('tasks.txt', 'r') as task_file:
            tasks = task_file.readlines()

        total_tasks = len(tasks)
        completed_tasks = sum("Yes" in task for task in tasks)
        uncompleted_tasks = sum("No" in task for task in tasks)
        overdue_tasks = sum("No" in task and "Due: overdue" in task for task in tasks)
        incomplete_percentage = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        overdue_percentage = (overdue_tasks / uncompleted_tasks) * 100 if uncompleted_tasks > 0 else 0

        print("Task Overview Report:")
        print(f"Total tasks: {total_tasks}")
        print(f"Completed tasks: {completed_tasks}")
        print(f"Uncompleted tasks: {uncompleted_tasks}")
        print(f"Overdue tasks: {overdue_tasks}")
        print(f"Incomplete task percentage: {incomplete_percentage:.2f}%")
        print(f"Overdue task percentage: {overdue_percentage:.2f}%")

    except FileNotFoundError:
        print("No tasks available for generating task overview report.")

    try:
        # Read users data from 'user.txt'
        with open('user.txt', 'r') as user_file:
            users = user_file.readlines()

        for user in users:
            assigned_tasks = [task for task in tasks if f"Assigned to: {user.strip()}" in task]
            total_assigned_tasks = len(assigned_tasks)
            assigned_percentage = (total_assigned_tasks / total_tasks) * 100 if total_tasks > 0 else 0
            completed_assigned_tasks = sum("Yes" in task for task in assigned_tasks)
            completed_assigned_percentage = (completed_assigned_tasks / total_assigned_tasks) * 100 if total_assigned_tasks > 0 else 0
            incomplete_assigned_percentage = 100 - completed_assigned_percentage if total_assigned_tasks > 0 else 0
            overdue_assigned_tasks = sum("No" in task and "Due: overdue" in task for task in assigned_tasks)
            overdue_assigned_percentage = (overdue_assigned_tasks / total_assigned_tasks) * 100 if total_assigned_tasks > 0 else 0

            print(f"\nUser: {user.strip()}")
            print(f"Total tasks assigned: {total_assigned_tasks}")
            print(f"Percentage of total tasks: {assigned_percentage:.2f}%")
            print(f"Percentage of completed tasks: {completed_assigned_percentage:.2f}%")
            print(f"Percentage of incomplete tasks: {incomplete_assigned_percentage:.2f}%")
            print(f"Percentage of overdue tasks: {overdue_assigned_percentage:.2f}%")

    except FileNotFoundError:
        print("No users available for generating user overview report.")

# Update main menu
while True:
    command = input("Enter command (r/a/va/vm/g/d/q to quit): ").lower().strip()

    if command == 'r':
        reg_user()
    elif command == 'a':
        add_task()
    elif command == 'va':
        view_all()  
    elif command == 'vm':
        view_mine()
    elif command == 'g':
        generate_reports()
    elif command == 'd':
        display_statistics()
    elif command == 'q':
        print("Exiting program.")
        break
    else:
        print("Invalid command. Try again.")
