T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    num = int(input())

    count_list = [0] * 10
    for i in range(0, N):
        count_list[num % 10] += 1
        num = num // 10

    max = count_list[0]
    for i in range(0, len(count_list)):
        if max <= count_list[i]:
            max = count_list[i]

    max_index = count_list.index(max)
    for i in range(9, -1, -1):
        if count_list[i]  == max:
            max_index = i
            break



    print(f'#{test_case} {max_index} {max}')
