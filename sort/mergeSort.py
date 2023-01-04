def mergeSort(nums, l, r):
    if l == r or l == r-1:
        return
    m = l+(r-l)//2
    mergeSort(nums, l, m)
    mergeSort(nums, m+1, r)
    merge(nums, l, m, r)


def merge(nums, l, m, r):
    copy = nums[:]
    lindex = l
    rindex = m+1
    index = l
    while lindex <= m and rindex <= r:
        if nums[lindex]<=nums[rindex]:
            copy[index] = nums[lindex]
            index += 1
            lindex += 1
        else:
            copy[index]= nums[rindex]
            index += 1
            rindex +=1
    while lindex <= m:
        copy[index] = nums[lindex]
        index += 1
        lindex += 1
    while rindex <=r:
        copy[index ]= nums[rindex]
        index += 1
        rindex += 1


nums1 = [7, 6, 5, 4, 3, 2, 1]
mergeSort(nums1, 0, len(nums1)-1)
print(nums1)

nums2 = [4, 4, 4]
mergeSort(nums2, 0, len(nums2)-1)
print(nums2)