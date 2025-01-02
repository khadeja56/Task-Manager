def add_task(task_list, task):
    """
    Adds a task to the task list.
    Prevents adding duplicate tasks.

    Args:
        task_list (list): The list of tasks.
        task (str): The task to add.

    Returns:
        list: The updated task list or a message if the task exists.
    """
    if task in task_list:
        return "Task already exists!"
    task_list.append(task)
    return task_list
