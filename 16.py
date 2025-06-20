import turtle
t = turtle.Turtle()

size = int(input("집의 크기 입력:"))
house_color = input("그리는 색 입력:")
t.color(house_color)
t.width(10)

t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)

t.fd(size)
t.lt(120)
t.fd(size)
t.lt(120)
t.fd(size)
t.lt(120)
