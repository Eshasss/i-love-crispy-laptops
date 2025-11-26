from turtle import *
tracer(0)
screen = Screen()
screen.setup(width=1200, height=1200)
screen.setworldcoordinates(-1200, -1200, 1200, 1200)
k = 20
# pendown()
left(90)
# forward(14*k)
for i in range(2):
    forward(14*k)
    left(270)
    backward(12*k)
    right(90)

penup()
forward(9*k)
right(90)
backward(7*k)
left(90)
pendown()
for i in range(2):
    forward(13*k)
    right(90)
    forward(6*k)
    right(90)
penup()



for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x*k, y*k)
        dot(4, 'red')

done()
