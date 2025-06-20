import random
tries = 0
guess = 0
answer = random.randint(1,100)

print("1부터 100 사이의 숫자를 맞추시오")

while guess != answer :
    guess = int(input("숫자를 입력하시오 :"))
    tries = tries +1
    if guess < answer:
        print("정답보다 낮음!")
    elif guess > answer :
        print("정답보다 높음!")
    else:
        break

print("축하합니다. 정답은 %s 시도횟수 = %s" %(answer, tries))
