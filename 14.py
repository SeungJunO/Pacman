myMoney = int(input("돈을 입력하세요:"));
candyPrice = 120;
# 최대한 살 수 있는 사탕 수
numCandies = myMoney//candyPrice
print("살 수 있는 사탕의 수 :", numCandies)
# 최대한 사탕을 구입하고 남은 돈
change = myMoney%candyPrice;
print("사탕을 구입하고 남은 돈:", change)
