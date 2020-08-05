# 비트 연산
"""
arr = [1,2,3]
N = len(arr)
for i in range(1<<N):   #(2 ** n)
    for j in range(N):
        if i & (1 << j):
            print(arr[j], end= ",")
    print()
print()
"""
T = int(input())
for tc in range(1, T+1):
    arr =list(map(int, input().split()))
    ans = 0

    for i in range(1, 1 << 10):
        s= 0
        for j in range(10):
            if (i & (1 << j)) != 0:
                s += arr[j]
        if s ==0:
            ans =1
            break
    print(f'#{tc} {ans}')

