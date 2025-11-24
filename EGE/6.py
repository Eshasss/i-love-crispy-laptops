import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.setworldcoordinates(-300, -300, 300, 300)
t.left(90)
for i in range(8):
    t.right(45)
    t.forward(8)
turtle.done()