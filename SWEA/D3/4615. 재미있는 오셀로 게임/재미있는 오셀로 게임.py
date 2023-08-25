# def othello(row, col, color):
#     board[row][col] = color # 입력 받은 위치에 돌을 놓자!!
#     stone_count[color] += 1 # 방금 놓은 돌의 갯수를 1개 증가!
#
#     # 8방향 탐색
#     dy = [-1, -1, -1, 0, 1, 1, 1, 0]
#     dx = [-1, 0, 1, 1, 1, 0, -1, -1]
#     for idx in range(8):
#         # 변경되는 돌이 있다면 해당 돌을 수집할 리스트
#         change = []
#         ni = row + dy[idx]
#         nj = col + dx[idx]
#
#         # 범위 벗어나거나 0을 만나지 않는 한 반복
#         while 1:
#             if ni < 0 or nj < 0 or ni >= N or nj >= N:
#                 break
#             if board[ni][nj] == 0:
#                 break
#             if board[ni][nj] != color:   # 다른 색의 돌이라면
#                 change.append([ni, nj])  # 현재 위치의 돌의 정보를 수집
#                 ni = ni + dy[idx]
#                 nj = nj + dx[idx]
#             else:                       # 같은 색이라면
#                 if len(change):         # 변경할 돌이 1개라도 있다면
#                     while change:
#                         r, c = change.pop()
#                         tmp = board[r][c]
#                         stone_count[tmp] -= 1    # 이전 돌의 개수를 감소
#                         board[r][c] = color      # 돌의 색을 현재 돌로 변경
#                         stone_count[color] += 1  # 현재 돌의 색을 증가
#
#                 break   # 해당 방향 탐색을 더이상 하지 않아도 되므로 반복 종료!
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # N 한 변의 길이, M 돌 놓는 횟수
#
#     # 보드 만들고 돌 4개 놓기
#     board = [[0]*N for _ in range(N)]
#     board[N//2-1][N//2-1] = 2
#     board[N//2][N//2] = 2
#     board[N//2][N//2-1] = 1
#     board[N//2-1][N//2] = 1
#
#     stone_count = [0, 2, 2] # 각 돌의 갯수를 저장하는 리스트
#
#     for _ in range(M):
#         col, row, color = map(int, input().split())
#         othello(row-1, col-1, color)
#
#     print(f'#{tc}', stone_count[1], stone_count[2])


def othello(row, col, color):
    board[row][col] = color # 입력 받은 위치에 돌을 놓자!!

    # 8방향 탐색
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    for idx in range(8):
        ni = row + dy[idx]
        nj = col + dx[idx]

        # 변경되는 돌이 있다면 해당 돌을 수집할 리스트
        change = []

        # 범위 벗어나거나 0을 만나지 않는 한 반복
        while 1:
            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                break
            if board[ni][nj] == 0:
                break

            if board[ni][nj] != color:   # 다른 색의 돌이라면
                change.append([ni, nj])  # 현재 위치의 돌의 정보를 수집
                ni = ni + dy[idx]
                nj = nj + dx[idx]
            else:                       # 같은 색이라면
                if len(change):
                    for q, p in change:
                        board[q][p] = color

                break   # 해당 방향 탐색을 더이상 하지 않아도 되므로 반복 종료!


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 한 변의 길이, M 돌 놓는 횟수

    # 보드 만들고 돌 4개 놓기
    board = [[0]*N for _ in range(N)]
    board[N//2-1][N//2-1] = 2
    board[N//2][N//2] = 2
    board[N//2][N//2-1] = 1
    board[N//2-1][N//2] = 1

    for _ in range(M):
        col, row, color = map(int, input().split())
        othello(row-1, col-1, color)

    b_cnt = w_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                w_cnt += 1
            elif board[i][j] == 1:
                b_cnt += 1

    print(f'#{tc} {b_cnt} {w_cnt}')
