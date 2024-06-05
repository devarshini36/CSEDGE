class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.description} - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task added: {task.description}")

    def delete_task(self, task_index):
        try:
            removed_task = self.tasks.pop(task_index)
            print(f"Task deleted: {removed_task.description}")
        except IndexError:
            print("Invalid task index!")

    def complete_task(self, task_index):
        try:
            self.tasks[task_index].completed = True
            print(f"Task marked as completed: {self.tasks[task_index].description}")
        except IndexError:
            print("Invalid task index!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks):
                print(f"{idx}. {task}")

def main():
    todo_list = ToDoList()
    
    print("To-Do List Application")
    
    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Complete task")
        print("4. Show tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            description = input("Enter task description: ").strip()
            todo_list.add_task(description)
        elif choice == '2':
            try:
                task_index = int(input("Enter task index to delete: ").strip())
                todo_list.delete_task(task_index)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == '3':
            try:
                task_index = int(input("Enter task index to mark as completed: ").strip())
                todo_list.complete_task(task_index)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
    
if __name__ == "__main__":
    main()
