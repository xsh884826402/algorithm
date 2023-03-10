class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

# nodes1存储单向链表
nodes = []
for i in range(1, 7):
    nodes.append(Node(i))

# 构造单向链表
for i, node in enumerate(nodes):
    if i+1 < len(nodes):
        node.next = nodes[i+1]


def find_mid_node(root):
    if not root:
        return root
    slow = root
    fast = root
    # 偶数情况
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def find_mid_node_v2(root):
    # 当时偶数时候 返回中间偏右的节点
    # 当奇数的时候，返回中间的节点
    if not root:
        return root
    slow = root
    fast = root
    while True:
        if not fast.next:
            return slow
        elif not fast.next.next:
            return slow.next
        else:
            slow = slow.next
            fast = fast.next.next

    # while fast.right and fast.right.right:
    #     slow = slow.next
    #     fast = fast.next.next
    # return slow if fast.right else slow.right



mid = find_mid_node_v2(nodes[0])
print(mid.val)

