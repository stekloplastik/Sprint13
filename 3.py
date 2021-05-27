class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, elem):
    index = 0
    while node:
        if node.value == elem:
            return index
        index += 1
        node = node.next_item
    return -1
