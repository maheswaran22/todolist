class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("Your To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def delete_task(self, task_index):
        try:
            del self.tasks[task_index - 1]
        except IndexError:
            print("Invalid task index.")

my_list = ToDoList()
my_list.display_tasks()
my_list.add_task("Buy groceries")
my_list.add_task("Walk the dog")
my_list.display_tasks()
my_list.delete_task(2)
my_list.display_tasks()
