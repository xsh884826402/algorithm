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


def morris_traverse(root):
    mostright = None
    while root:
        #寻找左子树最右边界
        left = root.left
        if not left:
            print(root.val, end=', ')
            root = root.right
        else:
            mostright = left

            while mostright.right and mostright.right != root:
                mostright = mostright.right

            # 如果是第一次访问
            if mostright.right != root:
                mostright.right = root
                root = root.left
            else:
                mostright.right = None
                print(root.val, end=', ')
                root = root.right


if __name__ == '__main__':
    root = build_tree(8)
    # root.left.right = None
    morris_traverse(root)