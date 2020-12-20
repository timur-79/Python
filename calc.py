import turtle

turtle.shape('turtle')
for i in range(10):
    for step in range(4):
        turtle.forward(50+i*10)
        turtle.left(90)
