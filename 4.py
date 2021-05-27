class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)


def solution(node: DoubleConnectedNode):
    head = node  # голова списка, первый узел n1
    next_node = head.next  # следующий узел n2
    head.next = None  # делаем первый узел последним, изменив его n1.next на None вместо n2, n1 = DoubleConnectedNode('first', next=n2--> None, prev=None)
    head.prev = next_node  # делаем первый узел последним, изменив его n1.prev = None на n1.prev = next_node, n1 = DoubleConnectedNode('first', next = n2--> None, prev=head.next)
    while next_node is not None:  # итерация по списку слева направо, начиная со второго элемента так как next_node = head.next
        next_node.prev = next_node.next  # пока список не кончился, меняем местами prev/next у элементов
        next_node.next = head
        head = next_node
        next_node = next_node.prev
    return head
