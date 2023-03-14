# 利用队列来实现
from queue import Queue
from graph_learn.graph_utlis import *


def bfs(node):
    if not node:
        return
    queue = Queue()
    visited = set()
    queue.put(node)
    visited.add(node)
    while not queue.empty():
        tmp = queue.get()
        print(tmp.value)
        for next in tmp.nexts:
            if next not in visited:
                visited.add(next)
                queue.put(next)

def bfs2(root):
    q = Queue()
    visited = set()
    q.put(root)
    while q:
        tmp = q.get()
        if tmp not in visited:
            print(tmp.value)
            # 具体问题具体调整
            for next in tmp.nexts:
                q.put(next)
            visited.add(tmp)


if __name__ == '__main__':
    graph = [
        ['a', 'b', 10],
        ['b', 'c', 4],
        ['a', 'd', 2],
        ['d', 'e', 10]
    ]
    nodes, edges = init_graph_with_weight(graph)
    print([ node for node in nodes])
    bfs2(nodes['a'])