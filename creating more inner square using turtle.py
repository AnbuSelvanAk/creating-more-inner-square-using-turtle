from turtle import *
a=Screen()
x=Turtle()
def test(s):
    for i in range(4):
        x.fd(s)
        x.left(90)
        s=s+5
test(10)
test(30)
test(70)
test(90)
test(110)
test(130)