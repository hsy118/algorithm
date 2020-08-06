T = int(input())
for test_case in range(0, T+1):
    K, N, M = map(int, input().split()) # 몇칸 식 간다 / 총 정류장 / 충전기 수
    arr = list(map(int, input().split()))

    station_list = [0] * (N + 1)
    for i in range(len(arr)):
         station_list[arr[i]] += 1

    start = 0
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

"""
T = int(input())
for test_case in range(0, T+1):
    K, N, M = map(int, input().split()) # 몇칸 식 간다 / 총 정류장 / 충전기 수
    charger = list(map(int, input().split()))
    #충전위치 표를 만드는 경우
    
    stop = [0] * (N+1)
    for i in charger:
    stop[i] = 1
    
    cnt = 0
    last = 0 #마지막 충전 위치
    while last+K < N: # 마지막 충전 이후 종점을 통과하지 않으면
        if stop[last+K] == 1: #최대 이동 후 충전기가 있으면
            last = last + K #마지막 충전 위치 갱신
            cnt += 1
            
    
"""
"""
T = int(input())
for test_case in range(0, T+1):
    K, N, M = map(int, input().split()) # 몇칸 식 간다 / 총 정류장 / 충전기 수
    charger = list(map(int, input().split()))
    
    last = 0
    cnt = 0
    for i in range(1, M+2): #마지막 충전위치로부터 도착할 수 있는 충전기인지 확인
    if charger[i]-charger[i-1] > K: #두 충전기 사이 거리가 이동 가능 거리 초과
        cnt = 0
        break # 운행 불가
    elif charger[i] - charger[last] > K: #마지막 충전기로부터 도착할 수 없으면
        last = i-1 # 이전 충전기에서 충전
        cnt += 1
    
    print(f'{test_case} {cnt}')
    
        
"""
"""
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, intput().split())
    
    stop = [0] * N ...
    last = 0
    cnt = 0
    while last + K < N: # 종점에 도착하지 않은 경우
        if stop[last+K} == 1: #최대 이동후 충전기가 있으면
            last =last + K #마지막 충전 위치 갱신
            cnt += 1
        else: #최대 이동후 충전기가 없으면
        pre = last #last+1부터 last + K 사이 충전기 중 가장 먼 충전기 찾기
        for i in range(last+K, last, -1):
        if stop[i] == 1 :
            last = i #충전기 번호 기록
            cnt += 1 #충전횟수 추가
            break
        if pre == last: #마지막 충전위치 갱신되지 않으면
            cnt = 0 #운행 실패, 중단
            break
    print(f'#{tc} {cnt}'
"""