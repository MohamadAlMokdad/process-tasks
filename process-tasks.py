import queue

def process_tasks(task_list):
    """
    Processes a list of tasks using a queue.
    Each task is expected to be a dictionary with keys: 'task_id', 'type', and 'value'.

    Args:
        task_list (list): List of tasks to process.

    Returns:
        list: A list of results for each task.
    """
    task_queue = queue.Queue()
    results = []

    # Enqueue tasks
    for task in task_list:
        task_queue.put(task)

    # Process tasks in the queue
    while not task_queue.empty():
        task = task_queue.get()
        task_id = task.get("task_id", "unknown")
        task_type = task.get("type", "other")
        task_value = task.get("value", None)

        if task_type == "math" and isinstance(task_value, (int, float)):
            # Perform a square root calculation
            result = f"Square root of {task_value} is {task_value ** 0.5:.2f}"
        elif task_type == "string" and isinstance(task_value, str):
            # Convert string to uppercase
            result = f"Uppercased string: {task_value.upper()}"
        else:
            # Handle other types
            result = f"Task type '{task_type}' not recognized or invalid value"

        results.append({"task_id": task_id, "result": result})

    return results


# Example usage
tasks = [
    {"task_id": 1, "type": "math", "value": 25},
    {"task_id": 2, "type": "string", "value": "hello"},
    {"task_id": 3, "type": "math", "value": 9},
    {"task_id": 4, "type": "string", "value": "world"},
    {"task_id": 5, "type": "other", "value": "unknown"},
    {"task_id": 6, "type": "math", "value": "invalid"},  # Invalid math task
]

# Process the tasks
results = process_tasks(tasks)

# Display the results
print("Task Results:")
for res in results:
    print(f"Task {res['task_id']}: {res['result']}")
