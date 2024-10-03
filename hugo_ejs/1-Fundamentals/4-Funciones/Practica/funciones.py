def convertidor (num):
    correspondencia = {1:"Lunes",2:"Martes", 3: "Miércoles", 4: "Jueves", 5 : "Viernes", 6 : "Sábado", 7 : "Domingo"}
    for key, value in correspondencia.items():
        if num == key:
            print (value)

def piramide(lista):
    while len(lista) > 0:
        print (str(lista).replace(",","").replace("[", "").replace("]",""))
        lista.pop(0)

def comparador (numero1,numero2):
    if numero1 == numero2:
        print("Son iguales")
    elif numero1 > numero2:
        print(numero1, "es mayor que", numero2)
    elif numero2 > numero1:
        print(numero1, "es menor que", numero2)


def contador (frase,letra):
    veces = 0
    veces = veces + frase.count(letra)
    letra = letra.upper()
    veces = veces + frase.count(letra)
    return print ("La letra", letra, "se repite:", veces, "veces.")

def contador2 (s):
    diccionario5 = {}
    string = str(s)
    conteo = len(string) - string.count(" ")
    diccionario5[string] = conteo
    return diccionario5

def listador (lista, comando: bool, elementos = None):
    listafinal = []
    lista = list(lista)
    if comando == "Add" or comando == "Remove":
        if comando == "Add":
            if elementos == None:
                return print("Falta elementos")
            elif elementos != None:
                lista.append(elementos)
                listafinal = lista
                return print(listafinal)
        if comando == "Remove":
            if elementos == None:
                return print("Falta elementos")
            elif elementos != None:
                lista.remove(elementos)
                listafinal = lista
                return print (listafinal)
    else:
        return print("Comando erróneo. Solo Add o Remove.")
    
def fraseador (*args):
    frase = ""
    print(frase)
    for palabra in args:
            frase += palabra + " "
    frase = frase[:-1]
    return frase

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1)  + fibonacci(n-2)



def cuadrado (lado):
    area = lado**2
    return area

def triangulo (base, altura):
    area = (base * altura)/2
    return area

def circulo (radio):
    import math
    area = (radio*math.pi)**2
    return area

