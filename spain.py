import turtle as Turtle
import time

def draw_spain():

    Turtle.setup(700, 700)

    ancho_banda = 300
    alto_banda = 200
    color_rojo = "#FF0000"
    color_amarillo = "#FFFF00"

    Turtle.speed(3)
    Turtle.hideturtle()
    Turtle.penup()
    Turtle.goto(-ancho_banda / 2, -alto_banda/3)
    Turtle.pendown()
    Turtle.showturtle()

    Turtle.begin_fill()

    # Dibujar la banda roja
    Turtle.color(color_rojo)
    Turtle.forward(ancho_banda)
    Turtle.right(90)
    Turtle.forward(alto_banda / 3)
    Turtle.right(90)
    Turtle.forward(ancho_banda)
    Turtle.right(90)
    Turtle.forward(alto_banda / 3)
    Turtle.end_fill()

    # Dibujar la banda amarilla
    Turtle.begin_fill()
    Turtle.color(color_amarillo)
    Turtle.forward(alto_banda / 3)
    Turtle.right(90)
    Turtle.forward(ancho_banda)
    Turtle.right(90)
    Turtle.forward(alto_banda / 3)
    Turtle.right(90)
    Turtle.forward(ancho_banda)
    Turtle.end_fill()

    Turtle.penup()
    Turtle.right(90)
    Turtle.forward(alto_banda / 3)
    Turtle.pendown()

    Turtle.begin_fill()

    # Dibujar la banda roja
    Turtle.color(color_rojo)
    Turtle.forward(alto_banda / 3)
    Turtle.right(90)
    Turtle.forward(ancho_banda)
    Turtle.right(90)
    Turtle.forward(alto_banda / 3)
    Turtle.right(90)
    Turtle.forward(ancho_banda)
    Turtle.end_fill()

    # Ocultar la tortuga y finalizar
    Turtle.hideturtle()
    time.sleep(10)
    
    # Cerrar la ventana
    Turtle.bye()