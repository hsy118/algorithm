T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    sum_max = 0
    sum_min = 0
    sum_max = arr[0] + arr[1]
    sum_min = arr[0] + arr[1]
    for i in range(0, len(arr)-1):
        if sum_max < (arr[i] + arr[i+1]):
            sum_max = arr[i] + arr[i+1]
        elif sum_min > (arr[i] + arr[i+1]):
            sum_min = arr[i] + arr[i+1]

    print(f'#{test_case} {sum_max} {sum_min}')


