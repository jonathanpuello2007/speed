import turtle

#set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(2)

t.penup()
t.goto(0,-50)
t.pendown()
t.circle(100)

t.penup()
t.goto(-30,50)
t.pendown()
t.dot(20)

t.penup()
t.goto(30,50)
t.pendown()
t.dot(20)

t.penup()
t.goto(0,30)
t.setheading(-90)
t.pendown()
t.forward(20)

t.penup()
t.goto(-40,10)
t.setheading(-60)
t.width(3)
t.pendown()
t.circle(40,120)

t.penup()
t.goto(-70,100)
t.setheading(60)
t.width(2)
t.pendown()
for _ in range(3):
  t.forward(80)
  t.backward(80)
  t.right(45)

t.penup()
t.goto(0,-50)
t.setheading(-90)
t.width(5)
t.pendown()
t.forward(150)

t.penup()
t.goto(0,-80)
t.setheading(180)
t.pendown()
t.forward(100)

t.penup()
t.goto(0,-80)
t.setheading(0)
t.pendown()
t.forward(100)

t.penup()
t.goto(0,-200)
t.setheading(-30)
t.pendown()
t.forward(100)

t.penup()
t.goto(0,-200)
t.setheading(-150)
t.pendown()
t.forward(100)

t.hideturtle()
turtle.done()
