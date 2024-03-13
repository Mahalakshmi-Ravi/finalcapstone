# Task Manager - Final Capstone
The aim of this project is to refactor the existing code for a task manager and enhance its features, demonstrating my proficiency in working with lists, functions, and string handling."

## Description
Initially, the task involved working with the supporting text files user.txt and tasks.txt. However, the code has been refactored to create these files if they do not already exist

![](txt_create.jpg)

The main body underwent alterations to incorporate functions for the various menu options and extend its functionality.

![](menu.jpg)

The menu will display differently based on whether the user has admin rights. However, the initial user must be an admin to register a new user, with the login information written in user.txt by default.

If a user selects an option by mistake, they can simply enter -1 to return to the main menu.

Upon selecting a specific task, users can mark it as complete or edit it. Editing is only allowed for tasks that are not yet completed.

When generating reports, the data within the files will be outputted in a readable format for the user.

Additionally, administrators have the option to display statistics, which will retrieve information from tasks.txt and users.txt.

## Getting started
the initial login credentials setup by the program is
user: admin
password: password

## Project Usage
This project is a component of my technical portfolio for the HyperionDev Software Engineering Bootcamp and serves as a demonstration for potential recruiters. It highlights my proficiency in refactoring code and working with lists, functions, string handling, as well as input/output operations