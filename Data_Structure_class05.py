# 정수 리스트로 변환 후 한 줄을 더 입력받아 인덱스/값으로 분해하고 직접 할당하세요.
n = int(input())

# n개의 점수를 입력받고, list에 저장
score = input().split()

# 문자열 리스트를 정수로 변경
int_score_list = []

for i in score:
    int_score_list.append(int(i))

# 원하는 곳에 원하는 점수를 insert()함
insert_score = input().split()

# 문자열 리스트 정수로 변환
int_insert_score = []

for j in insert_score:
    int_insert_score.append(int(j))

# 출력 
int_score_list[int_insert_score[0]] = int_insert_score[-1]

print(" ".join(str(s) for s in int_score_list))

# ----------------------------------------------------------------------------

# 정수 리스트로 변환 후 한 줄을 더 입력받아 인덱스/값으로 분해하고 직접 할당하세요.
n = int(input())

# n개의 점수를 입력받아 정수 리스트로 변환 (map 활용으로 루프 생략)
int_score_list = list(map(int, input().split()))  # 한 줄로 split + int 변환

# 인덱스와 새 점수를 바로 언패킹 (int_insert_score[-1] 같은 암묵적 참조 제거)
target_index, new_score = map(int, input().split())  # 두 값을 명시적으로 분리

# 원하는 위치에 새 점수를 직접 할당
int_score_list[target_index] = new_score

# 출력
print(" ".join(str(s) for s in int_score_list))