print('''
To do -list manager 

With this program you can create and edit a To Do -list

''')

#from todo.py import add_task, view_tasks, remove_task

# Initialize the list
tasks = []

def main ():
    while True:
        
        #Ask for user input
        user_input = input("""
        Please select an option (type 1, 2, 3 or 4):
        1: Add task
        2: View tasks
        3: Remove task
        4: Exit program
        """)

        #Print header of the to do list:
        print("""
        
        TO DO -LIST:
        
        """)

        #Call correct function:
        if user_input == '1':
            print("Add")  
            #add_task()
        elif user_input == '2':
            print("View")
            #view_tasks()
        elif user_input == '3':
            print("Remove")
            #remove_task()
        elif user_input == '4':
            print("Exiting program. Thank you for using the To Do -list manager.")
            break
        else:
            print("""Invalid option. Please type 1, 2, 3 or 4.
            1: Add task
            2: View tasks
            3: Remove task
            4: Exit
            """)


# Run the program
if __name__ == '__main__':
    main()
    