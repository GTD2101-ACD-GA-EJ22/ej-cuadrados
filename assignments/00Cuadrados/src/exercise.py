def sumaCuadrados(n):
    """ Esta función calcula
        la suma de n valores cuadrados
    """
    
    suma = 0
    for i in range(1,n+1):
        suma += i ** 2
    return suma

def main():
    #escribe tu código abajo de esta línea
    n=int(input("N:"))

    print(f"La suma de cuadrados desde 1 hasta {n:3} es: {sumaCuadrados(n):3}")

if __name__=='__main__':
    main()
