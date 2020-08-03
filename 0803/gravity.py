"""
가장 높은 상자 기준
오른쪽에 낮은 상자의 갯수만큼 이동 가능
for i in range(0, len(arr)-2):
    for j in range(i+1, len(arr)-1):
        if arr[i] >arr[j]:
        count += 1
    if maxV < count:
        maxV = count

"""
T = int(input())
for test_case in range(0, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    max = 0
    count_list = []
    for i in range(0, len(arr) - 2):
        count = 0
        for j in range(i+1, len(arr)-1):
            if arr[i] > arr[j]:
                count += 1
        if max < count:
            max = count

    print(max)




