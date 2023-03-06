class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def show_nodes(node):
    while node:
        print(node.val, end=',')
        node = node.right
    print('end')


def reverse_show_nodes(node):
    while node:
        print(node.val, end=',')
        node = node.left
    print('end')


# def find_mid_node(root):
#     if not root:
#         return root
#     slow = root
#     fast = root
#     # 偶数情况
#     while True:
#         if fast.right.right is None:
#             break
#         slow = slow.right
#         fast = fast.right.right
#
#     # 奇数情况
#     while True:
#         if fast.right is None:
#             break
#         slow = slow.right
#         fast = fast.right.right
#
#     while True:
#         if (fast.right is None) or (fast.right.right is None):
#             break
#         slow = slow.right
#         fast = fast.right.right
#
#     while fast.right or not fast.right.right:
#         slow = slow.right
#         fast = fast.right.right
#
#     return slow

def find_mid_node(root):
    if not root:
        return root
    slow = root
    fast = root
    while fast.right and fast.right.right:
        slow = slow.right
        fast = fast.right.right
    return slow


def find_mid_node_v2(root):
    # 当时偶数时候 返回中间偏右的节点
    # 当奇数的时候，返回中间的节点
    if not root:
        return root
    slow = root
    fast = root
    # while True:
    #     if not fast.next:
    #         return slow
    #     elif not fast.next.next:
    #         return slow.next
    #     else:
    #         slow = slow.next
    #         fast = fast.next.next

    while fast.right and fast.right.right:
        slow = slow.right
        fast = fast.right.right
    return slow if not fast.right else slow.right