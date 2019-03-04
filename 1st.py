class Task:

    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return ("The task is {} and due date is {}".format(self.description, self.due_date))


t1 = Task("write", "Jan 2")
print(t1)
print(t1.description)
t2 = Task("read", "Feb 4")
t3 = Task("sing", "April 5")
