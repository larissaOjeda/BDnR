# -*- coding: utf-8 -*-
"""
@author: larissa
"""

#Ejerciccio 3 (Este ta re bien según io c: ) 
def interseccion(list1,list2):
        res = False
        for x in list1: 
            for y in list2: 
                if x == y: 
                    res = True 
                    return res
                
print(interseccion(["alana","kevin","rob","mike"], ["Georgia","Eva","Felix"]))
                    
#Ejercicio 6 (Si jala pero hay que hacer funciones pa que quede más bello c: )
#Tal vez para este ejercicio convendría escribir la función multiplicacionValida y otra llamada multiplicacion
#de manera que el resultado solo mande llamar a la funcion multiplicacion para que se vea mas modular el código 
p = int (input("Intrdouce el número de renglones de la Matriz A: " ))
q = int (input("Intrdouce el número de columnas de la Matriz B: " ))
n = int (input("Intrdouce el número de columnas de la Matriz A/el número de renglones de la matriz B: " ))

#Formato de la matriz A 
print("Introduce los números de la matriz A: ")
matrizA = [[ int (input()) for i in range (n)] for j in range(p)]
print("MatrizA: ")
for i in range (p):
    for j in range (n):
        print(format(matrizA[i][j]," "), end = "")
    print()

#Formato de la matriz B 
print("Introduce los números de la matriz B: ")
matrizB = [[int(input()) for i in range (q)] for j in range(n)]
print("MatrizB: ")
for i in range (n):
    for j in range (q):
        print(format(matrizB[i][j]," "), end = "")
    print()
    
#Resultado
res = [[0 for i in range (q)]  for j in range (n) ]

for i in range(p):
    for j in range (q):
        for k in range (n):
            res[i][j] = res[i][j] + matrizA[i][k] * matrizB[k][j] # inicialmente res[i][j] = 0
        
print("El resultado es:")
for i in range(p):
    for j in range (q):
        print(format(res[i][j], " "), end= "")
    print()
    

#Ejercicio 8 (más o menos falta revisar lo de leer el archivo bien c:  ) 
def word_counter (filepath):
    text_file = open("textFile.txt", "r") #Lee el archivo
    data = text_file.read()
    words = data.split()  #Separa un string en una lista donde cada palabra es un elemento de la lista 
    counts = dict()  #crea un diccionario 
    for word in words : #ciclo para recorrer cada palabra del texto 
        if word in counts: 
            counts[word] += 1 #Si la palabra ya se encontraba en counts entonces se suma una unidad a la cuenta 
        else: 
            counts[word] = 1  #Si es una palabra nueva entonces incializa su cuenta en 1 
    return counts #regresa el diccionario con el número de veces que se repite cada palabra




