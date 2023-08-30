T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))

    Max = 0
    count_one = 0
    for i in range(1, N):
        if lst[i] == 1 and lst[i - 1] == 1:
            count_one += 1
            if count_one > Max:
                Max = count_one
        else:
            if count_one > Max:
                Max = count_one
            count_one = 0

    if Max > 0:
        print(f'#{tc} {Max+1}')
    else:
        print(f'#{tc} 1')