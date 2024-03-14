with open("listaordenada.txt") as file:
    def ordenarlista(lista):
     """ Esta función recibe una lista de numeros y los ordena de mayor a menor"""

     """Parámetros:
     -lista: recibe una lista de str con este formato:
        ["1","2","3","4"]"""

     """Salida:
        -La función no devuelve nada"""
    
    x=int(input("Escriba numeros enteros"))
    numeros = []
    while True:
        numeros.append(x)
        numeros.sort()
        for i in numeros:
            print(i)


        file.write(numeros)

 
       



