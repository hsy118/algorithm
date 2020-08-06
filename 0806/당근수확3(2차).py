"""
1번 영역의 오른쪽 아래가 i,j
3개의 영역이 유지되기위한 i,j의 범위 최소 1칸
i,j를 결정하면 2,3번의 영역을 정항수 있음
"""

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 이 i
    arr = [list(map(int, input().split())) for i in range(N)]

    # for i in range(N):
    #     for j in range(M):
    #         total += arr[i][j]
    minV = 100000
    for i in range(N - 1):
        for j in range(M - 1):
            sec1 = sec2 = sec3 = 0
            for x in range(i + 1):
                for y in range(j + 1):
                    sec1 += arr[x][y]
            for x in range(i + 1):
                for y in range(j + 1, M):
                    sec2 += arr[x][y]
            for x in range(i + 1, N):
                for y in range(M):
                    sec3 += arr[x][y]

            if (max(sec1, sec2, sec3) -min(sec1, sec2, sec3)) < minV:
                minV = (max(sec1, sec2, sec3) -min(sec1, sec2, sec3))
    print(f"#{tc} {minV}")
            # if (abs(s1 - s2) + abs(s2 - s3) + abs(s3 - s1)) / 2 < minV:
            #     minV = (abs(s1 - s2) + abs(s2 - s3) + abs(s3 - s1)) // 2
