K = 3
N = 10
M = 5
arr = [1,3,5,7,9]

station_list = [0] * (N + 1)
for i in range(len(arr)):
    station_list[arr[i]] += 1

start: int = 0
end = K
cnt = 0

while True:
    zero = 0
    for i in range(start+1, end+1):
        if station_list[i] == 1:
            start = i
         else:
            zero += 1

    if zero == K:
        cnt = 0
        break

    cnt += 1
    end = start + K

    if end >= N:
        break
print(f'#{test_case} {cnt}')
