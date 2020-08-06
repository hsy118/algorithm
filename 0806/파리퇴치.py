T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N 은 전체 , M은 파리채

    floor = [list(map(int, input().split())) for i in range(N)]
    sum = 0
    maxV = 0
    for i in range(0, (N-M+1)):
        for j in range(0, (N-M+1)):
            for a in range(i, i+M):
                for b in range(j, j+M):
                    sum += floor[a][b]

            if maxV < sum:
                maxV = sum
            sum = 0


    print(f'#{tc} {maxV}')