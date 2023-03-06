# 单链表反转
# 双向链表反转
from linkedlist.linkedlist_utils import *


def build_one_direction_linkedlist(n):
    nodes = []
    for i in range(1, n+1):
        nodes.append(Node(i))
    for i, node in enumerate(nodes):
        if i + 1 < len(nodes):
            node.right = nodes[i + 1]
    return nodes


def build_two_direction_linkedlist(n):
    nodes = []
    for i in range(1, n+1):
        nodes.append(Node(i))
    for i, node in enumerate(nodes):
        if i + 1 < len(nodes):
            node.right = nodes[i + 1]

        if i - 1 >= 0:
            node.left = nodes[i - 1]
    return nodes


def reverse_one_direction_node(root):
    # 1-> 2 -> 3 ->4
    prev = None
    head = root
    while root:
        head = root
        next = root.right
        root.right = prev
        prev = root
        root = next
    return head






def reverse_two_direction_node(root):
    # 1-> 2 -> 3 -> 4
    head = root
    while root:
        head =root
        next = root.right
        prev = root.left
        root.right = prev
        root.left = next
        root = next
    return head


def reverse_two_direction_node(root):
    # 1<-> 2 <-> 3 -> 4
    prev = None
    head = None
    while root:
        head = root
        next = root.right
        root.right = prev
        prev.left = root
        prev = prev.right
        root = next
    return head



if __name__ == '__main__':
    # # 验证单向链表
    # nodes1 = build_one_direction_linkedlist(4)
    # reverse_one_direction_node(nodes1[0])
    # show_nodes(nodes1[-1])
    # show_nodes(nodes1[0])

    # 验证双向链表
    nodes2 = build_two_direction_linkedlist(4)
    reverse_two_direction_node(nodes2[0])
    show_nodes(nodes2[-1])
    reverse_show_nodes(nodes2[0])

    # 测试 可行解， 边界解， 单个元素， 空元素，