time = int(input("근무시간을 입력하시오:"))
money = int(input("시간당 임금을 입력하시오:"))
if time >= 40 :
    print("40시간 이상 근무시 1.5배의 임금이 지급됩니다. 총임금은", time * money * 1.5,"입니다.")
else :
    print("총임금은",time * money,"입니다.")
