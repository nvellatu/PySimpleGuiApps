import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTeck")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_A = 0
score_B = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .3
ball.dy = .3

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: " + str(score_A) + " Player B: " + str(score_B), align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:

    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.Beep(200, 100)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.Beep(200, 100)

    if ball.xcor() > 390:
        score_A += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: " + str(score_A) + " Player B: " + str(score_B), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        score_B += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: " + str(score_A) + " Player B: " + str(score_B), align="center",
                  font=("Courier", 24, "normal"))

    if 340 < ball.xcor() < 350 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
        winsound.Beep(200, 100)

    if -350 < ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
        winsound.Beep(200, 100)
