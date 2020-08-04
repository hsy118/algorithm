T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    sum_list =[]
    for i in range(0, N-M+1):
        sum = 0
        for j in range(i, (i+M)):
            sum += arr[j]
        sum_list.append(sum)

    max = sum_list[0]
    min = sum_list[0]
    for i in sum_list:
        if max < i:
            max = i
        elif min > i:
            min = i

    result = max - min

    print(f'#{test_case} {result}')

