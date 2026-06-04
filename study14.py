# N을 연속된 자연수의 합으로 표현하는 모든 경우를 출력하세요.
N = int(input())

for i in range(1, N + 1): # i의 범위 : 1 ~ N까지
    total = i # total값은 i를 기본으로 하고
    for j in range(i + 1, N + 1): # j의 범위 : i + 1 ~ N 까지
        total += j # i에다 j를 하나씩 더함
        if total == N: # i + j[0] + ... = total일 때
            print(f"{N} = ", end = "")
            for k in range(i, j + 1): # 출력
                # k의 값이 마지막 값이 아닌 경우는 +를 붙여서
                if k != j: 
                    print(k, end = " + ")
                # 마지막인 경우는 그냥 출력 
                else:
                    print(k)
                    
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# N을 연속된 자연수의 합으로 표현하는 모든 경우를 출력하세요.
N = int(input())

for start in range(1, N // 2 + 1):  # 시작값 범위: 1 ~ N//2 (최소 2개 합산 가능한 범위)
    total = start
    for end in range(start + 1, N + 1):  # 끝값 범위: start+1 ~ N
        total += end
        if total == N:  # start + ... + end = N인 경우 출력
            print(f"{N} = " + " + ".join(str(k) for k in range(start, end + 1)))  # join으로 간결하게 출력
            break  # 같은 start에서 N을 만들었으면 더 탐색 불필요
        if total > N:  # 합이 N을 초과하면 더 이상 탐색 불필요
            break