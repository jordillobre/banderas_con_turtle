import turtle as Turtle
import time

def draw_finland():

    Turtle.setup(700, 700)
    Turtle.bgcolor("Black")

    ancho_banda = 600
    alto_banda = 400
    ancho_cruz = 80
    color_azul = "#002F6C"
    color_blanco = "#FFFFFF"

    Turtle.hideturtle()
    Turtle.penup()
    Turtle.goto(-ancho_banda / 2, -alto_banda/2)
    Turtle.pendown()
    Turtle.showturtle()

    Turtle.begin_fill()

    Turtle.color(color_blanco)
    Turtle.forward(ancho_banda)
    Turtle.left(90)
    Turtle.forward(alto_banda)
    Turtle.left(90)
    Turtle.forward(ancho_banda)
    Turtle.left(90)
    Turtle.forward(alto_banda)
    Turtle.end_fill()

    Turtle.penup()
    Turtle.left(90)
    Turtle.goto(-ancho_banda/2, ancho_cruz/2)
    Turtle.pendown()

    Turtle.begin_fill()
    Turtle.color(color_azul)
    Turtle.forward(ancho_banda)
    Turtle.right(90)
    Turtle.forward(ancho_cruz)
    Turtle.right(90)
    Turtle.forward(ancho_banda)
    Turtle.right(90)
    Turtle.forward(ancho_cruz)
    Turtle.end_fill()

    Turtle.penup()
    Turtle.left(90)
    Turtle.goto(-ancho_cruz, alto_banda/2)
    Turtle.pendown()

    Turtle.begin_fill()
    Turtle.color(color_azul)
    Turtle.left(90)
    Turtle.forward(alto_banda)
    Turtle.right(90)
    Turtle.forward(ancho_cruz)
    Turtle.right(90)
    Turtle.forward(alto_banda)
    Turtle.right(90)
    Turtle.forward(ancho_cruz)
    Turtle.end_fill()


    Turtle.hideturtle()
    time.sleep(10)
    
    # Cerrar la ventana
    Turtle.bye()