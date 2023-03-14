def solution(nums):
    l = 0
    r = len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] > nums[0]:
            l = mid+1
        else:
            r = mid-1
    return nums[r+1]


def solution2(nums, target):
    # 寻找目标target值 并返回下标
    l = 0
    r = len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > nums[0]:
            # 落在左侧
            if nums[mid]<target:
                l = mid + 1
            else:
                if target > nums[0]:
                    r = mid -1
                else:
                    l = mid +1
        else:
            # 落在右侧
            if nums[mid]>target:
                r = mid - 1
            else:
                if target > nums[0]:
                    r = mid-1
                else:
                    l = mid+1
    return -1


def solution3(nums, target):
    # 寻找目标target值 并返回下标
    l = 0
    r = len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[0]:
            # 落在左侧
            if nums[mid]<target:
                l = mid + 1
            else:
                if target >= nums[0]:
                    r = mid -1
                else:
                    l = mid +1
        else:
            # 落在右侧
            if nums[mid]>target:
                r = mid - 1
            else:
                if target >= nums[0]:
                    r = mid-1
                else:
                    l = mid+1
    return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    nums = [4, 5, 6, 7, 1, 2, 3]
    nums1= [1,3]
    # print(solution(nums))
    # print(solution2(nums, 3))
    print(solution3([1, 3], 1))
    print(solution3([1, 3, 5], 1))