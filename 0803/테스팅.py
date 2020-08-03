# arr = list(map(int, input().split()))
arr = [0, 0, 3, 5, 2, 4, 9, 0, 6, 4, 0, 6, 0,0]

count = 0
for i in range(2, len(arr) - 2):
    height = arr[i]
    left = max(arr[i - 2:i])

    if height < left:
        continue
    right = max(arr[i + 1:i + 3])

    if height < right:
        continue
    around_height = max(left, right)
    count += (height - around_height)

print(count)