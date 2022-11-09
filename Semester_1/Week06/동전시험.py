import turtle
def draw(x, y):
    t.penup()
    t.goto(x, y)
    t.stamp()
    t.pendown()
    
t = turtle.Turtle()
image = "front.GIF"
s = turtle.Screen()
s.addshape(image)
t.penup()
t.shape(image)
s.onscreenclick(draw)

s.listen()
s.mainloop()
