
print("Simple To Do List App")
print("By: Kyle Javier")


'''
PSEUDOCODE

create a global pending task list
-- create `completed list` to view and append to

while loop
  print menu options
  
  ask user choice
  
  validate user choice and match appropriate service
    if user choice is 'Add a new task':
        ask for the new task name
        append new task to the list
        show success message
    
    if user choice is 'view all pending tasks':
        validate if list has items in it:
          iterate through the whole list and print each task
        if list have no items in it:
          show appropriate message ("Empty List")
        
        Optional: view `completed list` for completed tasks
    
    if user choice is 'mark a task as done':
        validate list has items:
          iterate through the whole list and print each task
          
          ask user which task to mark as done
            add *DONE to the end of the string name
            show success message to user ("Marked task as done")
        
          Optional:
            append the task in a `completed list`:
            show success message to user
    
    if user choice is Exit the program
        show goodbye message
        break
    
    if user choice is invalid
        show error message, try again


'''

# global variables declaration
pending_tasks = []
completed_tasks = []


def add_task():
    new_task = input("\nEnter new task name: ")
    pending_tasks.append(new_task)
    print(f"task '{new_task}' has been added.\n")


def view_task_list():

    while True:
        print("\n-----Select List to View-----")
        print("a. Pending Tasks")
        print("b. Completed Tasks")
        print("c. Cancel\n")

        choice = input("Enter List:").upper()

        if choice == "A":
            # checking if the list has tasks in it
            if pending_tasks:
                print("-----Pending Tasks-----")
                # Iterate through the whole list and print each task
                for index, task in enumerate(pending_tasks, start=1):
                    print(f"{index}. {task}")
                print("\n")
                break
            # if the list is empty
            else:
                print("No pending tasks! Good Job")
                break
        elif choice == "B":
            # checking if the list has tasks in it
            if completed_tasks:
                print("-----Completed Tasks-----")
                # Iterate through the whole list and print each task
                for index, task in enumerate(completed_tasks, start=1):
                    print(f"{index}. {task}")
                print("\n")
                break
            # if the list is empty
            else:
                print("No completed tasks JUST YET! Finish them!")
                break
        elif choice == "C":
            break
        else:
            print(f"`{choice}` is an invalid choice")


def mark_task_done():
    if pending_tasks:
        print("-----Mark task as done-----")
        # Iterate through the whole list and print each task
        for index, task in enumerate(pending_tasks, start=1):
            print(f"{index}. {task}")

        task_completed = int(input("Enter task to mark as done: "))
        completed_tasks.append(pending_tasks[task_completed - 1])
        print(f"Task `{pending_tasks[task_completed - 1]}` completed. Well Done! ")
        pending_tasks.pop(task_completed - 1)
        print("\n")
    # if the list is empty
    else:
        print("No tasks to mark as done.")


while True:
    # Main menu services options
    print("\n-----Available Services-----")
    print("a. Add a new task")
    print("b. View task lists")
    print("c. Mark a task as done")
    print("d. Exit the program\n")

    # getting user choice of service to use
    user_choice = input("Enter choice of service: ").upper()

    # user selects: Adding a new task
    if user_choice == "A":
        add_task()
    # user selects: View all pending tasks
    elif user_choice == "B":
        view_task_list()
    # user selects: Mark a task as done
    elif user_choice == "C":
        mark_task_done()
    # user selects: Exit the program
    elif user_choice == "D":
        print("Exiting the program! GoodBye!")
        break
    # user selects: invalid service
    else:
        print(f"`{user_choice}` is an invalid choice. Please try again.")

