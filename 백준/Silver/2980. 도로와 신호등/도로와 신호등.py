N, L = map(int, input().split())
sign_info = [list(map(int, input().split())) for _ in range(N)]

ans = L
delay = 0

for i in range(N):
    if(sign_info[i][0] + delay) % (sign_info[i][1] + sign_info[i][2]) < sign_info[i][1]:
        ans += sign_info[i][1] - (sign_info[i][0] + delay) % (sign_info[i][1] + sign_info[i][2])
        delay += sign_info[i][1] - (sign_info[i][0] + delay) % (sign_info[i][1] + sign_info[i][2])
    else:
        if (sign_info[i][0] + delay) % (sign_info[i][1] + sign_info[i][2]) == 0:
            ans += sign_info[i][1]
            delay += sign_info[i][1]

        if sign_info[i][1] > (sign_info[i][0] + delay) % (sign_info[i][1] + sign_info[i][2]):
            ans += sign_info[i][2] -((sign_info[i][0] + delay) % (sign_info[i][1] + sign_info[i][2])) - sign_info[i][1]
            delay += sign_info[i][2] -((sign_info[i][0] + delay) % (sign_info[i][1] + sign_info[i][2])) - sign_info[i][1]

print(ans)
