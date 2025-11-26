### 5 задание
bin(n) 2-ричная
oct(n) 8-ричная
hex(n) 16-ричная
format(n, "b")

int(bin_n, X) X - система
zfill(n, 8)

### 6 задание

from turtle import *
tracer(0)


left(90)
for i in range(8):
    right(45)
    forward(8*k)

penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x*k, y*k)
        dot(4, 'red')

done()
