st = 'abababcdabcd'
st = 'faaacabcddcbabcddcbedfgaac'
st_need = ''
for right in range(1,len(st)+1):
    left = 0
    while(left<right):
        middle = (left+right)//2
        if st[left:middle]==st[middle:right]:
            if len(st[left:right]) > len(st_need):
               st_need = st[left:right]
        left+=1
print(st_need)