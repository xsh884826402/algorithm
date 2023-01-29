def kmp(s1, s2):
    # 如果s2 存在于s1中 那么返回s2首字母在s1中的索引
    i, j = 0, 0
    next = get_next(s2)
    while i<len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            if j== -1:
                i += 1
                j = 0
            else:
                j = next[j]

    print(f'i: {i}, j :{j}')
    if j== len(s2):
        return i-len(s2)
    else:
        return -1


def get_next(s):
    next = [-1]*len(s)
    next[1] = 0
    for i in range(2, len(s)):
        index = i-1
        while True:
            if index == -1:
                next[i] = 0
                break
            if s[i-1]==s[next[index]]:
                next[i] = next[index]+1
                break
            else:
                index = next[index]
    print(f'next array {next}')
    return next

if __name__ == '__main__':
    str1 = 'ababfababfababz'
    str2 = 'ababfababz'
    print(kmp(str1, str2))