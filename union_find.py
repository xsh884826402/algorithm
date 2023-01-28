class UnionFind:
    def __init__(self):
        self.father_dict = {}
        self.count_dict = {}

    def find_father(self, x):
        # 路径压缩优化
        if self.father_dict[x] != x:
            self.father_dict[x] = self.find_father(self.father_dict[x])
        return self.father_dict[x]

    def union(self, x, y):
        # 根据大小进行优化
        x_father = self.find_father(x)
        y_father = self.find_father(y)
        big_father = x_father if self.count_dict[x_father] > self.count_dict[y_father] else y_father
        small_father = x_father if big_father ==y_father else y_father

        # 更新并查集
        self.father_dict[small_father] = big_father
        self.count_dict[big_father] += self.count_dict[small_father]

    def is_same(self, x, y):
        return self.find_father(x)==self.find_father(y)

    def add(self, x):
        if x not in self.father_dict.keys():
            self.father_dict[x] = x
            self.count_dict[x] = 1

# leetcode 547 省份数量
def findCircleNum(nums):
    unionFind = UnionFind()
    n = len(nums)
    result = n
    for i in range(n):
        unionFind.add(i)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i][j] == 1:
                if not unionFind.is_same(i, j):
                    unionFind.union(i, j)
                    result -= 1
    return result


if __name__ == '__main__':
    nums = [[1,1,1],[1,1,1],[1,1,1]]

    print(findCircleNum(nums))