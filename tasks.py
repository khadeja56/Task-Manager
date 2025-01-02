

def add_task(task_list, task):



   
    task_list.append(task)
    return task_list

def remove_task(task_list, task):
   
    if task in task_list:
        task_list.remove(task)
        return task_list
    return "Task not found!"

 
    if task in task_list:
        return "Task already exists!"
        task_list.append(task)
    return task_list

