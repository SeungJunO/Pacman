import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("","몇각형을 원하시나요?:")
n = int(s)

i = 0
while i < n:
    t.forward(100)
    t.left(360/n)
    i += 1
