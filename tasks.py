class TaskQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task):
        self.queue.append(task)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

    def get_all(self):
        return self.queue

class TaskStack:
    def __init__(self):
        self.stack = []

    def push(self, task):
        self.stack.append(task)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def get_all(self):
        return self.stack
