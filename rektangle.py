import turtle

def rektangle(width,height,color):
    sissi = turtle.Turtle()
    sissi.color(color)
    sissi.begin_fill()
    sissi.forward(width)
    sissi.left(90)
    sissi.forward(height)
    sissi.left(90)
    sissi.forward(width)
    sissi.left(90)
    sissi.forward(height)
    sissi.end_fill()

rektangle(50,100,"red")
    
