n = int(input())

pttn_box = [1,1,1]

for i in range(4, 10001):
    num = 1
    for j in range(2,i+1):
        if i % j == 0:
            num += 1
    if num % 2 == 0:
        pttn_box.append(num//2)
    else:
        pttn_box.append((num//2)+1)

Sum = 0
for i in range(n):
    Sum += pttn_box[i]

print(Sum)