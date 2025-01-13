tasks = []
def add_task() -> bool:
    new_task = input("Enter task: ")
    try:
        tasks.append(new_task)
    except Exception:
        print(f"error: {Exception}")
        return False
    
    return True