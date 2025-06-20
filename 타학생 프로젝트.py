import turtle
import time
from random import *



def UserInput():
    while True:
        global num
        num = int(turtle.textinput("","참가할 거북의 수를 적어주세요. (2~5) : "))
        if 2<= num <= 5:
            break
        else:
            write.goto(-300,100)
            write.write('2~5 사이의 수를 입력해주세요', font=("", 30))
            time.sleep(1.5)
            write.clear()
    return 0
        

t = turtle.Turtle()
t.ht()
t.penup()
write = turtle.Turtle()
write.penup()
write.ht()
UserInput()
for line in range(num + 1):
    t.penup()
    a = 300-(line*100)
    t.goto(-300,a)
    t.pendown()
    t.forward(600)
t.penup()
t.goto(300,300)
t.pendown()

t.right(90)
t.forward(num*100)

tu3 = turtle.Turtle()
tu3.ht()
tu3.penup()

tu4 = turtle.Turtle()
tu4.ht()
tu4.penup()

tu5 = turtle.Turtle()
tu5.ht()
tu5.penup()

yellow = -1000
black = -1000
green = -1000
            
member = ['red','blue']
tu1 = turtle.Turtle()
tu1.ht()
tu1.penup()
tu1.goto(-300,250)
tu1.st()
tu1.pendown()
tu1.shape('turtle')
tu1.color('red')
red = 0

tu2 = turtle.Turtle()
tu2.ht()
tu2.penup()
tu2.goto(-300,150)
tu2.st()
tu2.pendown()
tu2.shape('turtle')
tu2.color('blue')
blue = 0

if num >= 3 :
    tu3.goto(-300,50)
    tu3.st()
    tu3.pendown()
    tu3.color('yellow')
    tu3.shape('turtle')
    member += ['yellow']
    yellow = 0
    
    if num >= 4 :
        tu4.goto(-300,-50)
        tu4.st()
        tu4.pendown()
        tu4.color('black')
        tu4.shape('turtle')
        member += ['black']
        black = 0

        if num >= 5 :
            tu5.goto(-300,-150)
            tu5.st()
            tu5.pendown()
            tu5.color('green')
            tu5.shape('turtle')
            member += ['green']
            green = 0


print('참가멤버는',member,'입니다.')

expect = turtle.textinput("",'누가 1등할지 예측해보세요 : ')


for turn in range(80):
    t1 = randrange(1,15)
    tu1.forward(t1)
    red += t1

    t2 = randrange(1,15)
    tu2.forward(t2)
    blue += t2

    t3 = randrange(1,15)
    tu3.forward(t3)
    yellow += t3

    t4 = randrange(1,15)
    tu4.forward(t4)
    black += t4

    t5 = randrange(1,15)
    tu5.forward(t5)
    green += t5

a = [red,blue,yellow,black,green]
a = sorted(a)
a.reverse()

if a[0] == red:
    write.write('red 이 1등입니다.', font=("", 20))
    time.sleep(1.5)
    write.clear()
    ans = 'red'
elif a[0] == blue:
    write.write('blue 이 1등입니다.', font=("", 20))
    time.sleep(1.5)
    write.clear()
    ans = 'blue'
elif a[0] == yellow:
    write.write('yellow 이 1등입니다.', font=("", 20))
    time.sleep(1.5)
    write.clear()
    ans = 'yellow'
elif a[0] == black:
    write.write('black 이 1등입니다.', font=("", 20))
    time.sleep(1.5)
    write.clear()
    ans = 'black'
elif a[0] == green:
    write.write('green 이 1등입니다.', font=("", 20))
    time.sleep(1.5)
    write.clear()
    ans = 'green'

if expect == ans:
     write.write('축하드립니다!!!', font=("", 30))
else:
    if expect == 'red':
         print('당신의 거북이는 ',a.index(red) + 1,'위 입니다.')
    elif expect == 'blue':
         print('당신의 거북이는 ',a.index(blue) + 1,'위 입니다.')
    elif expect == 'yellow':
         print('당신의 거북이는 ',a.index(yellow) + 1,'위 입니다.')
    elif expect == 'black':
         print('당신의 거북이는 ',a.index(black) + 1,'위 입니다.')
    elif expect == 'green':
         print('당신의 거북이는 ',a.index(green) + 1,'위 입니다.')
    else:
        print('예측이 참가목록에 없습니다.')
