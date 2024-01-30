todos = []
# Function to display the menu and get user input
def display_menu():
    print("\n==== Task Manager ====")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Show Tasks")
    print("4. Exit")

# Function to add a task to the list
def add_task():
    task = input("Enter the task: ")
    todos.append(task)
    print("Task added successfully!")

def show_tasks():
    print("\n==== Tasks ====")
    for i, task in enumerate(todos, start=1):
        print(f"{i}. {task}")

# Function to delete a task from the list
def delete_task():
    print("\n==== Delete Task ====")
    for i, task in enumerate(todos, start=1):
        print(f"{i}. {task}")

    try:
        task_index = int(input("Enter the task number to delete: "))
        deleted_task = todos.pop(task_index - 1)
        print(f"Task '{deleted_task}' deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid task number.")


# Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        print("Exiting the Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")