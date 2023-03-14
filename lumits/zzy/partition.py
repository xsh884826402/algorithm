def partition(nums, lower, upper):
    x = nums[lower]
    split = lower
    for index in range(lower+1, upper+1):
        if nums[index] < x:
            split = split + 1
            nums[split], nums[index] = nums[index], nums[split]
    nums[split], nums[lower] = nums[lower], nums[split]
    return split


def quicksort(nums, lower, upper):
    if lower < upper:
        index = partition(nums, lower, upper)
        # print(nums, index)
        quicksort(nums, lower, index-1)
        quicksort(nums, index+1, upper)


def partition2(strs, permutaion,  lower, upper):
    xs = permutaion[lower]
    xp = permutaion[lower]
    split = lower
    for index in range(lower+1, upper+1):
        if permutaion[index] < xp:
            split = split + 1
            permutaion[split], permutaion[index] = permutaion[index], permutaion[split]
            strs[split], strs[index] = strs[index], strs[split]
    strs[split], strs[lower] = strs[lower], strs[split]
    permutaion[split], permutaion[lower] = permutaion[lower], permutaion[split]
    return split


def quicksort2(strs, permutation, lower, upper):
    if lower < upper:
        index = partition2(strs, permutation, lower, upper)
        quicksort2(strs, permutation, lower, index-1)
        quicksort2(strs, permutation, index+1, upper)

if __name__ == '__main__':
    # nums = [18, 15, 3, 4, 24, 26]
    # quicksort(nums, 0, len(nums)-1)
    # print(nums)
    strs = ['a', 'b', 'c', 'd', 'e']
    permutation = [5, 2, 1, 3, 4]
    quicksort2(strs, permutation, 0, len(strs)-1)
    print(strs)