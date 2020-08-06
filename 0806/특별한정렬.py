T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    new_list = []
    while len(new_list) < 10:
        new_list.append(max(arr))
        arr.remove(max(arr))
        new_list.append(min(arr))
        arr.remove(min(arr))


    print(f'#{tc} {" ".join(map(str, new_list))}')



