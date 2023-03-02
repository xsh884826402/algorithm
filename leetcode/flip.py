import copy
# 输入数据为board
# board = [[0, 0, 1, 0, 0, 0],
#             [0, 1, 1, 1, 0, 1],
#             [0, 0, 1, 0, 1, 1]]

# board = [[1, 1, 1, 0, 1, 1],
#          [0, 1, 0, 1, 0, 0]]

board = [[0, 1, 1, 0, 1, 0],
         [1, 0, 0, 1, 1, 1],
         [0, 0, 1, 0, 0, 1],
         [1, 0, 0, 1, 0, 1],
         [0, 1, 1, 1, 0, 0],
         ]
m = len(board)
n = len(board[0])
# tra = [[0]*n for _ in range(m)]
# ans = [[0]*n for _ in range(m)]
dir = [(0, 0), (1, 0), (-1,0), (0,1),(0,-1)]


def get(x, y):
    c = board[x][y]
    for i in range(5):
        xx = x+dir[i][0]
        yy = y+dir[i][1]
        if xx>=0 and xx<m and yy>=0 and yy<n:
            c += tra[xx][yy]
    return c%2


def dfs(tra):
    for i in range(1, m):
        for j in range(n):
            if get(i-1, j)==1:
                # print(f'get {i-1}, {j}, {get(i-1, j)}')
                tra[i][j] = 1
    for i in range(n):
        if get(m-1,i)==1:
            return 100
    return sum([sum(tra[i]) for i in range(m)])


if __name__ == '__main__':
    res = 100
    # 遍历第一行所有情况
    for i in range(1<<n):
        tra = [[0] * n for _ in range(m)]
        for j in range(n):
            tra[0][j] = i>>(n-(j+1)) & 1
        tmp_res = dfs(tra)
        if tmp_res < res:
            res = tmp_res
            ans = copy.deepcopy(tra)
    if res==100:
        print('无结果')
    else:
        for i in range(m):
            for j in range(n):
                print(ans[i][j], end=' ')
            print()

