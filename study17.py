# 총 시간과 신호 주기를 입력받아 각 초의 신호를 출력하세요.
time = int(input())
green, yellow, red = input().split()
green = int(green)
yellow = int(yellow)
red = int(red)

# 남은 시간
time_left = time
# 입력된 시간의 전체 합
all_time = green + yellow + red
# 몇바퀴를 순회해야하는지
total_round = time // all_time + 1
# 순회한 바퀴
round_count = 0
# 추가 시간
plus_time = 0

# 무한 반복
while True:
    # 정지 조건 : 라운드 수와 총 순회해야하는 수가 같을 때
    if round_count == total_round:
        break
    # 그 외
    else:
        for t in range(time_left):  
            if green > t:
                print(f"{t + plus_time}초: 초록") 
            elif green + yellow > t:
                print(f"{t + plus_time}초: 노랑")
            elif green + yellow + red > t:
                print(f"{t + plus_time}초: 빨강")
        # 라운드 수 + 1
        round_count += 1
        # 남은 시간 : 전체 시간 - 합산 시간
        time_left -= all_time
        # 추가 시간 : 0 + 합산 시간
        plus_time += all_time

# ----------------------------------------------------------------------

# 총 시간과 신호 주기를 입력받아 각 초의 신호를 출력하세요.
t = int(input())
green, yellow, red = input().split()
green = int(green)
yellow = int(yellow)
red = int(red)

# 전체 주기
cycle_length = green + yellow + red

# 각 초에 대한 신호 상태 출력
for i in range(t):
    # 현재 초가 속한 주기 내 위치 계산
    position_in_cycle = i % cycle_length
    
    # 신호 상태 결정
    if position_in_cycle < green:
        signal = "초록"
    elif position_in_cycle < green + yellow:
        signal = "노랑"
    else:
        signal = "빨강"
    
    print(f"{i}초: {signal}")

# 나머지를 활용해서 간단하게 해결 가능