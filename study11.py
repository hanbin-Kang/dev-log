# 3개 문장을 라운드별로 처리하세요.
text1 = "Hello Python"
text2 = "I love coding"
text3 = "Practice makes perfect"
# 딕셔너리로 만들기
text = {
    1 : text1, 2 : text2, 3 : text3
}
# 정답인 글자 수
total_correct = 0
# 전체 글자수
total_chars = 0

# 두 문장 길이가 다르면 짧은 쪽만 비교, 길이 차이는 오류로 처리(비교 안 됨)

print("=== 타자 연습 ===")
print("표시된 문장을 정확히 입력하세요!")
print()

for i in range(1, 4):
    # 입력 변수
    user_input = input()
    # 전체 글자 수
    total_chars += len(text[i])
    print(f"[{i}번 문장] {text[i]}")
    # 글자수 비교를 해야함
    if len(text[i]) != len(user_input):
        print("글자수가 다릅니다") 
    else:
        # 정답인 글자
        correct = 0       
        # 각 글자마다 비교를 해야함
        for x in range(len(text[i])):
            if text[i][x] == user_input[x]:
                correct += 1
        print(f"정확도: {int(correct / len(text[i])) * 100:.1f}% ({correct}/{len(text[i])} 글자)")
        print()
        # 총 정답수 +1
        total_correct += correct


# 전체 정답률
correct_rate = int(total_correct / total_chars) * 100

# 출력
print("=== 최종 결과 ===")
print(f"전체 정확도: {correct_rate:.1f}% ({total_correct}/{total_chars} 글자)")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3개 문장을 라운드별로 처리하세요.
text1 = "Hello Python"
text2 = "I love coding"
text3 = "Practice makes perfect"

# 리스트로 관리하면 인덱스 접근이 더 자연스럽습니다
texts = [text1, text2, text3]

# 정답인 글자 수
total_correct = 0
# 전체 글자 수
total_chars = 0

print("=== 타자 연습 ===")
print("표시된 문장을 정확히 입력하세요!")
print()

for i, sentence in enumerate(texts, start=1):
    user_input = input()
    print(f"[{i}번 문장] {sentence}")

    # 비교할 범위: 짧은 쪽까지만 비교, 길이 차이는 오류(비교 안 됨)
    compare_len = min(len(sentence), len(user_input))
    correct = sum(1 for j in range(compare_len) if sentence[j] == user_input[j])

    # 문제 명세 공식: int(acc*10)/10 적용
    acc = int(correct / len(sentence) * 1000) / 10  # 소수점 첫째 자리 보장
    print(f"정확도: {acc:.1f}% ({correct}/{len(sentence)} 글자)")
    print()

    total_correct += correct
    total_chars += len(sentence)

# 전체 정답률 — 명세 공식 동일하게 적용
correct_rate = int(total_correct / total_chars * 1000) / 10

# 출력
print("=== 최종 결과 ===")
print(f"전체 정확도: {correct_rate:.1f}% ({total_correct}/{total_chars} 글자)")