# 정수 리스트로 변환 후 sorted 의 결과를 [1:-1] 로 잘라내 평균을 따로 구하세요.
n = int(input())

# 리스트 생성
score_list = list(map(int, input().split()))
print(f"원본 평균: {sum(score_list) / len(score_list):.1f}")

# 보정 리스트 생성
sorted_list = sorted(score_list)
new_list = sorted_list[1:-1] 

print(f"보정 평균: {sum(new_list) / len(new_list):.1f}")

# 질문 : 왜 sorted_list = sorted(score_list)여기서 
# sorted_list = sorted(score_list[1:-1])을 하면 이상하게 출력되는지
# => sorted(score_list[1:-1]) 이렇게 하면 list안에 있는 수를 먼저 자른 뒤에 순서대로 정렬하기 때문에
# sol : sorted(score_list)[1:-1]