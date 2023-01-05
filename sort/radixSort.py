def radixSort(nums):
    maxDigits = findDigits(nums)
    # ii变量 取名不合适 ，最好有对应的意义，不然i容易重用，这里如果用i，下面for i in range(1, len(count)): 会重置i的值
    for ii in range(maxDigits):
        count = [0] * (10)
        help = [0] * len(nums)
        for num in nums:
            index = get_number_digit(num, ii)
            # print('num', num, index)
            count[index] += 1
        for i in range(1, len(count)):
            count[i] = count[i]+count[i-1]
        for num in nums[::-1]:
            index = get_number_digit(num, ii)
            # print('num', num, 'index', index)
            help[count[index]-1] = num
            count[index] -= 1
        nums = help[:]
        # break
    print('final', nums)
    return nums



def findDigits(nums):
    count = 0
    max_value = max(nums)
    while max_value !=0:
        max_value //= 10
        count += 1
    return count


def get_number_digit(num, i):
    # 356 0
    num = num // 10**i
    num = num % 10
    return num
# Test case
nums = [1, 200, 304, 5, 68, 43]
print(radixSort(nums))
print(id(nums), nums)


