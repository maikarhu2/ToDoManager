# git ryhmä harjoitus a Jani (lead), b Jarmo, c Jussi, d Maiju 

#add_task
def add_task() -> bool:
    new_task = input("Enter task: ")
    try:
        tasks.append(new_task)
    except Exception:
        print(f"error: {Exception}")
        return False
    
    return True

# view_tasks
def view_tasks(tasks):
	print("This is the list of existing tasks")
	index = 0
	while index < len(tasks):  # while items in list
		print(f'{index+1}. {tasks[index]}')    # print item

# remove_task
def remove_task(tasks):
    answer = int(input('Choose number to remove '))
    tasks.remove(answer-1)
