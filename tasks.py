def add_task(task_list, task):
    """
    Adds a task to the task list.

    Args:
        task_list (list): The list of tasks.
        task (str): The task to add.

    Returns:
        list: The updated task list.
    """
    task_list.append(task)
    return task_list