T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    list1 = list(map(int, input().split()))

    max = list1[0]
    for i in list1:
        if i > max:
            max = i

    carrot = list1.index(max) + 1

    print(f'{test_case} {carrot} {max}')
