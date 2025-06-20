def get_line(x1,y1,x2,y2):
    if (x1 == x2):
        return 0,0
    else:
        slope = (y2-y1)/(x2-x1)
        yintercept = y1 - slope*x1
        return slope,yintercept

x1 = int(input("x1="))
y1 = int(input("y1="))
x2 = int(input("x2="))
y2 = int(input("y2="))

slope,yintercept = get_line(x1,y1,x2,y2)

print("기울기=", slope, "y절편=", yintercept)
