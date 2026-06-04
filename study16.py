# x를 0부터 100까지 순회하며 (c - a*x)가 b로 나누어 떨어지는지 확인
line = input()
parts = line.split()
a = int(parts[0])
b = int(parts[1])
c = int(parts[2])

# flag를 세우고
count = 0
# x를 0 ~ 100까지 순회
for x in range(0, 101):
    # c에서 ax값을 뺀거를 b로 나눴을 떄 나눠 떨어지는지 확인
    if (c - a * x) % b == 0:
        # 그때 y값을 구해야함 
        if (c - a*x) // b >= 0:
            # 해가 나올때마다 flag + 1
            count += 1
            print(f"x={x}, y={(c - a*x) // b}")

# flag가 없을 때는 
if count == 0:
    print("해가 없습니다")
    
# --------------------------------------------------------------------------------------------------------------------------------------------------------

# x를 0부터 100까지 순회하며 (c - a*x)가 b로 나누어 떨어지는지 확인
line = input()
parts = line.split()
a = int(parts[0])
b = int(parts[1])
c = int(parts[2])

# 해의 개수를 세는 변수 (해가 없는 경우 판별용)
solution_count = 0

# x를 0 ~ 100까지 순회
for x in range(0, 101):
    remainder = c - a * x  # 중간값을 변수에 저장해 중복 계산 방지

    # remainder가 b로 나누어 떨어지고 y가 음이 아닌 경우
    if remainder % b == 0 and remainder // b >= 0:
        solution_count += 1
        y = remainder // b
        print(f"x={x}, y={y}")

# 해가 하나도 없을 때
if solution_count == 0:
    print("해가 없습니다")