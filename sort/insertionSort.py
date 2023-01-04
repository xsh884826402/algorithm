nums = []


def sort(nums):
    lenn = len(nums)
    if lenn==0 or lenn == 1:
        return nums

    for l in range(1, lenn):
        for index in range(l-1, -1, 1):
            if nums[index+1]< nums[index]:
                nums[index+1], nums[index] = nums[index], nums[index+1]
    return nums


print(sort([7, 6, 5, 4, 3, 2,1]))
# 最坏复杂度 o(n^2)
