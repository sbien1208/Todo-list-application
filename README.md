# Todo-list-application
It is a console-based application that helps you keep track of tasks. You can add, delete, and complete tasks using the command-line interface.


# **How to run the project ?**

cd main.py
python main.py


# **How to contribute ?**

Fork the repository on Github.
Clone your forked repository to your local machine : git clone {URL of the repository}
Create a new branch : git checkout feature-name
Make your changes and test them
Commit your changes : git add .
git commit -m "Description of your changes"
Push your changer to your forked repository : git push origin feature-name
Create a pull request on the original repository
Await feedback and discussion on your pull request

Sure, let me explain the functions used in your code:

1. **display_menu()**
   - *Purpose:* Displays the menu options for the Task Manager.
   - *Explanation:* Prints a simple menu with options to add a task, delete a task, show tasks, and exit.

2. **add_task()**
   - *Purpose:* Adds a task to the todos list.
   - *Explanation:* Takes user input for a new task and appends it to the todos list. Prints a success message.

3. **show_tasks()**
   - *Purpose:* Displays the list of tasks.
   - *Explanation:* Prints the list of tasks stored in the todos list along with their respective indices.

4. **delete_task()**
   - *Purpose:* Deletes a task from the todos list.
   - *Explanation:* Displays the list of tasks with indices, asks the user to enter the task number they want to delete, and removes the selected task from the todos list. Handles errors if the input is invalid.

5. **while True: (Main loop)**
   - *Purpose:* Continuously runs the main loop until the user chooses to exit.
   - *Explanation:* Repeatedly displays the menu, takes the user's choice, and executes the corresponding action based on the choice. The loop continues until the user chooses to exit.

6. **choice == "1":, choice == "2":, choice == "3":, choice == "4": (Conditions inside the loop)**
   - *Purpose:* Controls the flow based on the user's choice.
   - *Explanation:* Checks the user's input and executes the corresponding function (add_task(), delete_task(), show_tasks()) or exits the program based on the user's choice.

7. **print("Invalid choice. Please enter a number between 1 and 3.")**
   - *Purpose:* Handles invalid user input.
   - *Explanation:* Prints a message when the user enters an invalid choice (not 1, 2, 3, or 4).

This code represents a simple console-based task manager with the ability to add tasks, delete tasks, show the list of tasks, and exit the program.

