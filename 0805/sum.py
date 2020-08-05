"""
오른쪽으로 M
아래로 N 인 사각형
maxV = 0
for i in range(N):
    sum = 0
    for j in range(N):
        sum += A[i][j]
    if maxV < sum:
        maxV = sum
print(maxV)
"""
"""
for 돌면서 맥스 값 비교 - 행
또 돌면서 맥스값 비교  - 열
또 돌고 맥스값 비교 - 대각선 두
"""

for tc in range(1, 11):
    test_case = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    maxV = 0
    #열의 합
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        if maxV < sum:
            maxV = sum

    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[j][i]
        if maxV < sum:
            maxV = sum

    for i in range(100):
        sum = 0
        for j in range(100):
            if i == j:
                sum += arr[i][j]
        if maxV < sum:
            maxV = sum

    for i in range(100):
        sum = 0
        for j in range(100):
            if (i+j) == 99:
                sum += arr[i][j]
        if maxV < sum:
            maxV = sum

    print(f'#{test_case} {maxV}')

