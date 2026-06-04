# 5개 숫자를 입력받아 5x5 빙고판에서 해당 숫자를 X로 표시하세요.
x = 1
user_list = []
for k in range(5):
    # 입력값 변수
    user_input = int(input())   
    user_list.append(user_input)

for i in range(5):
    # 입력값 변수
    # user_input = int(input()) >> 처음에 여기 둬서 안됐음  
    for j in range(5):
        if x in user_list:
            print("X", end = "\t")
        else:
            print(x, end = "\t")
        x += 1
    print()


# 처음에 저 위치에 둬서 안된 이유:
# 저 위치에 있으면 1행일때 받고, 2행일때 받고, ... ,5행일 때 받는건데
# 그래서 1,2,3,4,5는 출력이 안됨

# ! 중첩 for문에서 위치 잘 봐야함

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5개 숫자를 입력받아 5x5 빙고판에서 해당 숫자를 X로 표시하세요.

# 입력: 5개의 숫자를 먼저 모두 받아 집합에 저장
marked_numbers = set()
for k in range(5):
    user_input = int(input())
    marked_numbers.add(user_input)

# 출력: 빙고판 순회
num = 1  # x → num 으로 변경: 현재 칸의 숫자를 나타냄
for i in range(5):
    # 한 행을 리스트로 구성한 뒤 탭으로 join → 후행 탭 없음
    row = []
    for j in range(5):
        if num in marked_numbers:
            row.append("X")
        else:
            row.append(str(num))
        num += 1
    print("\t".join(row))  # 마지막 원소 뒤에 탭이 붙지 않음

