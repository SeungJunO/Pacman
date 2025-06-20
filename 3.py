Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t=turtle.Pen()
t.shape(turtle)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t.shape(turtle)
  File "C:\Users\o6439\AppData\Local\Programs\Python\Python310\lib\turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named <module 'turtle' from 'C:\\Users\\o6439\\AppData\\Local\\Programs\\Python\\Python310\\lib\\turtle.py'>
t.shape("turtle")
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.reset()
pencolor(red)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    pencolor(red)
NameError: name 'pencolor' is not defined
pencolor(colorstring)-red
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    pencolor(colorstring)-red
NameError: name 'pencolor' is not defined
pencolor(colorstring)red
SyntaxError: invalid syntax
pencolor(colorstring)-"red"
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    pencolor(colorstring)-"red"
NameError: name 'pencolor' is not defined
pencolor("red")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    pencolor("red")
NameError: name 'pencolor' is not defined
pencolor(colorstring)"red"
SyntaxError: invalid syntax
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
