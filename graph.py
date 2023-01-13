from queue import PriorityQueue

# 节点
class Node:
    def __init__(self, value ):
        self.value = value
        self.nexts = set()
        self.edges = set()


# 边
class Edge:
    def __init__(self, fromm, to, weight):
        self.fromm = fromm
        self.to = to
        self.weight = weight

    def __gt__(self, other):
        a = self.fromm.value + self.to.value
        b = other.fromm.value + other.to.value
        return a > b


def init_graph():
    graph = [['a', 'b'],
             ['a', 'c'],
             ['a', 'd'],
             ['c', 'e']]


def init_graph_with_weight(graph):
    nodes_dict = {}
    edges_dict = {}
    for line in graph:
        node1, node2, weight = line
        # 创建点
        if node1 not in nodes_dict:
            nodes_dict[node1] = Node(node1)
        if node2 not in nodes_dict:
            nodes_dict[node2] = Node(node2)

        # 创建边
        if (node1, node2) not in edges_dict:
            edges_dict[(node1, node2)] = Edge(nodes_dict[node1], nodes_dict[node2], weight)
        if (node2, node1) not in edges_dict:
            edges_dict[(node2, node1)] = Edge(nodes_dict[node2], nodes_dict[node1], weight)

        nodes_dict[node1].nexts.add(node2)
        nodes_dict[node1].edges.add(edges_dict[(node1, node2)])

        nodes_dict[node2].nexts.add(node1)
        nodes_dict[node2].edges.add(edges_dict[(node2, node1)])

    # for key, value in edges_dict.items():
    #     print(value.fromm.value, value.to.value, value.weight)
    return nodes_dict, edges_dict


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
                print(edge.fromm.value, edge.to.value, edge.weight)
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
def k():
    pass


# 迪杰斯特拉算法
def d(node):
    # 构造距离dict
    distance_dict = dict()
    nodes_visited = set()

    distance_dict[node] = 0
    nodes_visited.add(node)

    def find_next_node():
        for key, value in distance_dict.items():
            print(key.value, value, end='***')
        print()
        node_distance_tuple = [[key, value] for key, value in distance_dict.items()]
        node_distance_tuple_sorted = sorted(node_distance_tuple, key=lambda x: x[1])
        for key, value in node_distance_tuple_sorted:
            if key not in nodes_visited:
                return key
        return None

    while node:
        # print('loop', node.value)
        for edge in node.edges:
            current_value = distance_dict[node]
            if edge.to not in nodes_visited:
                if edge.to not in distance_dict:
                    distance_dict[edge.to] = current_value + edge.weight
                else:
                    distance_dict[edge.to] = min(current_value + edge.weight, distance_dict[edge.to])

        node = find_next_node()
        nodes_visited.add(node)

    for k,v in distance_dict.items():
        print(k.value, v)


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
    # prim(nodes, edges)
    d(nodes['a'])

