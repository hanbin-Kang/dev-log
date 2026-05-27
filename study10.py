# 수를 문자열로 변환하여 뒤집고, 회문 여부를 판단
num = int(input())

# 변수를 문자열로 바꿔서 인덱스 사용
num = str(num)

# 변수가 몇글자인지
digit = len(num) - 1

# 단계
step_count = 0 

# 처음부터 회문인 경우
if num[0] == num[-1]:
    print(f"이미 회문입니다: {num}")

# 아닌 경우
else:
    while True:
        # 거꾸로 뒤집은 수 누적 변수로 쌓기
        reversed_num = ""

        # 풀이 과정
        step_count += 1
        for i in range(digit, -1, -1):
            reversed_num += str(num)[i]
        print(f"단계 {step_count}: {int(num)} + {int(reversed_num)} = {int(num) + int(reversed_num)}")

        num = int(num) + int(reversed_num)
        digit = len(str(num)) - 1
        
        # 정지 조건
        if str(num)[0] == str(num)[-1]:
            print(f"회문 완성: {num} ({step_count}단계)")
            break

# 내가 푼 알고리즘 : 입력한 숫자를 문자열로 바꾸고 인덱스를 사용하고 첫글자와 끝글자 비교, 몇자리인지 판단하여 for문의 step을 활용하여 숫자 뒤집기, 회문이 될 때 까지 반복 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 수를 문자열로 변환하여 뒤집고, 회문 여부를 판단
num = int(input())

# 단계
step_count = 0

# 처음부터 회문인 경우: 전체 문자열을 뒤집어 비교해야 정확함
num_str = str(num)
if num_str == num_str[::-1]:
    print(f"이미 회문입니다: {num_str}")

# 아닌 경우
else:
    while True:
        num_str = str(num)
        # [::-1] 슬라이싱으로 간결하게 뒤집기 (digit 변수와 for 루프 불필요)
        reversed_str = num_str[::-1]
        reversed_num = int(reversed_str)

        # 풀이 과정
        step_count += 1
        result = num + reversed_num
        print(f"단계 {step_count}: {num} + {reversed_num} = {result}")

        num = result

        # 정지 조건: 전체 문자열 비교로 정확한 회문 판별
        if str(num) == str(num)[::-1]:
            print(f"회문 완성: {num} ({step_count}단계)")
            break

# 회문의 개념 정확하게 알기, if num == num[::-1]: << 활용하기 , num[::-1]은 문자열을 뒤집는 슬라이싱이다([start : end : step]). 굳이 for문으로 안하여도 됨

# 인덱싱 추가로 공부하기

