# 一个数组 一种数 出现了 奇数次，找到该数
nums = [3, 3, 4, 4, 1]
def find_num(nums):
    result = nums[0]
    for num in nums[1:]:
        result = result ^ num
    return result

# 一个数组 两种数 出现了奇数次，找到该数
nums = [3, 3, 4, 4, 1, 2]
# 易找到 x ^ y
# 找到第一个 z， z=x 或者 z=y 利用异或 轻易得到另一个
# 如何找到第一个z 因为x != y 一定在某一位上 不同时为1 需要把 x和y分开，
# 技巧 取右边第一个一 rightindex = x &(~x+1)
xor = 0
for num in nums:
    xor = xor ^ num
print(xor)
rightone = xor & (~xor+1)
print(rightone)
a = 0
for num in nums:
    if num&rightone==0:
        a ^= num




