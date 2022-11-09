import random
import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range (30):
    length = random.randint(1, 100)
    # length = random.randrange(1, 100)
    t.fd(length)
    angle = random.randint(-180, 180)
    t.rt(angle)
