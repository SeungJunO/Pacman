import random

list = ['head','tail']

while(True):
    response = input("동전 던지기를 계속하시겠습니까?")
    if response == "yes":
        coin = random.choice(list)
        print(coin)
    else:
        break
