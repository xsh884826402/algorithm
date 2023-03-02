def find(nodes, matrix):

    res = 0
    visited = set()
    def dfs(node):
        global res
        if node not in visited:
            visited.add(node)
            for index, next_node in enumerate(matrix[node]):
                if next_node == 1 and index not in visited:
                    dfs(index)
    for node in range(nodes):
        if node not in visited:
            res += 1
            dfs(node)
    return res


if __name__ == '__main__':
    # nodes = 5
    # matrix = [[0, 1, 1, 0, 0],
    #           [1, 0, 1, 0, 0],
    #           [1, 1, 0, 0, 0],
    #           [0, 0, 0, 0, 1],
    #           [ 0, 0, 0, 1, 0],
    #           ]
    nodes = 7
    matrix = [[0, 1, 0, 0, 0, 1, 0],
              [1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 0, 0],
              [0, 0, 1, 0, 1, 0, 0],
              [0, 0, 1, 1, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 1, 0]
              ]
    print(find(nodes, matrix))