def quickSort(nums, l, r):
    if l >= r:
        return
    less, more = partation(nums, l, r)
    quickSort(nums, l, less)
    quickSort(nums, more, r)


def partation(nums, l, r):
    target = nums[r]
    less = l-1
    more = r+1
    i = l
    while i < more:
        if nums[i] < target:
            less += 1
            swap(nums, i, less)
            i += 1
        elif nums[i] == target:
            i += 1
        else:
            swap(nums, i, more-1)
            more -= 1
    return less, more


def swap(nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]


nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
nums2 = [7, 8, 9, 4, 5, 6, 1, 2, 3]
quickSort(nums1, 0, len(nums1)-1)
print(nums1)


quickSort(nums2, 0, len(nums2)-1)
print(nums2)