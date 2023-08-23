P = int(input())

for _ in range(P):
    lst = list(map(int, input().split()))
    tc = lst.pop(0)
    cnt = 0
    sorted_lst = [lst[0]]


    for i in range(1, 20):
        min_idx = 21e8
        flag = 0
        sorted_lst.append(lst[i])
        for j in range(len(sorted_lst)-2, -1, -1):
            if lst[i] < sorted_lst[j]:
                if min_idx > j:
                    min_idx = j

        if min_idx == 21e8:
            flag = 1

        if flag == 0:
            for _ in range(len(sorted_lst)-min_idx-1):
                sorted_lst.append(sorted_lst.pop(min_idx))
                cnt += 1

    print(tc, cnt)