# Create a ToDoList class with a tasks list (which will contain instances
# of the Task class). Create an __init__ method and an add_task method that
# allows you to pass in an instance of your Task class.
# Try creating a todo list and adding your three tasks to it.


from '1st' import Task


class Todo:

    todo_list = []

    def __init__(self, tasks):
        self.tasks = tasks

    @classmethod
    def add_task(cls, description, due_date):
        task = Task(description, due_date)
        cls.todo_list.append(task)
        return cls.todo_list


t1 = Todo.add_task("write", "Jan 2")
t2 = Todo.add_task("read", " Feb 4")
t3 = Todo.add_task("sing", " April 5")
print(len(Todo.todo_list))
print(Todo.todo_list[1])
print(Todo.todo_list[2].due_date)
