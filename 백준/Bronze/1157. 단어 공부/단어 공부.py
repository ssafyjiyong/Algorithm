lst = [0]*100
a = str(input()).upper()

flag = 0

for i in a:
    lst[ord(i)] += 1

Mx = -21e8
Mx_idx = 21e8
for i in range(len(lst)):
    if lst[i] > Mx:
        Mx = lst[i]
        Mx_idx = i

for i in range(Mx_idx+1,len(lst)):
    if lst[i] == Mx:
        flag = 1
        print('?')
        break

if flag == 0:
    print(chr(Mx_idx))


