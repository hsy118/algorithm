T = int(input())
for tc in range(1, T+1):
    total, key_a, key_b = map(int, input().split())

    count = 0
    count_a = 0
    count_b = 0
    start = 1
    end = total

    while start <= end:
        count += 1
        middle = (start + end) // 2
        if middle == key_a:
            count_a = count
            count = 0
            start = 1
            end = total
            break

        elif middle < key_a:
            start = middle

        elif middle > key_a:
            end = middle

    while start <= end:
        count += 1
        middle = (start + end) // 2
        if middle == key_b:
            count_b = count
            count = 0
            break

        elif middle < key_b:
            start = middle

        elif middle > key_b:
            end = middle

    if count_a < count_b:
        answer = 'A'
    elif count_a > count_b:
        answer = 'B'
    else:
        answer = 0

    print(f'#{tc} {answer}')