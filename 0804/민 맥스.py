T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max = 0
    min = 0
    max = arr[0]
    min = arr[0]
    for i in range(0, len(arr)):
        if min > arr[i]:
            min = arr[i]
        elif max < arr[i]:
            max = arr[i]

    result = (max - min)
    print(f'#{test_case} {result}')

