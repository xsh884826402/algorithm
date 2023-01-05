def swap(nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]


def sink(nums, i, heapsize):
    temp = i
    while temp < heapsize:
        left = 2*temp + 1
        if left >= heapsize:
            break
        large = left
        if left + 1 < heapsize and nums[left + 1] > nums[left]:
            large = left + 1
        if nums[large] > nums[temp]:
            swap(nums, temp, large)
            temp = large
        else:
            break


def init(nums):
    for i in range(len(nums)-1, -1, -1):
        sink(nums, i, len(nums))


def swam():
    pass

def heapSort(nums, heapsize):
    init(nums)
    while heapsize > 0:
        swap(nums, 0, heapsize-1)
        heapsize -= 1
        sink(nums, 0, heapsize)

# Test case
nums = [1, 2, 3, 4, 5, 6, 7]
heapSort(nums, len(nums))
print(nums)

nums = [1, 2, 3, 5, 5, 5, 6, 7, 4, 5]
heapSort(nums, len(nums))
print(nums)