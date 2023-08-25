T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    rotated_arr = list(zip(*arr))
    cnt = 0
    result_arr = []

    for i in range(100):
        for j in range(100):
            if rotated_arr[i][j] != 0:
                result_arr.append(rotated_arr[i][j])
        result_arr.append(0)

    for i in range(len(result_arr)-1):
        if result_arr[i] == 1 and result_arr[i+1] == 2:
            cnt += 1

    print(f'#{tc} {cnt}')