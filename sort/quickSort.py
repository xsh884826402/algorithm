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


nums = [1, 2, 3, 5, 5, 5, 6, 7, 4, 5]
quickSort(nums, 0, len(nums)-1)
print(nums)

nums = [1, 2, 3, 5, 5, 5, 6, 7, 4, 5]
quickSort(nums, 0, len(nums)-1)
print(nums)