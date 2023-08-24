C, R = map(int, input().split())
K = int(input())

seat = [[0]*C for _ in range(R)]
num = 1

# 상하좌우 입력에 필요한 변수 각각 지정
i_start = 0
i_end = R
j1 = 0

j_start = 0
j_end = C
i1 = R - 1

i_start1 = R - 1
i_end1 = -1
j2 = C - 1

j_start1 = C - 1
j_end1 = 0
i2 = 0

# 상하좌우로 채워넣기
while num <= C*R:
    # 아래
    for i in range(i_start, i_end):
        if seat[i][j1] == 0:
            seat[i][j1] = num
            num += 1
    i_start += 1
    i_end -= 1
    j1 += 1

    # 오른쪽
    for j in range(j_start, j_end):
        if seat[i1][j] == 0:
            seat[i1][j] = num
            num += 1
    j_start += 1
    j_end -= 1
    i1 -= 1

    # 위

    for i in range(i_start1, i_end1, -1):
        if seat[i][j2] == 0:
            seat[i][j2] = num
            num += 1
    i_start1 -= 1
    i_end1 += 1
    j2 -= 1

    # 왼쪽

    for j in range(j_start1, j_end1, -1):
        if seat[i2][j] == 0:
            seat[i2][j] = num
            num += 1
    j_start1 -= 1
    j_end1 += 1
    i2 += 1

flag = 0
for i in range(R):
    for j in range(C):
        if seat[i][j] == K:
            print(f'{j+1} {i+1}')
            flag = 1
if flag == 0:
    print(0)
