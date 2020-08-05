T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [ [0] * N for i in range(N)]

    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    direction = 0
    i = 0
    j = 0
    count = 1
    while count <= N * N:
        arr[i][j] = count
        count += 1

        ni = i + di[direction]
        nj = j + dj[direction]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i = ni
            j = nj
        else:
            direction = (direction + 1) % 4
            i += di[direction]
            j += dj[direction]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()

