T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # arr[0]이 최대값으로 가정 maxV = arr[0]
    # 0부터 끝까지 가서, maxV랑 비교하면서 크면 바꿔라

    max = arr[0]
    for i in arr:
        if i > max:
            max = i

    # print("#" + str(test_case) + " " + str(max), end = '')
    print(f'#{test_case} {max}')



