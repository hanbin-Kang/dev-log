# 이중 반복문과 배치 카운트로 구현하세요.
n = int(input())
m = int(input())

# n명의 인원을 m열로 배치

# 열은 n // m 나머지가 있으면 + 1
if n % m == 0:
    standard_row = n // m
else:
    standard_row = (n // m) + 1


# 몇줄로 배치
for row in range(standard_row):
    print(f"[{row + 1}행]", end = " ")
    # 몇 명
    for col in range(m):
        # 나머지가 있을때 출력과 나머지가 없을 때 출력이 달라짐
        if n % m == 0:
            print(f"{row + 1}-{col + 1}", end = "  ")
        else:
            # 마지막 열에서의 출력을 다르게 해야함, 조건을 걸어야하는데 어떻게 걸지? for문 한번 더?
            if row + 1 == standard_row:
                for last_col in range(n %  m):
                    print(f"{row + 1}-{last_col + 1}", end = "  ")               
                break
            else:
                print(f"{row + 1}-{col + 1}", end = "  ")
    print()

  

# 출력
print(f"총 {standard_row}행 배치 완료 ({n}명)")

# ----------------------------------------------------------------------------------------------------

import math

# 이중 반복문과 배치 카운트로 구현하세요.
n = int(input())
m = int(input())

# n명의 인원을 m열로 배치

# 열은 n // m, 나머지가 있으면 + 1 → math.ceil 로 한 줄 처리
total_rows = math.ceil(n / m)

# 몇 줄로 배치
for row in range(total_rows):
    # 이번 행에 배치할 실제 인원 수 계산 (마지막 행은 나머지 인원만)
    seats_in_row = min(m, n - row * m)

    # 좌석 문자열 목록을 join으로 연결 → trailing space 없이 출력
    seats = '  '.join(f'{row + 1}-{col + 1}' for col in range(seats_in_row))
    print(f'[{row + 1}행] {seats}')

# 출력
print(f'총 {total_rows}행 배치 완료 ({n}명)')

# ------------------------------------------------------------------------------------------------------------------------

n = int(input())
m = int(input())

count = 1

if n % m == 0:
    standard_row = n // m
else:
    standard_row = n // m + 1

for row in range(standard_row):
    print(f"[{row + 1}행]", end=" ")

    for col in range(m):
        if count > n:
            break

        print(f"{row + 1}-{col + 1}", end="  ")
        count += 1

    print()

print(f"총 {standard_row}행 배치 완료 ({n}명)")

# 발상의 전환
# 너무 문제를 맞추는데 치중되어있지 말고, 알고리즘적으로 전체를 보고 풀기

"""첫번째는 내가 푼거, 두번째는 eval, 세번째는 gpt인데
내가 푼건 정답을 맞추자에 치중되어있는거같고, 두번째는 그 과정을 간단하게 명령어 사용하여 푸는 느낌이고,
세번째는 전체 틀을 보고 알고리즘적으로 어떻게 접근할지를 본 느낌이다""" 