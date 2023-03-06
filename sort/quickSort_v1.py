def quickSort(nums, l, r):
    if l <= r:
        index = partation(nums, l, r)
        quickSort(nums, l, index-1)
        quickSort(nums, index+1, r)


def partation(nums, l, r):
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


nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
nums2 = [7, 8, 9, 4, 5, 6, 1, 2, 3]
quickSort(nums1, 0, len(nums1)-1)
print(nums1)