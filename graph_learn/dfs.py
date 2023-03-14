# 利用栈来实现
from graph_learn.graph_utlis import *


def dfs(node):
    if not node:
        return
    stack = []
    visited = set()
    stack.append(node)
    visited.add(node)
    while stack:
        tmp = stack.pop()
        print(tmp.value)
        for next in tmp.nexts:
            if next not in visited:
                visited.add(next)
                stack.append(next)

def dfs2(root):
    stack = []
    visited = set()
    stack.append(root)
    visited.add(root)
    while stack:
        tmp = stack.pop()
        print(tmp.value)
        for next in tmp.nexts:
            if next not in visited:
                stack.append(next)
                visited.add(next)


if __name__ == '__main__':
    graph = [
        ['a', 'b', 10],
        ['b', 'c', 4],
        ['a', 'd', 2],
        ['d', 'e', 10]
    ]
    nodes, edges = init_graph_with_weight(graph)
    dfs2(nodes['a'])