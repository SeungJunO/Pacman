import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

t=turtle.Turtle()
t.shape("turtle")
t.width(3)

colors = ["yellow","red","purple","blue"]
for c in colors:
    t.color(c)
    t.forward(200)
    t.left(90)
