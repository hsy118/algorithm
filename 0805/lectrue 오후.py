# 비트 연산

arr = [1,2,3]
N = len(arr)
for i in range(1<<N):   #(2 ** n)
    for j in range(N):
        if i & (1 << j):
            print(arr[j], end= ",")
    print()
print()

#========
# 2진 탐색
def seq_search(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
    if i < n:
        return i
    else:
        return -1

arr= [4, 9, 11,23,2,19,7]
key = 23
print(seq_search(arr, len(arr), key))
#========================
#2 진 탐
def bin_sear(a, key):
    start = 0
    end = len(a)
    while start <= end:
        middle = (start + end) // 2
        # key 값과 같을때
        if a[middle] == key:
            return True, middle
        # key 값보다 작을때
        elif a[middle] > key:
            end = middle -1
        # key 값보다 클때
        else:
            start = middle + 1
    return -1
#=================
#선택 정
def selectionSort(a):
    # i : 0 ~ len(n) -1
    for i in range(len(a)-1): #0, 1, 2, 3
        # 최소값 찾기
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        #최소값 찾은 인덱스는 이제 min 이다.
        #그 min번째 값이랑 i랑 바꾼다.
        a[i], a[min] = a[min], a[i]

arr = [64, 25, 10, 22, 11]
selectionSort(arr)
print(arr)
#====================
def selection(a, k):
    # i : 0 ~ len(n) -1
    for i in range(k): #k번하
        # 최소값 찾기
        min = i
        for j in range(i+1, len(a)):
            if a[min] < a[j]:
                min = j
        #최소값 찾은 인덱스는 이제 min 이다.
        #그 min번째 값이랑 i랑 바꾼다.
        a[i], a[min] = a[min], a[i]
    return a[k-1]

def selectionSort(a):
    # i : 0 ~ len(n) -1
    for i in range(len(a)-1): #0, 1, 2, 3
        # 최소값 찾기
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        #최소값 찾은 인덱스는 이제 min 이다.
        #그 min번째 값이랑 i랑 바꾼다.
        a[i], a[min] = a[min], a[i]

arr = [64, 25, 10, 22, 11]
selectionSort(arr)
print(arr)
print(selection(arr, 3))
#==============================
"""
달팽이 문제:
돌떄 델타 검색 4방향임 오른쪽으로 0 아래로 1 왼쪽으로 2 위로 3
돌다가 만나면 멈추고, 방향 바꾸고

"""