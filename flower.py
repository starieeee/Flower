import turtle
p = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
p.pencolor("blue")
p.speed(0)
for i in range(150):
    p.circle(190-i,90)
    p.lt(90)
    p.circle(190-i,90)
    p.lt(18)