T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    list1 = list(map(int, input().split()))

    count = 1
    max = []
    max_count = 0
    for i in range(0, len(list1) - 1):
        if list1[i] < list1[i+1]:
            count += 1
            max.append(count)
        elif list1[i] > list1[i+1]:
            max.append(count)
            count = 1

    for i in range(0, len(max)):
        max_count = max[0]
        if max[i] > max_count:
            max_count = max[i]



    print(f'#{test_case} {max_count}')

"""
num = 456789
c = [0] * 12
for i in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue

    i += 1
if tri + run == 2 : print("baby gin")
else: print('lose')
"""