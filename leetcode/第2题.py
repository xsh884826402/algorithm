import collections


def find(m, n , map):
    path_dict = collections.defaultdict(list)
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = map[0][0]
    path_dict[(0,0)] = [(0, 0)]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1]+map[0][i]
        path_dict[(0, i)] = path_dict[(0, i - 1)] + [(0, i)]

    for i in range(1, m):
        dp[i][0] = dp[i-1][0]+map[i][0]
        path_dict[(i, 0)] = path_dict[(i-1, 0)] + [(i, 0)]

    for i in range(1, m):
        for j in range(1, n):
            if dp[i][j-1]>dp[i-1][j]:
                path_dict[(i, j)] = path_dict[(i,j-1)]+[(i, j)]
            else:
                path_dict[(i, j)] = path_dict[(i-1,j)]+[(i, j)]
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])+map[i][j]
    return dp[m-1][n-1], path_dict[(m-1, n-1)]
# m = 3
# n = 3
# map = [[1, 4, 3],
#        [2, 3,1],
#        [2, 3, 4]]
m = 5
n = 5
map = [[1, 1, 1, 1, 2],
        [2, 3, 4, 1, 4],
       [3, 1, 4, 2, 4,],
[2, 1, 5, 7, 2],
[4, 3, 3, 4, 5]]
res, path = find(m,n,map)
print(res)
for item in path:
    print(map[item[0]][item[1]], end=' ')
