from datetime import datetime, date
import os

user_login_stat = 0
logged_username = None

def validate_credentials(username, password):
    try:
        # Open the 'user.txt' file in read mode
        with open('user.txt', 'r') as file:
            # Iterate through each line in the file
            for line in file:
                # Split each line into username and password using ',' as delimiter
                v_username, v_password = line.strip().split(',')
                 #verify if the username and password provided matches the username stored in the file
                if username == v_username and password == v_password:
                    return True
        return False
    # Handle the case where the file 'user.txt' is not found
    except FileNotFoundError:
        # Print an error message indicating that the user credentials file is not found
        print("User credentials file not found.")
        return False
    
def user_exist(username):
    try:
        # Open the 'user.txt' file in read mode
        with open('user.txt', 'r') as file:
            # Iterate through each line in the file
            for line in file:
                # Split each line into username and password using ',' as delimiter
                v_username = line.strip().split(',')[0]
                #verify if the username provided matches the username stored in the file
                if username == v_username:
                    return True
        return False
    # Handle the case where the file 'user.txt' is not found
    except FileNotFoundError:
        # Print an error message indicating that the user file is not found
        print("User not found.")
        return False

def get_users():
     # Initialize an empty list to store usernames
    users = []
    try:        
        with open('user.txt', 'r') as file:
            # Read each line in the file
            for line in file:
                # Extract the username from each line by splitting at ','
                v_username = line.strip().split(',')[0]
                # Append the extracted username to the list of users
                users.append(v_username)
        # Return the list of usernames
        return users      
    except FileNotFoundError: 
        # If the file is not found, return an empty list of user       
        return users
    
def login():
    # getting user input for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")
    #validating credentials using if condition
    if validate_credentials(username, password):
        #if credentials are valid printing a success message and return a tuple indicating successful login
        print("\nLogin successful!")
        return 1,username
    else:
        # If invalid, print an error message and return a tuple indicating unsuccessful login
        print("Invalid username or password.")
        return 0,None
    
def reg_user():
    # Function to register a new user
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        # Try to open 'user.txt' file in read mode
        with open('user.txt', 'r') as file:
            # Read existing users from the file
            existing_users = file.readlines()
            # Check if the provided username already exists
            if any(username in user.split(",")[0] for user in existing_users):
                print(f"Username {username} already exists. Please choose a different username.")
            else:
                # If the username is unique, open the file again in append mode and add the new user
                with open('user.txt', 'a') as user_file:
                    user_file.write(username + ',' + password + '\n')
                # Print a success message
                print(f"\nUser {username} registered successfully!\n")
    except FileNotFoundError:
        # If the file doesn't exist, create it and add the new user
        with open('user.txt', 'w') as user_file:
            user_file.write(username + ',' + password + '\n')
        # Print a success message
        print(f"\nUser {username} registered successfully!\n")

def add_task():
    # Initialize assigned_to variable
    assigned_to = None
    while True:
        assigned_to = input("Kindly provide a username to assign task: ") # Prompt user to enter username for task assignment
        is_user_exist = user_exist(assigned_to)  # Check if the user exists
        # Make sure that user exists in "user.txt" file
        if is_user_exist is True:
            break # If user exists, exit the loop
        else:
            # Print error message if user does not exist
            print(f"{assigned_to} - User does not exist. Please enter a valid username.\n")    
    
    # Getting user inputs    
    task_name = input("Enter task name : ")
    task_desc = input("Enter task description : ")
    date_assigned = date.today() # Get the current date
    due_date = input("Due date of task (DD-MM-YYYY) : ")
    task_completed = "No"  # Initialize task_completed variable as "No"
    
    with open('tasks.txt', 'a') as file:
         # Write task details to 'tasks.txt'
        file.write(f"{assigned_to}#{task_name}#{task_desc}#{date_assigned}#{due_date}#{task_completed}\n")
    print("Task added successfully!")

def get_tasks():
    # Open 'tasks.txt' file in read mode
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines() # Read all lines from 'tasks.txt'
    
    # Loop through each task in the tasks list and append the task id to it
    lst_task = []
    count = 1               
    for task in tasks:                                        
        lst_task.append(str(count) + '#' + task )
        count+=1
    return lst_task

def modify_file(task_id, task_string):
     # Read and update the line corresponding to the task_id with the new task_string
    with open('tasks.txt', 'r') as file:
        lines = file.readlines()
        lines[task_id - 1] = task_string + "\n"
        out = open('tasks.txt', 'w')                                                
        out.writelines(lines)
        out.close()

def modify_task(lst_tasks:list):    
    while True:
        # Prompt user to enter task id or '-1' to return to the menu
        task_id = int(input("Kindly enter your task id or '-1' to return to the menu:  "))
        if task_id == -1:            
            break
        else:
            # Extract task details from the list of tasks based on task id            
            tsk = lst_tasks[task_id - 1]
            lst_task_modify = tsk.split('#')
            
            if (lst_task_modify[6].strip("\n").lower() == "yes"):
                print("Task has been already completed")
            else:
                # Prompt user to choose whether to mark task as complete or edit task
                modify_task = input("Kindly enter 'c' to mark task as complete or 'e' to edit task :  ").lower()
                if modify_task == "c":    
                    # Mark task as complete                
                    lst_task_modify[6] = "Yes"
                    lst_task_modify.pop(0)
                    task_string = "#".join(lst_task_modify)                    
                    modify_file(task_id, task_string)
                else:
                    # Prompt user to enter username to re-assign the task
                    while True:
                        assign_user = input("Kindly enter username to re-assign a task :  ").lower()
                        if user_exist(assign_user):
                            lst_task_modify[1] = assign_user
                            break
                        else:
                            print(f"{assign_user} user is not exist. Kindly provide a valid user")
                    
                    # Prompt user to enter due date for the task
                    while True:
                        try:
                            due_date = input("Kindly enter due date (DD-MM-YYYY) to a task :  ")
                            validate_date = datetime.strptime(due_date, "%d-%m-%Y")
                            break
                        except ValueError:                            
                            print("Invalid date format. Kindly use the specified format")
                    valid_due_date = validate_date.strftime("%d-%m-%Y")
                    lst_task_modify[5] = valid_due_date
                    lst_task_modify.pop(0)
                    task_string = "#".join(lst_task_modify)
                    print(task_string)
                    modify_file(task_id, task_string.strip("\n"))

def view_all():
    try:
        # Get all tasks from tasks file        
        total_tasks = get_tasks()                
        print("*"*30)
        for task in total_tasks:
            if len(task) > 10:
                tsk = task.split('#')                
                print(f"{'Task Id'.ljust(20)} : {tsk[0]}")
                print(f"{'Task Name'.ljust(20)} : {tsk[2]}")
                print(f"{'Task description'.ljust(20)} : {tsk[3]}")
                print(f"{'Assigned to'.ljust(20)} : {tsk[1]}")
                print(f"{'Date assinged'.ljust(20)} : {tsk[4]}")
                print(f"{'Due date'.ljust(20)} : {tsk[5]}")
                print(f"{'Task complete'.ljust(20)} : {tsk[6]}")
                print("*"*30)       

    except FileNotFoundError:
        print("No tasks available.")

def view_mine():    
    try:
        # Retrieve and filter tasks from the file for the logged-in user.
        lst_my_tasks = []
        lst_tasks = get_tasks()

        for task in lst_tasks:                        
            if logged_username == task.split('#')[1]:
                lst_my_tasks.append(task)                
        
        print("*"*30)

        # Display the task details for the logged-in user.
        for task in lst_my_tasks:
            tsk = task.split('#')            
            print(f"{'Task Id'.ljust(20)} : {tsk[0]}")
            print(f"{'Task Name'.ljust(20)} : {tsk[2]}")
            print(f"{'Task description'.ljust(20)} : {tsk[3]}")
            print(f"{'Assigned to'.ljust(20)} : {tsk[1]}")
            print(f"{'Date assinged'.ljust(20)} : {tsk[4]}")
            print(f"{'Due date'.ljust(20)} : {tsk[5]}")
            print(f"{'Task complete'.ljust(20)} : {tsk[6]}")
            print("*"*30)

        modify_task(lst_my_tasks)
            
    except FileNotFoundError:
        print(f"No tasks assigned to {logged_username}.")

def display_statistics():    
    
    # If files not available. it should be created before displaying resutls on screen 
    if (os.path.exists('./task_overview.txt') == False) or (os.path.exists('./user_overview.txt') == False):
        generate_reports()
    
    #show task overview on screen
    with open('task_overview.txt', 'r') as task_file:
        for line in task_file:
                print(line, end = '')
    
    #show user overview on screen
    with open('user_overview.txt', 'r') as user_file:
        for line in user_file:
            print(line, end = '')

def generate_reports():
    # Get all tasks and all the users list
    tasks = get_tasks()
    users = get_users()    

    # Define local variables
    total = len(tasks)
    total_users = len(users)
    complete = 0
    incomplete = 0
    overdue = 0
    percent_incomplete = 0
    percent_overdue = 0

    # calculation for the statistics 
    for i in range(0, total):
        task =  tasks[i].strip("\n").split("#")          
        if task[6].lower() == "yes":            
            complete += 1
        elif task[6].lower() == "no" and datetime.strptime(task[5], "%d-%m-%Y") < datetime.now():
            incomplete += 1
            overdue += 1
            percent_incomplete = (incomplete / total) * 100
            percent_overdue = (overdue / total) * 100

        elif task[6].lower() == "no":
            incomplete += 1
            percent_incomplete = (incomplete / total) * 100

    # Generate "task_overview.txt" in a viewable format
    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write(f"{'Total tasks'.ljust(30)}: {total}\n")
        task_overview_file.write(f"{'Completed tasks'.ljust(30)}: {complete}\n")
        task_overview_file.write(f"{'Uncompleted tasks'.ljust(30)}: {incomplete}\n")
        task_overview_file.write(f"{'Overdue tasks'.ljust(30)}: {overdue}\n")
        task_overview_file.write(f"{'Incomplete task percentage'.ljust(30)}: {percent_incomplete:.2f}%\n")
        task_overview_file.write(f"{'Overdue task percentage'.ljust(30)}: {percent_overdue:.2f}%\n")

    # Generate "user_overview.txt" in a viewable format
    with open("user_overview.txt", "w") as user_overview_file:
        user_overview_file.write(f"Total users\t: {total_users}\n")
        user_overview_file.write(f"Total tasks\t: {total}\n\n")

        # Loop through users to seperate tasks by assigned user
        for i in range(0, total_users):                        
            user_tasks = 0
            completed = 0
            not_complete = 0
            user_overdue = 0
            task_percent = 0
            complete_percent = 0
            incomplete_percent = 0
            overdue_percent = 0

            # Loop through set user to find relevant information, count tasks, completed and not, and due date
            for j in range(0, total):
                task =  tasks[j].strip("\n").split("#")                 
                if users[i] == task[1] and task[6].lower() == "yes":
                    user_tasks += 1
                    completed += 1

                # Converts datetime.strip from the string format into date
                elif users[i] == task[1] and task[6].lower() == "no" and datetime.strptime(task[5], "%d-%m-%Y") < datetime.now():
                    user_tasks += 1
                    not_complete += 1
                    user_overdue += 1

                elif users[i] == task[1] and task[6].lower() == "no":
                    user_tasks += 1
                    not_complete += 1

                # Calculate user percentage
                task_percent = (user_tasks / total) * 100
                if user_tasks != 0:
                    complete_percent = (completed / user_tasks) * 100
                    incomplete_percent = (not_complete / user_tasks) * 100
                    overdue_percent = (user_overdue / user_tasks) * 100

            # Write the results to file 
            user_overview_file.write("-" * 50 + "\n")
            user_overview_file.write(f"User: {users[i]}\n\n")
            user_overview_file.write(f"{'Total user tasks'.ljust(40)}: {user_tasks}\n")
            user_overview_file.write(f"{'Percentage of total tasks'.ljust(40)}: {task_percent:.2f}%\n")
            user_overview_file.write(f"{'Percentage of completed tasks'.ljust(40)}: {complete_percent:.2f}%\n")
            user_overview_file.write(f"{'Percentage of incomplete tasks'.ljust(40)}: {incomplete_percent:.2f}%\n")
            user_overview_file.write(f"{'Percentage of overdue tasks'.ljust(40)}: {overdue_percent:.2f}%\n")
    print("\n Report has been generated!\n")

def welcome():
    # Declare global variables to track user login status and username
    global user_login_stat
    global logged_username

    # Start an infinite loop to continuously prompt the user
    while True:
        
        # Check if the user is logged in
        if user_login_stat == 1:

            # Display menu options for logged-in users
            print("""\nKindly select one of the following options below :\n
r - register a user
a - add a task
va - view all tasks
vm - view my tasks
gr - generate reports""")
            if(logged_username == "admin"):
                print("ds - display Statistics")
            print("e - exit")
            command = input("\nKindly enter the code here : ").lower()
            if command == 'r':
                reg_user()
            elif command == 'a':
                add_task()
            elif command == 'va':
                view_all()
            elif command == 'vm':
                view_mine()
            elif command == 'gr':
                generate_reports()
            elif command == "ds" and logged_username.lower() == "admin":
                display_statistics()
            elif command == 'e':
                print("Exiting program.")
                logged_username = None
                user_login_stat = 0
                break
            else:
                print("\nInvalid command. Try again.")
        else:
            
            # Display options for users who are not logged in
            print(
                """
Kindly select one of the following Options below: \n
l - Login
q - Quit
                """
                  )
            command = input("Enter command (l/q to quit): ").lower()
            if command == 'l':
                
                user_login_stat, logged_username = login()
            elif command == 'q':
                print("Exiting program.")
                logged_username = None
                user_login_stat = 0
                break
            else:
                print("Invalid option. Try again.")

# Call the welcome function to start the program
welcome()