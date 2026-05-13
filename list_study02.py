numbers = [1, 2, 2, 3, 1, 4]

# 중복 제거해서 출력
# 결과: [1, 2, 3, 4]

#set을 사용하면 순서가 섞이고, 중복 제거 -> sorted를 사용해서 오름차순으로 정렬
print(sorted(set(numbers)))
# 자료형이 set에서 sorted를 씌우면 리스트가 됨
# -------------------------------------------------------

new_numbers = []

for i in numbers:
    if i not in new_numbers:
        new_numbers.append(i)
print(new_numbers)
# 자료형이 list