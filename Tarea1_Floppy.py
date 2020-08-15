# -*- coding: utf-8 -*-
"""
@author: larissa
"""

#Ejercicio 1a 
def desplaza_lista(k, lista):
    """
    Parameters
    ----------
    k : int 
        cantidad de lugares a desplazar (un valor positivo indica desplazar a la derecha; un valor negativo, a la izquierda.)
    lista : list
        lista que se desea desplazar (girar).

    Returns
    -------
    lista : list
        lista desplazada 'k' lugares a la derecha o izquierda. 
    """
    if k < 0: 
        for i in range (abs(k)):  #Se trata de girar la lista 
            lista.append(lista.pop(0))
    else: 
        for i in range(k):
            lista.insert(0,lista.pop())
    return lista


print (desplaza_lista (-2, [1,6,6,2,8,0] ) )  


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def matrix_format(row, col):
    print("Introduce los números de la matriz A: ")
    matrizA = [[ int (input()) for i in range (col)] for j in range(row)]
    print("MatrizA: ")
    for i in range (row):
        for j in range (col):
            print(format(matrizA[i][j]," "), end = "")
        print()
        
    print("Introduce los números de la matriz B: ")
    matrizB = [[int(input()) for i in range (col)] for j in range(row)]
    print("MatrizB: ")
    for i in range (row):
        for j in range (col):
            print(format(matrizB[i][j]," "), end = "")
        print()
    return matrizA, matrizB 


#Ejercicio 1b Suma de matrices
def matrix_sum():
    row = int (input("Intrdouce el número de renglones de la Matriz A: " ))
    col = int (input("Intrdouce el número de columnas de la Matriz B: " ))
    matrizA, matrizB =  matrix_format(row, col)
    
    res = [[0 for i in range (col)]  for j in range (row) ] #Resultado

    for i in range(row):
        for j in range (col):
                res[i][j] = matrizA[i][j] + matrizB[i][j] # inicialmente res[i][j] = 0
    
    print("El resultado es:")
    for i in range(row):
        for j in range (col):
            print(format(res[i][j], " "), end= "")
        print()
    return res

matrix_sum()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ejerciccio 3 
def interseccion(list1,list2):
    """
    Parameters
    ----------
    list1 : List
        primera lista que recibe para la intersección
    list2 : list
        segunda lista con la cual se realizará la interseccion.

    Returns
    -------
    res : boolean
        variable True en caso de que list1 y list2 tengan al menos 1 elemeto en común entre ellas y False en caso contrario. 
    """
    n = len(list1)
    m = len(list2)
    i = 0
    j = 0
    res = False
    while i < n and not res: 
        while j <m and not res:
             res = (list[1] == list2[j])
             j += 1
        i += 1
        return res
                
print(interseccion(["alana","kevin","rob","mike"], ["Georgia","Eva","Felix"]))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 6
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
    
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Ejercicio 8 (más o menos falta revisar el checar el archivo)  
def word_counter (filepath):
    """
    Parameters
    ----------
    filepath : path
        Ruta del archivo que se quiere leer para contar las palabras 

    Returns
    -------
    res : int 
        número de palabras distintas obtenido de contar las llaves del diccionario 'counts'. 
        En counts cada llave es una palabra y tiene asignado un int que indica el número de repeticiones de esa palabra en el texto. 
    """
    if filepath.split('.')[-1] != 'txt':
        print ("El archivo que ingresaste no tiene la extensión correcta, inténtalo de nuevo: ")
        fp = str(input("Ingresa el filepath del archivo .txt que desees leer"))
        return word_counter(fp)
    else:
        text_file = open("textFile.txt", "r") #Lee el archivo
        data = text_file.read()
        words = data.split()  #Separa un string en una lista donde cada palabra es un elemento de la lista 
        counts = dict()  #crea un diccionario 
        res = 0
        
        for word in words : #ciclo para recorrer cada palabra del texto 
            word = word.lower()
            if word in counts: 
                counts[word] += 1 #Si la palabra ya se encontraba en counts entonces se suma una unidad a la cuenta 
            else: 
                counts[word] = 1  #Si es una palabra nueva entonces incializa su cuenta en 1 
        res = len(counts.keys()) #Cuenta el número de llaves del diccionario counts para saber las palabras distintas 
    return res #regresa el numero de palabras distintas 
