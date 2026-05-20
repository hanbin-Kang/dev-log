# 1부터 N 사이의 카프리카 수를 찾아 출력하세요.
n = int(input())

#출력
print("카프리카 수:")
print(1)

# 1. 범위 내의 수에서 제곱수 구하기
for divisor in range(1, n + 1):
    # 제곱한 수를 문자열로 바꿔서
    str_divisor = str(divisor ** 2)
    # 짝수 자리의 수만 남기고,
    if len(str_divisor) % 2 == 0:
        # print(str_divisor) : n이 10일 떄 16, 25, ... , 81
        is_kaprica_list = []
        is_kaprica_list.append(str_divisor)
        # 그 짝수 자리 수를 반으로 나누고 합이 divisor과 같으면 카프리카 수
        half = len(str_divisor) // 2
        # print(half) # 1, 1, 1 ... 
        # 카프리카 수인지 구하기
        for kaprica in is_kaprica_list:
            if int(kaprica[half:]) + int(kaprica[:half]) == divisor:
                print(f"{divisor}: {divisor}^2 = {kaprica}, {kaprica[:half]} + {kaprica[half:]} = {divisor}")
                
# --------------------------------------------------------------------------------------------------------------------------------

# 1부터 N 사이의 카프리카 수를 찾아 출력하세요.
n = int(input())

# 출력 헤더
print("카프리카 수:")
print(1)  # 1은 특수 케이스로 항상 포함

# 1. 2부터 N 범위의 후보 수에 대해 카프리카 수 검사
for num in range(2, n + 1):  # divisor → num: 검사 대상 숫자임을 명확히
    squared_str = str(num ** 2)  # 제곱수를 문자열로 변환
    sq_len = len(squared_str)

    # 2. 모든 분할 위치를 시도 (오른쪽 부분이 0이면 제외)
    for split in range(1, sq_len):
        left_str = squared_str[:split]
        right_str = squared_str[split:]

        # 오른쪽 부분이 순수하게 0이면 제외
        if int(right_str) == 0:
            continue

        # 두 부분의 합이 원래 수와 같으면 카프리카 수
        if int(left_str) + int(right_str) == num:
            print(f"{num}: {num}^2 = {squared_str}, {left_str} + {right_str} = {num}")
            break  # 한 분할로 조건 충족 시 다음 수로 이동