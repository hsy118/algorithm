"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    sum = 0
    compare = []
    #위쪽 구역
    for i in range(N):
        for j in range(N):
            if i < j and i+j < (N-1):
                sum += arr[i][j]
    compare.append(sum)
    #3시 방
    sum = 0
    for i in range(N):
        for j in range(N):
            if i < j and i+j > (N-1):
                sum += arr[i][j]
    compare.append(sum)
    #6시 방향
    sum = 0
    for i in range(N):
        for j in range(N):
            if i > j and i + j > (N-1):
                sum += arr[i][j]
    compare.append(sum)
    #9시 방향
    sum = 0
    for i in range(N):
        for j in range(N):
            if i > j and i + j < (N-1):
                sum += arr[i][j]
    compare.append(sum)
    result = max(compare) - min(compare)
    print(f'#{tc} {result}')
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    compare = []
    section1 = 0 #12시 구역
    section2 = 0 # 3시
    section3 = 0 # 6시
    section4 = 0 # 9시
    for i in range(N):
        for j in range(N):
            if i < j and i+j < N-1:
                section1 += arr[i][j]
            elif i < j and i+ j > N-1:
                section2 += arr[i][j]
            elif i > j and i + j > N-1:
                section3 += arr[i][j]
            elif i > j and i + j < N-1:
                section4 += arr[i][j]
    result = max(section1, section2, section3, section4) - min(section1, section2, section3, section4)
    print(f'#{tc} {result}')

