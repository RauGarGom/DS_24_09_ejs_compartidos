import random as rd

## Ej 1
def num_to_days (num):
    conversor = {1: "Lunes",2: "Martes",3:"Miércoles",4: "Jueves",5:"Viernes",6:"Sábado",7:"Domingo"}
    return (conversor[num])

## Ej 2
def pyramid(num):
    num_left = num
    num_list = []
    x = 0
    while num_left > 0:
        num_list.append(num_left)
        num_left -= 1
    print(f"Lista original: {num_list}")
    while x < len(num_list):
        print(*num_list[x:])
        x += 1

## Ej 3
def comparison (first,second):
    if first > second:
        return(f"{first} es mayor que {second}")
    elif first < second:
        return(f"{first} es menor que {second}")
    elif first == second:
        return(f"{first} es igual a {second}")
    
## Ej 4
def counter(text,letter):
    result = 0
    text_low = text.lower()
    letter_low = letter.lower()
    for x in text_low:
        if x == letter_low:
            result += 1
    return(f'La letra "{letter}" aparece {result} veces en el texto "{text}"')

## Ej 5
def word_count(text):
    counter_5 = {}
    for x in text:
        if x not in counter_5:
            counter_5[x] = 1
        else:
            counter_5[x] += 1
    return(counter_5)

## Ej 6
def modifier(in_list,in_command,in_element = None):
    if in_element == None:
        return("No hay elementos a agregar o eliminar")
    elif in_command == "add":
        in_list.append(in_element)
        return (print(in_list))
    elif in_command == "remove":
        in_list.remove(in_element)
        return(print(in_list))
    
## Ej 7
def sentencer(*args):
    sentence = ""
    for x in args:
        sentence += x + " "
    sentence = sentence
    return(sentence)
sentencer("hola,","esto","es","una","frase")

## Ej 8
def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

## Ej 9
def sq_area(len_sq):
    return(len_sq**2)

def tr_area(base_tr,height_tr):
    return(base_tr*height_tr/2)

def cr_area(rad_cr):
    import math
    pi = math.pi
    return(round(pi*rad_cr**2))
