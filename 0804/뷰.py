for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(2, len(arr)-2):
        height = arr[i]
        left = max(arr[i-2:i])
        if height < left:
            continue

        right = max(arr[i+1:i+3])
        if height < right:
            continue
        around_height = max(left, right)
        count += (height - around_height)
        