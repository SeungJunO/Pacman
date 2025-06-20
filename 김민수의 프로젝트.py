print("흑과 백게임을 시작합니다.")
print("################ 흑과 백 게임 설명 ################")
print("당신은 0부터 9까지의 숫자를 하나씩 가지고 있습니다.")
print("높은 숫자를 낸 플레이어가 승리하게 되는 게임입니다.")
print("#####0,2,4,6,8은 흑색, 1,3,5,7,9은 백색입니다.#####")
print("상대방의 숫자는 공개되지 않으며, 승패만 알 수 있습니다.")

import random

comScore = 0

userScore = 0

step = 0
number = [0,1,2,3,4,5,6,7,8,9]
while step <= 9:
    com = random.choice(number)
    if ( com == 0 or com == 2 or com == 4 or com == 6 or com == 8):
        print(" 컴퓨터의 숫자는 흑색입니다")
    else :
        print(" 컴퓨터의 숫자는 백색입니다")

    user = int(input("0부터 9까지의 숫자중 하나를 선택해주세요:"))

    if (com < user):
        print(" 당신이 이겼습니다.")
        userScore = userScore + 1
        print("(플레이어) %s : %s (컴퓨터)" %(userScore, comScore))
        
    elif (com > user):
        print(" 컴퓨터가 이겼습니다.")
        comScore = comScore + 1
        print("(플레이어) %s : %s (컴퓨터)" %(userScore, comScore))
    elif (com == user):
        print("비겼습니다")
        userScore = userScore + 1
        comScore = comScore + 1
        print("(플레이어) %s : %s (컴퓨터)" %(userScore, comScore))
    step = step + 1
    number.remove(com)
    





print("최종결과 (플레이어) %s: %s (컴퓨터) 입니다." %(userScore, comScore))
if (comScore < userScore) :
    print("당신이 승리하셨습니다.")
elif (comScore > userScore) :
    print("당신이 패배하셨습니다.")
elif (comScore == userScore):
    print("동점으로 비겼습니다.")
