# Define the Task class to represent a task in the system
class Task:
    def __init__(self, task_id, priority, duration):
        # Initialize task attributes
        self.task_id = task_id  # Unique identifier for the task
        self.priority = priority  # Priority of the task (higher value = higher priority)
        self.duration = duration  # Duration of the task in time units
        self.status = "Waiting"  # Initial status of the task

    def __repr__(self):
        # Method to represent the task as a string (used for printing)
        return f"Task(ID={self.task_id}, Priority={self.priority}, Duration={self.duration}, Status={self.status})"


# Function to initialize the system
def initialize_system():
    task_queue = []  # List to hold tasks
    system_clock = 0  # System clock to track time
    return task_queue, system_clock


# Function to load tasks into the task queue
def load_tasks(task_queue):
    # Create a list of tasks
    tasks = [
        Task(1, 3, 5),  # Task 1: Priority 3, Duration 5
        Task(2, 1, 5),  # Task 2: Priority 1, Duration 5
        Task(3, 2, 4)   # Task 3: Priority 2, Duration 4
    ]
    # Add tasks to the task queue
    task_queue.extend(tasks)


# Function to schedule tasks based on priority
def schedule_tasks(task_queue):
    # Sort tasks by priority in descending order (higher priority first)
    task_queue.sort(key=lambda x: x.priority, reverse=True)
    # Return the highest-priority task
    return task_queue[0]


# Function to execute a task
def execute_task(task, system_clock):
    # Update task status to "running"
    task.status = "Running"
    print(f"Executing {task} at time {system_clock}")
    # Decrement the task's duration
    task.duration -= 1
    # Check if the task is completed
    if task.duration == 0:
        task.status = "Completed"
        print(f"\n Task {task.task_id} completed at time {system_clock}\n")
    return task


# Main function to run the task-scheduling algorithm
def main():
    # Initialize the system
    task_queue, system_clock = initialize_system()
    # Load tasks into the task queue
    load_tasks(task_queue)

    # Continue processing tasks until the task queue is empty
    print("\n ******* Initiating the Task.*******\n")
    while task_queue:
        # Schedule the highest-priority task
        current_task = schedule_tasks(task_queue)
        # Execute the task
        current_task = execute_task(current_task, system_clock)
        # Increment the system clock
        system_clock += 1

        # Check if the task is completed
        if current_task.status == "Completed":
            # Remove the completed task from the queue
            task_queue.remove(current_task)

    # Print a message when all tasks are completed
    print("\n ******* All tasks completed.*******")


# Entry point of the program
if __name__ == "__main__":
    main()