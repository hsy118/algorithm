T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    if min in arr:
        min_index = arr.index(min) + 1

    print(f'#{test_case} {min_index}')
