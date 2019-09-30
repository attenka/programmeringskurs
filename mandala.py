import turtle

def mandala(width,degrees,color):
    
    sissi = turtle.Turtle()
    sissi.color(color)

    for a in range(30):
        sissi.circle(width)
        sissi.left(degrees)

mandala(50,12,"red")
