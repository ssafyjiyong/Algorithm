T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 배열 크기, M은 지불 가능 비용
    arr = [list(map(int, input().split())) for i in range(N)]
    Benefit = M - 1 # K가 1인 경우 최대 이익
    Max_service = 1 # K가 1인 경우 서비스 제공 받는 집 개수

    # K(범위)가 어디일 때까지 확인해야 하는가?
    for K in range(2, N+2):
        maintain_fee = K * K + (K-1) * (K-1)

        dy = [0,-1,1,0,0]
        dx = [0,0,0,-1,1]

        # K 2 단위부터해서 모든 곳을 탐색해보자
        for i in range(N):
            for j in range(N):
                # 탐색용 배열
                used = [[0]*N for _ in range(N)]
                cnt = 0
                for k in range(5):
                    ni = i + dy[k]
                    nj = j + dx[k]
                    if ni < 0 or nj < 0 or ni >= N or nj >= N:
                        continue
                    if used[ni][nj] >= 1:
                        continue
                    cnt += arr[ni][nj]
                    used[ni][nj] = 1
                if K >= 3:
                    for KK in range(K-2):
                        for p in range(N):
                            for q in range(N):
                                if used[p][q] == KK+1:
                                    for l in range(5):
                                        ni1 = p + dy[l]
                                        nj1 = q + dx[l]
                                        if ni1 < 0 or nj1 < 0 or ni1 >= N or nj1 >= N:
                                            continue
                                        if used[ni1][nj1] >= 1:
                                            continue
                                        cnt += arr[ni1][nj1]
                                        used[ni1][nj1] = KK+2

                # 탐색 완료 후 이익 계산하기
                outcome = cnt * M - maintain_fee
                if outcome >= 0 and cnt > Max_service:
                    Benefit = outcome
                    Max_service = cnt

    print(f'#{tc} {Max_service}')
