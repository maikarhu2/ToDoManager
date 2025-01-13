# git ryhmä harjoitus Jani (lead), b Jarmo, c Jussi, d Maiju 

def view_tasks(tasks):
	print("This is the list of existing tasks")
	index = 0
	while index < len(tasks):  # while items in list
		print(f'{index+1}. {tasks[index]}')    # print item