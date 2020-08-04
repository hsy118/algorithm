T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
     #M은   # 수레 용량
    arr = [0] + list(map(int, input().split()))

    count = 0
    i = 1
    while i <=N:
        if M == arr[i] :
            arr[i] = 0
            count += (i *2)
            i += 1

        elif M < arr[i]:
            arr[i] = arr[i] - 6
            count += (i * 2)


        elif M > arr[i]:
            extra = 6 - arr[i]
            arr[i] = 0
            if extra > arr[i+1]:
                j = i
                while True:
                    extra = extra - arr[i+1]
                    arr[j+1] = 0
                    count += 1
                    j += 1
                    if j = N:
                        count += (j*2)
            arr[i+1] = arr[i+1] - extra
            #if 하나 더 붙어야함
            count += (2 * (i+1))
            i += 1

        elif i == N:
            if arr[i] > 0:
                count += (2*i)
                break
            elif arr[i] == 0:
                break

    print(f'#{test_case} {count}')