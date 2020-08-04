"""
minV = 큰 수 구역중 가장
for i in range(0, N-2):
    a = 0부터 i까지의 당근 개수 - b =  i+1 부터 N-1까지의 당근 개수    의 최소값
    if minV > abs(a-b):
        minV = abs(a-b)

i 가 한칸씩 가면서 칸을 나누는데
left += 한칸씩 더하고
right = 전체 합 - left

"""
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    total = sum(arr)
    where_i = 0
    minV = 500
    for i in range(0, N-1):
        left = sum( arr[0: i+1] )
        right = total - left
        balance = abs(left-right)
        if minV >= balance:
            minV = balance
            where_i = i + 1

    print(f'#{test_case} {where_i} {minV}')
