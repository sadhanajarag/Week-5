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
def add_task_manually(task_queue):
    print("\n Add New Task : ")
    task_id = len(task_queue)+1
    while True:
        try:
            priority = int(input("Enter the task Priority (highet value = higher priority) : "))
            break
        except:
            print("Invalid Input. Check the value of Priority should be in number")
    # Validate duration input
    while True:
        try:
            duration = int(input("Enter the task duration (in minutes): "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Duration must be a number. Please try again.")

    # Create a new task and add it to the queue
    new_task = Task(task_id, priority, duration)
    task_queue.append(new_task)
    print(f"Task {task_id} added successfully!\n")

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

def display_task(task_queue):
    if not task_queue:
        print("\n No Task in the queue")
    else:
        print("\n Task in the queue:")
        for task in task_queue:
            print(task)
        print()

# Main function to run the task-scheduling algorithm
def main():
    # Initialize the system
    task_queue, system_clock = initialize_system()
    while True:
        #Display menu option
        print("\n *******Task Scheduling System***********")
        print("1. Add a Task")
        print("2. View All Task")
        print("3. Run Scheduler for task")
        print("4. Exit")
        choice = int(input("Enter the choice between 1-4 : "))

        if choice == 1:
            #Add a Task manually
            add_task_manually(task_queue)
        elif choice == 2:
            # Display all task in queue
            display_task(task_queue)
        elif choice == 3:
            # Run the Scheduler
            if not task_queue:
                print("\n No task to schedule.Please add task first .\n")
            else:
                print("\n************ Initiating the Task Scheduler**********")
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
        elif choice == 4:
            #Exit the Program
            print("\n Exiting the program...................Goodbye!!!!!!!!")
            break
        else:
            #Handle Invalid Input
            print("\n Invalid choice .Please try again. \n")


# Entry point of the program
if __name__ == "__main__":
    main()