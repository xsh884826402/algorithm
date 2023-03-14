class Node:
    def __init__(self, value ):
        self.value = value
        self.nexts = set()
        self.edges = set()
        self.in_degre = 0
        self.to_degre = 0


class Edge:
    def __init__(self, fromm, to):
        self.fromm = fromm
        self.to = to
        # self.weight = weight

    def __gt__(self, other):
        a = self.fromm.value + self.to.value
        b = other.fromm.value + other.to.value
        return a > b


def init_graph(graph):
    nodes_dict = {}
    edges_dict = {}
    for line in graph:
        node1, node2 = line
        # 创建点
        if node1 not in nodes_dict:
            nodes_dict[node1] = Node(node1)
        if node2 not in nodes_dict:
            nodes_dict[node2] = Node(node2)

        # 创建边
        if (node1, node2) not in edges_dict:
            edges_dict[(node1, node2)] = Edge(nodes_dict[node1], nodes_dict[node2])
        nodes_dict[node2].in_degre += 1

        nodes_dict[node1].nexts.add(nodes_dict[node2])
        nodes_dict[node1].edges.add(edges_dict[(node1, node2)])

    return nodes_dict, edges_dict


def find_zero_in_nodes(nodes_dict):
    zero_in_nodes = []
    for node_name, node in nodes_dict.items():
        if node.in_degre == 0:
            zero_in_nodes.append(node)
    return zero_in_nodes


def find_solution(zero_in_nodes):
    while zero_in_nodes:
        node = zero_in_nodes.pop(0)
        print(node.value)
        for next in node.nexts:
            next.in_degre -= 1
            if next.in_degre == 0:
                zero_in_nodes.append(next)




if __name__ == '__main__':
    graph = [
        ['a', 'c'],
        ['a', 'd'],
        ['b', 'c'],
        ['c', 'e']
    ]
    nodes_dict, edges_dict = init_graph(graph)
    zero_in_nodes = find_zero_in_nodes(nodes_dict)
    find_solution(zero_in_nodes)