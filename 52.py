from random import randint

answer = randint(1,10)
print("숫자 게임에 오신 것을 환영합니다.")
guess = int(input("1-10 사이의 숫자를 맞춰 보세요: "))

if guess == answer:
    print("정답을 맞췄습니다!")
elif guess > answer:
    print("정답보다 큼!")
else:
    print("정답보다 작음!")
print("게임 종료")
