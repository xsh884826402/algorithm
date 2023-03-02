a = 1000000

temp = []
y = a
result = ''

while y > 0:
    x = a % 8
    y = a // 8
    a = y
    temp.append(x)

for i in range(1, len(temp) + 1):
    result += str(temp[-i])

result = int(result)
print(result)