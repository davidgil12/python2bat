import random

minimo = 1
maximo = 10


numeroElegido = random.randint(minimo,maximo)

numeroPedido = int(input(f"Elige un numero entre {minimo} y {maximo}"))
if numeroElegido == numeroPedido:
    print("Enhorabuena!")
else:
    print(f"Mala suerte, no has acertado! era el {numeroElegido}")
    

