# leetcode 215题
def findKthLargest(self, nums: List[int], k: int) -> int:
    l = 0
    r = len(nums)-1
    index = partition(nums, l, r)
    while index != len(nums)-k:
        if index < len(nums)-k:
            l = index+1
            index = partition(nums, l, r)
        else:
            r = index-1
            index = partition(nums, l, r)
    return nums[index]


def partition(nums, l, r):
    target = nums[l]
    l_index = l
    r_index = r
    while l_index <= r_index:
        # 找到最右侧小于等于target的数
        while l_index <= r_index and nums[r_index] > target:
            r_index -= 1

        # 找到最左侧大于target的数
        while l_index <= r_index and nums[l_index] <= target:
            l_index += 1
        if l_index <= r_index:
            swap(nums, l_index, r_index)

    swap(nums, r_index, l)
    return r_index


def swap(nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]