import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.fillcolor("red")
t.pencolor("green")
t.shapesize(1,5,10)
t.shapesize(10,5,1)
t.shapesize(1,10,5)
t.shapesize(10,1,5)
t.pensize(5)
t.forward(100)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.circle(60)
t.dot(20)

turtle.bgcolor("blue")
turtle.title("My Turtle Program")