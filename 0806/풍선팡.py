T = int(input())
for tc in range(1, T+1):
    I, J = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(I)]

    di = [-1,0,1,0]
    dj = [0,1,0,-1]
    dir = 0
    sum_list = []
    sum = 0
    for i in range(I):
        for j in range(J):
            value = arr[i][j]
            sum = value
            for k in range(1, value+1):
                for l in range(4):
                    ni = i + (k * di[dir])
                    nj = j + (k * dj[dir])
                    if 0 <= ni < I and 0 <= nj < J:
                        sum += arr[ni][nj]
                        dir = (dir + 1) % 4
                    else:
                        dir = (dir + 1) % 4
            sum_list.append(sum)
            sum = 0

    print(f'#{tc} {max(sum_list)}')
