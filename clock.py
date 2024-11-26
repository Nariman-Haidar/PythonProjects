import turtle
import time

# Set up the window
window = turtle.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)
window.title("Clock")
window.tracer(0)  # Turns off screen updates

# Create the Pen that is going to draw the clock
pen = turtle.Turtle()
pen.speed(1)
pen.pensize(3)
pen.hideturtle()

# Draw the clock frame once
def draw_clock_frame():
    """pen.penup()
    pen.pensize(6)
    pen.setposition(0, 210)
    pen.setheading(180)
    pen.color("white")
    pen.backward(10)
    pen.pendown()
    pen.circle(210)"""
    # draw the 3,6,9,12 in the clock
    pen.penup()
    pen.setposition(0, 160)
    pen.write("12", align="center", font=("Arial", 24, "normal"))
    pen.setposition(140, 0)
    pen.write("3", align="center", font=("Arial", 24, "normal"))
    pen.setposition(0, -180)
    pen.write("6", align="center", font=("Arial", 24, "normal"))
    pen.setposition(-140, 0)
    pen.write("9", align="center", font=("Arial", 24, "normal"))


def draw_clock(h, m, s):
    # Draw lines for the hours
    pen.penup()
    pen.setposition(0, 0)
    pen.setheading(90)
    for _ in range(12):
        pen.forward(210)
        pen.pendown()
        pen.backward(20)
        pen.penup()
        pen.setposition(0, 0)
        pen.right(360 / 12)

    for _ in range(60):
        pen.color("pink")
        pen.pensize(2)
        pen.forward(210)
        pen.pendown()
        pen.backward(10)
        pen.penup()
        pen.setposition(0, 0)
        pen.right(360/60)

    # Draw the hour hand
    pen.color("pink")
    pen.pensize(10)
    pen.penup()
    pen.setposition(0, 0)
    angle = (h / 12) * 360
    pen.setheading(90)
    pen.right(angle)
    pen.pendown()
    pen.forward(90)

    # Draw the minute hand
    pen.color("yellow")
    pen.pensize(8)
    pen.penup()
    pen.setposition(0, 0)
    angle = (m / 60) * 360
    pen.setheading(90)
    pen.right(angle)
    pen.pendown()
    pen.forward(120)

    # Draw the second hand
    pen.color("purple")
    pen.pensize(6)
    pen.penup()
    pen.setposition(0, 0)
    angle = (s / 60) * 360
    pen.setheading(90)
    pen.right(angle)
    pen.pendown()
    pen.forward(170)

# Draw the clock frame initially
draw_clock_frame()

# Main loop
while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    pen.clear()
    draw_clock_frame()  # Keep the clock frame visible
    draw_clock(h, m, s)  # Update the clock hands

    window.update()  # Update the window
    time.sleep(1)  # Wait for one second
