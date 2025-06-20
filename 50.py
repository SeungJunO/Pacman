englishscore = int(input("영어 점수 입력:"))
mathscore = int(input("수학 점수 입력:"))

sum = englishscore + mathscore

if englishscore < 40 :
    print("불합격 : 영어 점수가 부족합니다.")
else:
    if mathscore < 40 :
        print("불합격 : 수학 점수가 부족합니다.")
    else:
        if sum <= 110 :
            print("불합격 : 총합 점수가 부족합니다.")
        else:
            print("합격")
    
    
    
