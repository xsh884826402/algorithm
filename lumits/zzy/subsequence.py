def find_subsequnce(nums, n):
    l = 1
    r = n-1
    while l < r:
        if nums[l] == 'b':
            if nums[l-1]=='a':
                return True
            else:
                l += 1
        if nums[r] =='a':
            if nums[r+1]=='b':
                return True
            else:
                r -= 1
    mid = l
    if nums[mid]=='a':
        if nums[mid+1]=='b':
            return True
    else:
        if nums[mid-1]=='a':
            return True
    return False

# 核心思路 通过左指针去寻找最右侧的b，通过右指针寻找最左侧的a，
# 判断是否出现substr 'ab', 任何时刻 发现substr'ab' ,返回True； 否则返回False

# 伪代码
#    Input: L sequeence, n the length of sequence L
# #    Outpt: Bool True or False
#      l := 2
#      r := n-1
#     while l < r:
#         if L[l]=='b' then
#                 if L[l-1]=='a' then return True
#                 else l += 1
#         if L[r]=='a' then
#                 if L[r+1] == 'b' then return True
#                 else r -= 1
#
#     endwhile
#     mid := l
#     if L[mid]=='a' then if L[mid+1]=='b' return True
#     if L[mid]=='b' then if L[mid-1]=='a' return True
#     return False
#
# 正确性证明
#   Lema：任何xxxxmxxxxn(其中m in （a,b）,n in (a,b), x为任意字符)
#   可转换为 xxxxmnxxxxx[不相邻的m和n可以转为相邻的位置]
# #   # Proof：
#         case1: xxx均为m,任何xxxxmxxxxn => xxxxmnxxxx
#         case2： xxx均为n,
#         case3: xxx同时包含m,n;
#     任何L均可转换为四种形式 xxxxaaxxxx;xxxxabxxxx;xxxxbaxxxxx;xxxxbbxxxxx
#     case1-4,我们提的算法均正确
#     可证我们的算法是正确的



# 时间复杂度分析
## worst time:(bbbbbaaaa) n-1 [bbbaa] n-2+1 n-1 T(n) = O(n)
## averge time:
    # 'aaaaabbbb'
    #     assume L contain 'ab' subsequence P,P/((n-1)/2) (not contain 1-P)
    #     key operation : I
    #     T(n) = (1-P)[时间成本]+P*[时间成本]
    #          = （1-P）


if __name__ == '__main__':
    nums = ['a', 'a', 'a', 'b', 'b']


# 思路 ：
#   维护两个指针 左指针寻找a 右指针寻找b，
    #   二者相向而行，若指针相遇时仍然未发现ab，则不存在子序列
# 正确性证明 其实共四种情况，ab，aa，ba， bb
    引理： MxxxN 最终可以转换成MN，
    这四种case都能通过我们的算法进行检测

#时间复杂度证明
最坏情况下 n-1次
平均复杂度
# 假设包含subsequence 的概率是p
# 某次出现True的概率是p/((n-1)/2)
# 算法复杂度为O(n)

