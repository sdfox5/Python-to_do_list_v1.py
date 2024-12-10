print('''TO-DO LIST MENU: 
1->> ADD task
2->> View task
3->> Edit task
4->>Search task
5->>Exit''')
def to_do_list():
    to_do_list = []
    choise = int(input("Enter your choise: \n"))
    if choise == 1:
        add_task = input("Enter the task To add : \n")
        print(f"Task {add_task} added successfuly")
        to_do_list.append(add_task)
    elif choise == 2:
         print(to_do_list) 
    elif choise ==3:
        print(f"YOUR TASK: \n{to_do_list}")      
        edit_task = input("Enter the task number to edit: \n") 
        edit_new_task = input("Enter the new task: \n")
        print("Task updated successfuly.")
        to_do_list.remove(edit_task)
        to_do_list.append(edit_new_task)
        print(f"YOUR NEW UPDIT TASK: \N{to_do_list}")
while True:
    to_do_list()
    choice = input("Do you want to calculate again? (yes/no):\n").strip().lower()
    if choice != "yes":
        print("Goodbye!")
        break