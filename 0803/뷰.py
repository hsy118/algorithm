"""
for i in ragne(2, len(arr) -3 ):
    a[i]에 대해..
    arr[i-2],arr[i-1]
    arr[i+1], arr[i+2]
    중에 가장 높은 건물보다 높은 칸수만큼 조망권 확보


"""
"""
T = int(input())
for test_case in range(0, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    window = 0
    sum = 0
    for i in range(2, len(arr)-2):
        if arr[i] > max(arr[i-2], arr[i-1], arr[i+1], arr[i+2]):
            window = arr[i] - max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
            sum += window
            window = 0


    print(f'#{test_case} {sum}')
"""
"""
T = int(input())
for test_case in range(0, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    for i in range(2, len(arr) - 2):
        height = arr[i]
        left = max(arr[i-2:i])

        if height < left:
            continue
        right = max(arr[i+1:i+3])

        if height < right:
            continue
        around_height = max(left, right)
        count += (height- around_height)

    print(f'#{test_case} {count}')
"""

for j in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))
    counter = 0
    for i in range(2, len(buildings) - 2):
        if buildings[i] <= buildings[i-1] or buildings[i] <= buildings[i-2] or buildings[i] <= buildings[i+1] or buildings[i] <= buildings[i+2]:
            continue
        else:
            k = max([buildings[i-1], buildings[i-2], buildings[i+1], buildings[i+2]])
            counter += (buildings[i] - k)
    print(f'#{j} {counter}')
