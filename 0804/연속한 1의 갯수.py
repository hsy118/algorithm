T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    cnt = 0
    max_cnt = 0
    for i in range(0, len(arr)):
        if arr[i] == 1:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt

        elif arr[i] == 0:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 0

        # elif arr[i] == 0:
        #     cnt = 0

    print(f'#{test_case} {max_cnt}')
