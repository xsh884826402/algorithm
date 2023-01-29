def longest_palindromic(s):
    # 添加特殊字符# 以便统一处理奇数回文和偶数回文
    s = transform(s)
    array = [1]*len(s)
    r = -1
    c = -1
    for i in range(len(s)):
        if i >= r:
            length = 0
            while i+length < len(s) and i-length >= 0 and s[i+length]==s[i-length]:
                length += 1
            length -= 1
            if i+length > r:
                c = i
                r = i+length
            # print(f'debug1 {length}')
            array[i] = length + 1
        else:
            i_prime = 2*c-i
            l = 2*c-r
            if i_prime-l+1 > array[i_prime]:
                array[i] = array[i_prime]
            elif i_prime-l+1 < array[i_prime]:
                array[i] = r-i+1
            else:
                length = r-i
                while i + length < len(s) and i - length >= 0 and s[i + length] == s[i - length]:
                    length += 1
                length -= 1
                if i + length > r:
                    c = i
                    r = i + length
                # print('debug 2')
                array[i] = length + 1
    max_length = max(array)
    # 剔除#
    for i in range(len(array)):
        if array[i]==max_length:
            result = s[i-max_length+1:i+max_length]
            result= result.replace('#', '')
            return result


def transform(s):
    temp = ''
    for c in s:
        temp += '#'+c
    temp += '#'
    return temp


if __name__ == '__main__':
    print(longest_palindromic('babaa'))
