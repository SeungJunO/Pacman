score = int(input("성적을 입력하시오:"))
if score >= 90 :
    print("학점 A")
else:
    if score >= 80:
        print("학점 B")
    else :
        if score >= 70:
            print("학점 C")
        else:
            if score >= 60 :
                print("학점 D")
            else:
                print("학점 F")
