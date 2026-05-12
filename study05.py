# 1부터 N 사이의 쌍둥이 소수 쌍을 출력하세요.
# 범위 내에서 차이가 2이상 나는 소수를 찾아 출력하라
N = int(input())

prime_list = []
# 범위 내에서 소수 찾기
for prime in range(2, N + 1):
    # 범위를 지정했고 소수인지 확인해야함
    not_prime_count = 0
    for num in range(2, prime):
        # 나누어 떨어지면 그 숫자는 소수가 아니다
        if prime % num == 0:
            not_prime_count += 1
    # 범위 내의 소수 출력
    if not_prime_count == 0:
        prime_list.append(prime)

# 2차이나는 숫자들 찾기
for twins in prime_list:
    # 설정한 수 + 2가 리스트 안에 존재하면
    if twins + 2 in prime_list:
        # 그 수는 twin이다.
        twin = twins + 2
        print(f"({twins}, {twin})")

# ----------------------------------------------------------------------------------------------------------
# 1부터 N 사이의 쌍둥이 소수 쌍을 출력하세요.
# 범위 내에서 차이가 정확히 2인 소수 쌍(쌍둥이 소수)을 찾아 출력한다
N = int(input())

prime_list = []
# 범위 내에서 소수 찾기
for prime in range(2, N + 1):
    # 범위를 지정했고 소수인지 확인해야함
    is_prime = True  # 불리언 플래그로 변경: 소수 여부를 직접 표현
    for num in range(2, int(prime ** 0.5) + 1):  # √prime까지만 검사해 효율 개선
        # 나누어 떨어지면 그 숫자는 소수가 아니다
        if prime % num == 0:
            is_prime = False
            break  # 약수 발견 즉시 종료
    # 범위 내의 소수 저장
    if is_prime:
        prime_list.append(prime)

prime_set = set(prime_list)  # in 연산을 O(1)로 만들기 위해 집합 변환

# 2 차이 나는 숫자들 찾기
for twins in prime_list:
    # 설정한 수 + 2가 집합 안에 존재하면
    if twins + 2 in prime_set:
        # 그 수는 twin이다.
        twin = twins + 2
        print(f"({twins}, {twin})")
        
        
        
