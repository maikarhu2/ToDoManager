tasks = []

def add_task() -> bool:
    new_task_content = input("Enter task: ")
    try:
        tasks.append((len(tasks), new_task_content))
    except Exception:
        print(f"error: {Exception}")
        return False
    
    return True
    
