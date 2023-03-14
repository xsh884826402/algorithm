class Node:
    def __init__(self, value ):
        self.value = value
        self.nexts = set()
        self.edges = set()


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

        nodes_dict[node1].nexts.add(nodes_dict[node2])
        nodes_dict[node1].edges.add(edges_dict[(node1, node2)])

        nodes_dict[node2].nexts.add(nodes_dict[node1])
        nodes_dict[node2].edges.add(edges_dict[(node2, node1)])

    # for key, value in edges_dict.items():
    #     print(value.fromm.value, value.to.value, value.weight)
    return nodes_dict, edges_dict


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


