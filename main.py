import turtle
import spain
import france
import italy
import germany
import japan
import time

list_paises = ["españa", "francia", "italia", "alemania", "japon"]

def main():
    while True:
        pais = input("Ingrese el nombre de un país: ").lower()

        if pais in list_paises:
            if pais == "españa":
                spain.draw_spain()
            elif pais == "francia":
                france.draw_france()
            elif pais == "italia":
                italy.draw_italy()
            elif pais == "alemania":
                germany.draw_germany()
            elif pais == "japon":
                japan.draw_japan()
            break  
        elif pais == "salir":
            break 
        else:
            print("El país ingresado no está en la lista. Inténtelo nuevamente.")

    print("Saliendo del programa.")
    time.sleep(1)

if __name__ == "__main__":
    main()