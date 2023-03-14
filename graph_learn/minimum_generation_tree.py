from queue import PriorityQueue
from graph_learn.graph_utlis import *


# 最小生成树 普里姆算法
def prim(nodes_dict, edges_dict):
    results = []
    visited = set()
    edges_visited = set()
    q = PriorityQueue()

    # 检查边未出现过
    def check_edge_not_visited(edge):
        if (edge.fromm, edge.to) not in edges_visited and (edge.to, edge.fromm) not in edges_visited:
            return True
        else:
            return False
    # 随机选择一个节点
    for value, node in nodes_dict.items():
        if node not in visited:
            visited.add(node)
            for edge in node.edges:
                if check_edge_not_visited(edge):
                    edges_visited.add((edge.fromm, edge.to))
                    q.put((edge.weight, edge))

            # 初始化出发点的的边集 完毕
            while not q.empty():
                weight, edge = q.get()
                # print(edge.fromm.value, edge.to.value, edge.weight)
                next_node = edge.to
                if next_node not in visited:
                    results.append((edge.fromm.value, edge.to.value))

                    visited.add(next_node)
                    for next_edge in next_node.edges:
                        if check_edge_not_visited(next_edge):
                            # print('not visited', next_edge.fromm.value, next_edge.to.value, next_edge.weight, next_edge)
                            edges_visited.add((next_edge.fromm, next_edge.to))
                            q.put((next_edge.weight, next_edge))
                # print(q.qsize())
    for edge in results:
        print(edge[0]+','+edge[1], end='\t\t')


# 最小生成树 克鲁斯卡尔算法
def k(nodes_dict, edges_dict):
    edge_visited = set()
    node_set_dict = {}
    for node_index, node in nodes_dict.items():
        node_set_dict[node] = []
        node_set_dict[node].append(node)

    def is_same_set(node_from, node_to):
        node_from_set = node_set_dict[node_from]
        node_to_set = node_set_dict[node_to]
        return node_from_set == node_to_set

    def union_two_set(node_from, node_to):
        node_from_set = node_set_dict[node_from]
        node_to_set = node_set_dict[node_to]
        for node in node_to_set:
            node_from_set.append(node)
        for node in node_from_set:
            node_set_dict[node] = node_from_set

    q = PriorityQueue()
    for edge_index, edge in edges_dict.items():
        q.put((edge.weight, edge))
    results = []
    while not q.empty():
        weight, edge = q.get()
        if (edge.fromm.value, edge.to.value) not in edge_visited:
            if not is_same_set(edge.fromm, edge.to):
                results.append((edge.fromm.value, edge.to.value))
                union_two_set(edge.fromm, edge.to)
            edge_visited.add((edge.fromm.value, edge.to.value))
            edge_visited.add((edge.to.value, edge.fromm.value))

    for edge in results:
        print(edge[0]+','+edge[1], end='\t\t')

if __name__ == '__main__':
    graph = [
        ['a', 'b', 10],
        ['a', 'c', 8],
        ['a', 'd', 5],
        ['b', 'd', 3],
        ['c', 'd', 2],
        ['b', 'e', 2],
        ['d', 'e', 10]
    ]
    nodes, edges = init_graph_with_weight(graph)
    prim(nodes, edges)



