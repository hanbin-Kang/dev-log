# 정수 리스트 변환 후 두 번째 줄에서 a, b 를 받아 del 슬라이싱 한 줄로 처리하세요.
n = int(input())

# n개가 있는 리스트 생성
num_list = list(map(int, input().split()))

# 인덱싱 넘버 리스트 생성
index_list = list(map(int, input().split()))

# index_list[0]앞쪽 + index_list[1]뒤쪽
new_list = num_list[:index_list[0]] + num_list[index_list[1]:]

# 출력
print(" ".join(str(number) for number in new_list))

# ------------------------------------------------------------------------

# 정수 리스트 변환 후 두 번째 줄에서 a, b 를 받아 del 슬라이싱 한 줄로 처리하세요.
n = int(input())

# n개가 있는 리스트 생성
num_list = list(map(int, input().split()))

# 인덱싱 넘버 리스트 생성
index_list = list(map(int, input().split()))

# 중간부분 삭제
del num_list[index_list[0]:index_list[1]]

# 출력
print(" ".join(str(number) for number in num_list))