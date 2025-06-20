number = 1234
sum1 = 0
while number > 0:
    digit = number % 10
    sum1 = sum1 + digit
    number = number // 10
print("자리수의 합은%d입니다." %sum1)
