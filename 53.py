import random
options = ['가위', '바위','보']
player = input("(가위,바위,보) 중에서 하나를 선택하세요: ")
computer = random.choice(options)
print("사용자: %s, 컴퓨터: %s" %(player,computer))
if (player == computer):
    print("비겼음!")
elif (player == "바위"):
    if (computer == "보"):
        print("컴퓨터가 이겼음!")
    else:
        print("사용자가 이겼음!")
elif (player == "보"):
    if (computer == "바위"):
        print("사용자가 이겼음!")
    else:
        print("컴퓨터가 이겼음!")
elif (player == "가위"):
    if (player == "바위"):
        print("컴퓨터가 이겼음!")
    else:
        print("사용자가 이겼음!")
