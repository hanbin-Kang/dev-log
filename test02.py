hp = 100
has_key = 0
current_room = 1
game_over = 0

# 다시 풀어보기 

print("=== 미니 텍스트 어드벤처 ===\n당신은 신비한 던전에 들어왔습니다...")
print(f"HP: {hp}")

while True:
    # 1번방일 때
    if current_room == 1:
        choice = input()
        print("--- 방 1: 시작의 방 ---\n두 개의 문이 보입니다.\n(1) 왼쪽 문  (2) 오른쪽 문")
        if choice == "1":
            current_room += 1
            print("왼쪽 문을 열고 조심스럽게 들어갑니다.")
            print()
        elif choice == "2":
            hp -= 20
            print("오른쪽 문에 함정이 있었습니다! HP -20")
            print(f"HP: {hp}")
            if hp <= 0:
                print("체력이 다했습니다 ... 게임 오버!")
            else:
                current_room += 1
            print()
    
    #2번방일때
    elif current_room == 2:
        print("--- 방 2: 보물의 방 ---")
        print("낡은 상자가 하나 있습니다.")
        choice = input("상자 선택: ")
        print("(1) 상자 열기  (2) 그냥 지나가기")
        

        if choice == "1":
            has_key += 1
            print("상자에서 열쇠를 발견했습니다!")
            current_room += 1
            print()
        elif choice == "2":
            current_room += 1
            print("상자를 무시하고 지나갑니다.")
            print()
        else:
            print("1 또는 2를 선택하세요.")
            print()

    # 3번방일때
    elif current_room == 3:
        print("--- 방 3: 최종 방---")
        print("거대한 잠긴 문이 보입니다.")
    
        # 열쇠가 있을 때
        if has_key == 1:
            print("열쇠로 문을 열었습니다!")
            print()
            print("축하합니다! 던전에서 탈출했습니다!")
            print(f"남은 HP: {hp}")
            break
        else:
            choice = input("어떻게하지?: ")
            if choice == "1":
                print("방 2로 돌아갑니다.")
            elif choice == "2":
                print("문이 잠겨 있습니다! 열쇠가 필요합니다.")
                print("(1) 돌아가기(방2) (2) 문 부수기(HP -50)")
                hp -= 50
                print("문을 부쉈습니다! HP -50")
                print(f"HP: {hp}")
                if hp > 0:
                    print("문을 부수고 탈출했습니다!")
                    print(f"남은 HP: {hp}")
                    break

                else:
                    print("체력이 다했습니다... 게임 오버!")
                    break

            else:
                print("1 또는 2를 선택하세요.")