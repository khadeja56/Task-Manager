def remove_task(task_list, task):
    """
    Removes a task from the task list.

    Args:
        task_list (list): The list of tasks.
        task (str): The task to remove.

    Returns:
        list: The updated task list or a message if the task is not found.
    """
    if task in task_list:
        task_list.remove(task)
        return task_list
    return "Task not found!"