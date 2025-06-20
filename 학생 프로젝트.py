import random
import turtle
def TurtleSquare():
    t=turtle.Turtle()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
def TurtleCircle(scale):
    t=turtle.Turtle()
    t.circle(scale)
def TurtleTriangle():
    t=turtle.Turtle()
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
def TurtleHexagon():
    polygon=turtle.Turtle()

    num_sides=6
    side_length=70
    angle=360.0/num_sides

    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)
def TurtleStar():
    star=turtle.Turtle()

    for i in range(5):
        star.forward(50)
        star.right(144)
def TurtlePentagon():
    polygon=turtle.Turtle()

    num_sides=5
    side_length=70
    angle=360.0/num_sides

    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)


print("도형 맞추기 게임을 시작합니다.")
print("자동으로 그려지는 도형들의 모형을 맞추어 주세요")
answerList=["사각형","원","삼각형","육각형","별","오각형"]

while True:
    r=random.randint(1,6)


    if r==1:TurtleSquare()
    elif r==2:TurtleCircle(100)
    elif r==3:TurtleTriangle()
    elif r==4:TurtleHexagon()
    elif r==5:TurtleStar()
    elif r==6:TurtlePentagon()
    answer=answerList[r-1]

    shape= input("도형의 이름을 적어주세요:")
    if shape not in answerList:
        print("다음 보기 중에서 입력해주세요")
        print(*answerList)

    else:
        if shape==answer:
            print("정답입니다.")
        else:
            print("틀렸습니다.")

          
           

