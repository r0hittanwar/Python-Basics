# To Do List

tasks = []

while True:
    print("\n-----TO DO LIST-----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

# Add Task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added sucsessfully!")

# View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks Availaable")
        else:
            print("\nYour Tasks: ")
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}. {task}")

#Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No task to delete")
        else:
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}. {task}")

        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"{removed} deleted")
        else:
            print("Invalid number")

#Exit
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid Choices")
