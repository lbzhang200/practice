"""
Add a task. Prompt the user to enter a task to add to the end of the list.
View all tasks. Display all tasks in the to-do list in the order they were entered. If the list is empty, display the message "No tasks in the list."
Quit the program. Say goodbye and end the program.
"""

tasks = []

while True:
    
    print("\n Menu")
    print("\n 1. Add a task")
    print("\n 2. View all tasks")
    print("\n 3. Quit")

    option = int(input("Choose an option -> "))

    if option == 1:
        add = input("Enter the task to add: ")
        tasks.append(add)
    elif option == 2:
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

    elif option == 3:
        print("goodbye!")
        break

    else: 
        print("invalid option")


"""
Enter width -> 7
Enter height -> 4
#######
#     #
#     #
#######
"""

w = int(input("Enter the width"))
h = int(input("Enter the height"))

if h == 1:
    print("#" * w)

else:
    print("#" * w)
    for i in range(h-2):
        print("#" + (w-2) * " " + "#")

    print("#" * w)
