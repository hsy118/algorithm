T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    list1 = list(map(int, input().split()))
    count = 0
    for i in list1:
        if abs(i % 2) == 0:
            count += 1

    print(f'#{test_case} {count}')
