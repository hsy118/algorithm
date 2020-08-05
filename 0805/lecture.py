N = 3
M = 5
arr = [0]* N
arr2 = [[0]*N for _ in range(N)]

arrNM = [[0]*M for _ in range(N)]

k = 1
for i in range(N):
    for j in range(M):
        arrNM[i][j] = k
        k += 1
print(arrNM)

"""
왼쪽 아래에서 오른쪽 위까지 올라가는 대각선
i랑 j랑 합이 3 
3 by3 일때 N =4 
그럼 그 대각선은 j + i = (N-1)
"""
arr = list(map(int, input()))

