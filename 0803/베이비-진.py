T = int(input())
for test_case in range(1, T+1):
    num = int(input())
    C = [0] * 12

    for i in range(6):
        C[num % 10] = C[num % 10] + 1
        num //= 10

    i = 0
    tri = runn = 0
    while i < 10:
        if C[i] >=3:
            C[i] -= 3
            tri += 1

        if C[i] >= 1 and C[i+1] >= 1 and C[i+2] >= 1:
            C[i] -= 1
            C[i+1] -= 1
            C[i+2] -= 1
            runn += 1
            continue
        i += 1
    if runn + tri == 2:
        print(f'#{test_case} Baby Gin')
    else:
        print(f'#{test_case} Lose')