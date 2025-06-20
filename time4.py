import time

now = time.time()
thisYear = int(1970 + now//(365*24*3600))

print("올해는 "+ str(thisYear)+"입니다.")
age = int(input("현재 나이는?"))

ageYear = int(input("내 나이를 알고싶은 년도:"))
print(str(ageYear)+"년에는 "+str(age+ageYear-thisYear)+"세가 됩니다.")
