print('''
To do -list manager 

With this program you can create and edit a To Do -list

''')

from todo.py import add_task, view_tasks, remove_task

def main ():
    #Ask for user input
    user_input = input("""
    Please select an option (type 1, 2, 3 or 4):
    1: Add task
    2: View tasks
    3: Remove task
    4: Exit
    """)

    #Call correct function:
    if user_input == '1':  
        add_task()
    elif user_input == '2':
        view_tasks()
    elif user_input == '3':


# Run the program
if __name__ == '__main__':
    main()
    