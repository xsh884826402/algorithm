# 单链表反转
# 双向链表反转
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

# nodes1存储单向链表
nodes1 = []
# nodes2 存储双向链表
nodes2 = []

for i in range(1, 5):
    nodes1.append(Node(i))
    nodes2.append(Node(i))
# 构造单向链表

for i, node in enumerate(nodes1):
    if i+1<len(nodes1):
        node.right = nodes1[i+1]

#构造双向链表
for i, node in enumerate(nodes2):
    if i+1 < len(nodes2):
        node.right = nodes2[i+1]

    if i-1 >= 0:
        node.left = nodes2[i-1]

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



# show_nodes(nodes2[0])


def reverse_node(root):
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


def reverse_node_bidirect(root):
    # 1-> 2 -> 3 -> 4
    head = root
    while root:
        head =root
        next = root.right
        prev = root.left
        root.right = prev
        root.left = next
        if root.val==2:
            print(prev.val, root.val, next.val)
        root = next
    # print(root.val, root.right, root.left)
    return head


reverse_node_bidirect(nodes2[0])
show_nodes(nodes2[3])
reverse_show_nodes(nodes2[0])
