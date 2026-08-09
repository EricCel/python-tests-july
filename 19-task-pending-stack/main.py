#Create a pending task stack using lists with operations to add tasks and complete the last task.

class stacks():
    def __init__ (self):
        self.stack = []

    def push(self,*items):
        return self.stack.extend(items)

    def pop(self):
        return self.stack.pop()

    @property
    def peek(self):
        return self.stack[-1]

    @property
    def size(self):
        return len(self.stack)

    @property
    def get(self):
        return self.stack

tasks = stacks()
tasks.push('clean', 'wash')
print(tasks.peek)