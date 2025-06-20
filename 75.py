n = 0
sum1 = 0
score = 0

print("종료하려면 음수를 입력하시오.")

while True:
    score = int(input("성적을 입력하시오: "))
    n = n+1

    if score < 0:
        break
    else :
        sum1 = sum1 + score

if n == 1:
    print("입력된 성적이 없습니다")
elif sum1 == 0 and n > 1:
    print("성적의 평균은 0점 입니다.")
else :
    avg = sum1 / (n -1)
    print("성적의 평균은 %f입니다."% avg)
