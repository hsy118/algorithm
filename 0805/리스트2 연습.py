"""
      i     j
오른쪽  0     1
아래   1     0
왼쪽   0     -1
위    -1     0

di = [0,1,0,-1]
dj = [1, 0 ,-1, 0]

for
    for
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <ni N N and o N= nj N N

"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    sum = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sum += abs( arr[i][j] - arr[ni][nj] )
    print(f'{tc} {sum}')

