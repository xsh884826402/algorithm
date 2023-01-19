# 非递归遍历
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 构造树
def build_tree(n):
    nodes = []
    for i in range(n):
        node = Node(i+1)
        nodes.append(node)

    for i in range(n):
        left_index = 2*i+1
        if left_index < n:
            nodes[i].left = nodes[left_index]
        right_index = 2*i+2
        if right_index < n:
            nodes[i].right = nodes[right_index]
    return nodes[0]


def layer_traverse(root):
    layer_index = 1
    temp = [root]
    while True:
        temp2 = []
        break_flag = True
        print()
        print(f'layer index {layer_index}', end=': \t')
        while temp:
            node = temp.pop(0)
            if not node:
                print('null', end=', ')
            else:
                print(node.val, end=', ')
                temp2.append(node.left)
                temp2.append(node.right)
                if node.left or node.right:
                    break_flag = False
        if break_flag:
            break
        temp = temp2[:]
        layer_index += 1


# 非递归 中序遍历
def inorderTraversal(root):
    result = []
    if not root:
        return []
    stack = []
    while root:
        stack.append(root)
        root = root.left
    while stack:
        node = stack.pop()
        result.append(node.val)
        root = node.right
        while root:
            stack.append(root)
            root = root.left
    return result


# 非递归 后序遍历
def postorderTraversal(root):
    stack1 = []
    stack2 = []
    result = []
    stack1.append(root)
    while stack1:
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        stack2.append(node)
    while stack2:
        node = stack2.pop()
        result.append(node.val)
    return result


def postorderTraversal2(root):
    if not root:
        return []
    stack1 = []
    stack2 = []
    result = []
    stack1.append(root)
    while stack1:
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        result.append(node.val)
    return result[::-1]


if __name__ == '__main__':
    root = build_tree(8)
    # root.left.right = None
    layer_traverse(root)