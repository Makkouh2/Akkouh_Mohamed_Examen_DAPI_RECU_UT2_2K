alimento=input("ingrese el nombre del alimento :")
cantidad= input("Ingrese la cantidad consumida(en gramos) :")
otro=input("¿Quieres registrar otro alimento? :")
diccionario={"alimento":alimento,"cantidad":cantidad}

if otro== "si":
    alimento=input("Ingrese el nombre del alimento :")
    cantidad= input("Ingrese la cantida consumida(en gramos) :")
    otro=input("¿Quieres registrar otro alimento? :")

if otro== "no":
   print("Resumen del consumo diario:", diccionario["alimento"], diccionario["cantidad"],"gramos")