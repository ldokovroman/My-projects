import turtle
from random import choice

window = turtle.Screen()
window.title("Ping Pong")
window.setup(width=1.0, height=1.0)
window.bgcolor("black")
window.tracer(10)

border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.color("green")

border.goto(-500, 300)
border.begin_fill()
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.end_fill()

border.goto(0, 300)
border.color("white")
border.setheading(270)
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()

left_rocket = turtle.Turtle()
left_rocket.color("white")
left_rocket.shape("square")
left_rocket.shapesize(stretch_len=1, stretch_wid=5)
left_rocket.up()
left_rocket.speed(0)
left_rocket.goto(-450, 0)

def move_up_l():
    y = left_rocket.ycor() + 20
    if y > 250:
        y = 250
    left_rocket.sety(y)

def move_down_l():
    y = left_rocket.ycor() - 20
    if y < -250:
        y = -250
    left_rocket.sety(y)

right_rocket = turtle.Turtle()
right_rocket.color("white")
right_rocket.shape("square")
right_rocket.shapesize(stretch_len=1, stretch_wid=5)
right_rocket.up()
right_rocket.speed(0)
right_rocket.goto(450, 0)

def move_up_r():
    y = right_rocket.ycor() + 20
    if y > 250:
        y = 250
    right_rocket.sety(y)

def move_down_r():
    y = right_rocket.ycor() - 20
    if y < -250:
        y = -250
    right_rocket.sety(y)

FONT = ("Arial", 44)

score_l = 0
score_l_t = turtle.Turtle()
score_l_t.hideturtle()
score_l_t.up()
score_l_t.color("white")
score_l_t.speed(0)
score_l_t.goto(-200, 300)
score_l_t.write(score_l, font=FONT)

score_r = 0
score_r_t = turtle.Turtle()
score_r_t.hideturtle()
score_r_t.up()
score_r_t.color("white")
score_r_t.speed(0)
score_r_t.goto(200, 300)
score_r_t.write(score_l, font=FONT)

DX = 1
DY = 1

ball = turtle.Turtle()
ball.up()
ball.shape("circle")
ball.color("red")
ball.speed(0)
ball.dx = choice([-DX, DX])
ball.dy = choice([-DX, DX])

window.listen()
window.onkey(move_up_l, "w")
window.onkey(move_down_l, "s")
window.onkey(move_up_r, "Up")
window.onkey(move_down_r, "Down")

def check(rocket):
    return rocket.ycor() - 60 <= ball.ycor() <= rocket.ycor() + 60 \
        and rocket.xcor() - 20 <= ball.xcor() <= rocket.xcor() + 20

while score_l < 10 and score_r < 10:
    window.update()
    ball.goto(ball.xcor() + ball.dx, ball.ycor() + ball.dy)
    if ball.ycor() >= 290:
        ball.dy = -ball.dy
    if ball.ycor() <= -290:
        ball.dy = -ball.dy
    if ball.xcor() >= 490:
        score_l += 1
        score_l_t.clear()
        score_l_t.write(score_l, font=FONT)
        ball.goto(0, 0)
        ball.dx = choice([-DX, DX])
        ball.dy = choice([-DY, DY])
    if ball.xcor() <= -490:
        score_r += 1
        score_r_t.clear()
        score_r_t.write(score_r, font=FONT)
        ball.goto(0, 0)
        ball.dx = choice([-DX, DX])
        ball.dy = choice([-DX, DX])
    if check(right_rocket):
        if ball.xcor() >= right_rocket.xcor() - 10:
            ball.dy = -ball.dy
        else:
            ball.dx = -ball.dx
        while check(right_rocket):
            ball.goto(ball.xcor() + ball.dx, ball.ycor() + ball.dy)
        ball.dy += ball.dy / abs(ball.dy) / 10
        ball.dx += ball.dx / abs(ball.dx) / 10
    if check(left_rocket):
        if ball.xcor() <= left_rocket.xcor() + 10:
            ball.dy = -ball.dy
        else:
            ball.dx = -ball.dx
        while check(left_rocket):
            ball.goto(ball.xcor() + ball.dx, ball.ycor() + ball.dy)
        ball.dy += ball.dy / abs(ball.dy) / 10
        ball.dx += ball.dx / abs(ball.dx) / 10

window.mainloop()
