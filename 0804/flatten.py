for test_case in range(1, 11):
    trial = int(input())
    list1 = list(map(int, input().split()))

    for i in range(trial):
        list1[list1.index(max(list1))] = max(list1) - 1
        list1[list1.index(min(list1))] = min(list1) + 1

    flat = max(list1) - min(list1)
    print(f'#{test_case} {flat}')

# list1 = [100, 90, 80]
# list1[list1.index(max(list1))] = max(list1) + 1

# print(list1)