class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return f'error'
        return self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            return f'None'
        return max(self.items)


stack = StackMax()

n = int(input())
command = [list(map(str, input().split())) for i in range(n)]


for i in command:
    if len(i) == 2:
        if i[0] == 'push':
            stack.push(int(i[1]))
        else:
            raise ValueError(f'{i}?')
    elif len(i) == 1:
        if i[0] == 'pop':
            stack.pop()
        elif i[0] == 'get_max':
            print(stack.get_max())
        else:
            raise ValueError(f'{i}?')
