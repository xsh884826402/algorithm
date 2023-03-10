def bubble_sort(nums):
    lenn = len(nums)
    if lenn == 0 or lenn == 1:
        return nums
    for l in range(lenn, 0, -1):
        for index in range(0, l-1, 1):
            if nums[index] > nums[index+1]:
                nums[index], nums[index+1] = nums[index+1], nums[index]
    return nums


nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
nums2 = [7, 8, 9, 4, 5, 6, 1, 2, 3]

print(bubble_sort(nums2))
