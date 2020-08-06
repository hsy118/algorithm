T = int(input())
for tc in range(1, T+1):
    N = int(input())
    red = []
    blue = []
    for read in range(N):
        i1, j1, i2, j2, color = map(int, input().split())
        for i in range(i1, i2+1):
            for j in range(j1, j2+1):
                if color == 1:
                    red.append( (i, j) )
                elif color == 2:
                    blue.append( (i,j) )

    result = []
    if len(red) > len(blue):
        for i in blue:
            if i in red:
                result.append(i)
    if len(red) < len(blue):
        for i in red:
            if i in blue:
                result.append(i)

    print(f"#{tc} {len(result)}")
