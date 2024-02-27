import turtle
import spain
import france
import italy

list_paises = ["españa", "francia", "italia"]
ejecucion = True

def main():
    global ejecucion
    
    pais = input("Ingrese el nombre de un país: ")

    if pais.lower() in list_paises:
        if pais.lower() == "españa":
            spain.draw_spain()
        elif pais.lower() == "francia":
            france.draw_france()
        elif pais.lower() == "italia":
            italy.draw_italy()
    elif pais.lower() == "salir":
        print("Saliendo del programa.")
        ejecucion = False
    else:
        print("No entendí el nombre del país.")

    turtle.done()

if __name__ == "__main__":
    while ejecucion:
        main()
