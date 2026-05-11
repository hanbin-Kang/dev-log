# 내 풀이

# 1!부터 N!까지 출력하고 합을 구하세요.
n = int(input())
# 팩토리얼의 값
total = 1
# 팩토리얼 전체의 합
sum_total = 0

# 팩토리얼 표현
for i in range(1, n + 1):
    total *= i 
    print(f"{i}! = {total}")
    sum_total += total
# 결과 표현
for x in range(1, n + 1):
    if x != n:
        print(f"{x}! +", end=" ")
    else:
        print(f"{x}! = {sum_total}")

# 해석
# 위에 for문은 팩토리얼 자체와 그 값을 표현하고, 
# 밑에 for문은 전체 팩토리얼들과, 그 합을 표현한다

# 이 문제를 풀고 느낀점: 항상 문제 풀때 중첩 for문에만 신경을 썻는데 for문을 두개 따로 쓰는 경우도 생각하면 편하다는것을 느꼇다 
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 답지

# 1!부터 N!까지 출력하고 합을 구하세요.
n = int(input())

# 현재까지 계산된 팩토리얼 값
current_factorial = 1  # 변수명을 명확하게 변경
# 팩토리얼 전체의 합
sum_total = 0

# 팩토리얼 출력 및 합 계산
for i in range(1, n + 1):
    current_factorial *= i
    print(f"{i}! = {current_factorial}")
    sum_total += current_factorial

# 결과 표현: join을 사용해 두 번째 루프 제거
summary = ' + '.join([f'{x}!' for x in range(1, n + 1)])  # 반복문 하나로 합산 라인 생성
print(f"{summary} = {sum_total}")

# 해석
# 팩토리얼의 범위를 1~n까지 잡고, 현재까지 계산된 팩토리얼의 값을 current_factorial로 두고, 전체 팩토리얼의 합을 sum_total으로 둔다
# join을 사용하여 한줄로 표현