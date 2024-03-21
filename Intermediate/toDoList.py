class ToDo:
    def __init__(self):
        self.tasks = []

    def create_task(self):
        try:
            task_name = input("Enter task name: ")
            priority = input("Enter priority: ")
            time = input("Enter time: ")
            task = {
                'task': task_name,
                'priority': priority,
                'time': time
            }
            self.tasks.append(task)
            self.save_tasks()
        except ValueError:
            print("Error: Incorrect data type entered. Please enter valid input.")

    def display_tasks(self):
        self.load_tasks()
        for task in self.tasks:
            print(task['task'] + ' ' + task['priority'] + ' ' + task['time'])

    def delete_task(self):
        try:
            task_index = int(input("Enter the index of the task to delete: "))
            print(self.tasks[task_index]['task'] + " deleted")
            self.tasks.pop(task_index)
            self.save_tasks()
        except (ValueError, IndexError):
            print("Error: Invalid input or index out of range.")

    def update_task(self):
        try:
            task_index = int(input("Enter the index of the task to update: "))
            task_name = input("Enter the new task name: ")
            priority = input("Enter the new priority: ")
            time = input("Enter the new time: ")
            self.tasks[task_index]['task'] = task_name
            self.tasks[task_index]['priority'] = priority
            self.tasks[task_index]['time'] = time
            self.save_tasks()
            print(self.tasks[task_index]['task'] + " updated")
        except (ValueError, IndexError):
            print("Error: Invalid input or index out of range.")

    def save_tasks(self):
        with open('Intermediate/tasks.txt', 'w') as file:
            for task in self.tasks:
                file.write(f"{task['task']},{task['priority']},{task['time']}\n")

    def load_tasks(self):
        try:
            with open('Intermediate/tasks.txt', 'r') as file:
                self.tasks = []
                for line in file:
                    task_data = line.strip().split(',')
                    task = {
                        'task': task_data[0],
                        'priority': task_data[1],
                        'time': task_data[2]
                    }
                    self.tasks.append(task)
        except FileNotFoundError:
            print("No tasks file found. Starting with an empty list.")

if __name__ == '__main__':
    todo = ToDo()
    while True:
        print("1) Create a task")
        print("2) Display the tasks")
        print("3) Delete a task")
        print("4) Update a task")
        print("5) Exit")
        try:
            choice = int(input("Enter the choice: "))
            if choice == 1:
                todo.create_task()
            elif choice == 2:
                todo.display_tasks()
            elif choice == 3:
                todo.delete_task()
            elif choice == 4:
                todo.update_task()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please enter a valid choice.")
        except ValueError:
            print("Error: Invalid choice. Please enter a valid integer choice.")
