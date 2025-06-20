print("묵찌빠게임")


import random
options = ['묵','찌','빠']
player = input("(묵,찌,빠) 중에서 하나를 선택하세요:")
computer = random.choice(options)

print("사용자: %s, 컴퓨터: %s" %(player,computer))

while True:
    if (player == computer):
        print("비겼습니다.")
        print("다시 하시려면 다시 실행해주세요.")
        break
    elif (player == 
