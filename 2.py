class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return str(self.value)


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(node, idx):
    if idx == 0:
        next_node = get_node_by_index(node, idx + 1)
        head = next_node
        return head
    previous_node = get_node_by_index(node, idx - 1)
    head = get_node_by_index(node, idx)
    previous_node.next_item = head.next_item
    return node


def linked_list(node):
    while node:
        print(node.value)
        node = node.next_item
