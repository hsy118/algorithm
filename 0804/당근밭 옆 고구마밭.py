T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    sum = 0
    count = 0
    sum_list = []
    for i in range(0, N):
        sum += arr[i]
        if i == N-1:
            if arr[i] < arr[i-1]:
                sum_list.append(sum)

            elif arr[i] > arr[i-1]:
                sum += arr[i]
                sum_list.append(sum)
                count += 1

        elif arr[i] > arr[i+1]:
            if arr[i] > arr[i-1]:
                sum_list.append(sum)
                sum = 0
                count += 1

            elif arr[i] < arr[i-1]:
                sum = 0



    print(f'#{test_case} {count} {max(sum_list)}')
