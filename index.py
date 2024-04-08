def crear_matriz():
    while True:
        try:
            filas = int(input("ingresa el numero de filas para la matrz: "))
            columnas = int(input("ingresa el numero de columnas para la matriz: "))
            if filas <= 0 or columnas <= 0:
                print("asegurate de ingresar un numero mayor o igual a 1")
                continue
            matriz = [[0] * columnas for _ in range(filas)]
            return matriz
        except ValueError:
            print("ingresa un numero valido")

def main():
    matriz = crear_matriz()
    print("con las filas y columnas que seleccionaste la matriz es la siguiente: ")
    for fila in matriz:
        print(fila)

if __name__ == "__main__":
    main()

print = int(input("elige la fila donde va a caer la bomba para el enemigo: "))
print = int(input("elige la columna donde va a caer la bomba para el enemigo: "))