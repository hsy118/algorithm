def counting_sort(A, B, k):
    c = [0] * k
    # 카운팅
    for i in range(0, len(B)):
        c[A[i]] += 1

    # 누적
    for i in range(1, len(c)):
        c[i] += c[i-1]

    # 소트
    for i in range(len(b)-1, -1, -1):
        B[c[A[i]]-1] = A[i]
        c[A[i]] -= 1



a = [0, 4, 1, 3, 1, 2, 4, 1] # 소스
b = [0] * len(a)             # 결과
counting_sort(a, b, 4 + 1)


print(a)
print(b)
