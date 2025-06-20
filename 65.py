i = 1
fact = 1

n = int(input("팩토리얼을 구할 정수:"))

while (i <= n):
    fact = fact*i
    i = i+1
print("%s!은 %d입니다."%(n,fact))
