N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
Mn = 21e8
b_start = []
w_start = []


for p in range(N-8+1):
    for q in range(M-8+1):
        # W 시작
        cnt = 0
        # B 시작
        cnt_B = 0
        for i in range(p, p+8):
            for j in range(q, q+8):
                # 홀수 줄에서
                if i % 2 == 1:
                    # 홀수 칸일 때
                    if j % 2 == 1:
                        if arr[i][j] == 'B':
                            cnt += 1
                        else:
                            cnt_B += 1
                    # 짝수 칸일 때
                    elif j % 2 == 0:
                        if arr[i][j] == 'W':
                            cnt += 1
                        else:
                            cnt_B += 1
                else:
                    # 홀수 칸일 때
                    if j % 2 == 1:
                        if arr[i][j] == 'W':
                            cnt += 1
                        else:
                            cnt_B += 1
                    # 짝수 칸일 때
                    elif j % 2 == 0:
                        if arr[i][j] == 'B':
                            cnt += 1
                        else:
                            cnt_B += 1
        Mn = min(cnt_B,cnt,Mn)

print(Mn)
