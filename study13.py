num = int(input())  
str_num = str(num)

number = {
    1 : "일", 2 : "이", 3 : "삼", 4 : "사", 5 : "오", 6 : "육", 7 : "칠", 8 : "팔", 9 : "구"
}

grade = {
    4 : "천", 3 : "백", 2 : "십" , 1 : ""
}

# 숫자를 한글로 출력 : 5001 -> 오천일
for idx, value in enumerate(str_num):
    # 주요 알고리즘 : 0의 위치가 어디냐
    if value == "0":
        continue
    
    # 1이 가장 마지막 자리가 아니면 출력형식을 다르게 해야함
    if value != "1": 
        print(f"{number[int(value)]}{grade[len(str_num) - idx]}", end = "")
    
    # value값이 1일 때 / str_num[-1]이 1일때 출력이 안됨
    else:
        print(grade[len(str_num) - idx], end = "")
        
# 문제점 바깥에서 해결!  
if num % 10 == 1:
    print("일")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        
# 각 자릿수를 분리하여 한글로 변환하세요.
num = int(input())
# num을 문자열로 변경
str_num = str(num)

number = {
    1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"
}

# grade -> place_unit: 자릿수 단위 매핑 (이름을 더 명확하게)
place_unit = {
    4: "천", 3: "백", 2: "십", 1: ""
}

result = ""  # 결과를 누적한 뒤 마지막에 한 번 출력

# 숫자를 한글로 변환: 5001 -> 오천일
for idx, value in enumerate(str_num):
    # 주요 알고리즘: 0인 자릿수는 건너뜀
    if value == "0":
        continue

    digit = int(value)
    unit = place_unit[len(str_num) - idx]

    # 자릿수가 1이면 숫자 '일'을 생략, 일의 자리(unit이 빈 문자열)면 숫자 표시
    # 통합 처리: 루프 밖 우회 코드 불필요
    if value == "1" and unit != "":
        result += unit          # 예: 천, 백, 십 (일천→천, 일백→백, 일십→십)
    else:
        result += number[digit] + unit  # 예: 이백, 오천, 일(일의 자리)

print(result)
   
    
    