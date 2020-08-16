#----------------------Ejercicio 1a---------------------------------------
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
#-----------------------------Ejercicio 1b Suma de matrices-----------------------

def matrix_format(row, col, letra):
    """
    Parameters
    ----------
    row : int
        Argumento que se recibe para saber el número de renglones de la matriz A 
    col : int
        Argumento que se recibe para saber el número de columnas de la matriz B 
    Returns
    -------
    matriz : 2D-list
        formato de la matriz como lista bidimensional que contiene los datos ingresados por el usuario.
    """
    print("Introduce los números de la matriz" + letra + ": ")
    matriz = [[ int (input()) for i in range (col)] for j in range(row)]
    print("Matriz" + letra + ": ")
    for i in range (row):
        for j in range (col):
            print(format(matriz[i][j]," "), end = "")
        print()
    return matriz



def matrixRes_format(row1,col1,res1): #Método auxiliar 
    """
    Parameters
    ----------
    row1 : int
    col1 : int
    res1 : 2D-list
    Returns
    -------
    formato de la matriz resultante.
    """
    print("El resultado es:")
    for i in range(row1):
        for j in range (col1):
            print(format(res1[i][j], " "), end= "")
        print()
    
def matrix_sum():
    """
    Returns
    -------
    2D-list 
        lista bidimensional con la matriz resultante de sumar las matrices A y B.
    """
    row = int (input("Intrdouce el número de renglones de la Matriz A: " ))
    col = int (input("Intrdouce el número de columnas de la Matriz B: " ))
    matrizA =  matrix_format(row, col, "A")
    matrizB = matrix_format(row, col, "B")
    
    res = [[0 for i in range (col)]  for j in range (row) ] #Resultado

    for i in range(row):
        for j in range (col):
                res[i][j] = matrizA[i][j] + matrizB[i][j] # inicialmente res[i][j] = 0
            
    return matrixRes_format(row,col,res)

matrix_sum()


#----------------------------------#Ejercicio 3---------------------------------------------------------
def interseccion(list1,list2):
    """
    Parameters
    ----------
    list1 : list
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
             res = (list1[1] == list2[j])
             j += 1
        i += 1
        return res
                
print(interseccion(["alana","kevin","rob","mike"], ["Georgia","Eva","Felix"]))




# --------------- Ejercicio 5 ---------------------------
import random

def tiraDados(n):
       
    '''
    función: tiraDados(n)
    args:
        n (int) : argumento que se recibe para saber cuántas veces se quieren tirar los dos dados.
        
    output:
        tuplas (dict): diccionario que contiene como llaves las tuplas de los distintos
        valores que pueden tomar los dados y cuyo valor es las veces que salió la tupla de valores
        dentro de los n tiros.
    '''
    try:
        
        n = int(n)
        print('entra bien')
        tuplas = {}
        for i in range (0,n):
            # simulamos de forma independiente los tiros ya que tirar uno no afecta el tiro del otro
            d1 = simulaTiro()
            d2 = simulaTiro()
            valores = (d1,d2) # convertimos los valores del dado 1 y el dado 2 en una tupla
            if valores in tuplas: #vemos si ya existe esa llave en el diccionario
                tuplas[valores] += 1 #Si ya existe le sumo 1 a la cantidad de veces que ha aparecido
            else:
                tuplas[valores] = 1 #Si no existe, inicialzo su valor en 1 vez ya que es su primera aparición
        
        return tuplas #una vez que terminamos los n tiros, regresamos el diccionario con los valores y su
        #cantidad de apariciones
    except:
        print('Parece ser que el tipo de dato que ingresaste no es correcto. Inténtalo de nuevo')
        n = input('Escribe el número de veces que quieres tirar los dados: ')
        return tiraDados(n)

        
    
            
def simulaTiro():
    return random.randint(1,6)

n = input('Escribe el número de veces que quieres tirar los dados: ')
tiraDados(n)

#-----------------------Ejercicio 6  ------------------
def matrix_product():
    """
    Returns
    -------
    2D-list
        lista bidimensional con la matriz resultante de la multiplicacion de las matrices A y B.
    """
    p = int (input("Intrdouce el número de renglones de la Matriz A: " ))
    q = int (input("Intrdouce el número de columnas de la Matriz B: " ))
    n = int (input("Intrdouce el número de columnas de la Matriz A/el número de renglones de la matriz B: " ))
    
    matrizA = matrix_format(p, n, 'A')
    matrizB = matrix_format(n, q, 'B')

    res = [[0 for i in range (q)]  for j in range (n) ]

    for i in range(p):
        for j in range (q):
            for k in range (n):
                res[i][j] = res[i][j] + matrizA[i][k] * matrizB[k][j] # inicialmente res[i][j] = 0
    
    return matrixRes_format(p,q,res)

matrix_product()
#---------------------- Ejercicio 7 --------------------------

#7. Un programa que contenga una función que reciba dos cadenas de caracteres, cuente y regrese
#la cantidad de veces que aparece la segunda cadena en la primera. Por ejemplo, si la primera
#cadena es 'azcbobobegghakl' y la segunda ´bob´, entonces la función regresará un dos.
#El programa deberá imprimir:
#Cantidad de veces que bob ocurre es: 2 


import regex as re

def count2in1(str1,str2):
    '''
    función count2in1(str1,str2):
        inputs:
            str1 (str): cadena de caracteres donde vamos a buscar el patrón definido en el str2.
            str2 (str): cadena de caracteres que será el patrón a buscar en el str1.
            
    '''
    matches = re.findall(str2,str1,overlapped=True) #Usamos la libería de regular expressions para buscar el patrón definido en str2 dentro de str1 permitiendo superposición
    message = "Cantidad de veces que '{}' ocurre es: {}".format(str2,len(matches))
    print(message)
    

s1 = str(input('Escribe la cadena donde quieres buscar: '))
s2 = str(input('Escribe la cadena que quieres buscar: '))

count2in1(s1,s2)

#--------------Ejercicio 8--------------------------------

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


#------------------------ Ejercicio 9 -----------------------

def cantvalores(d):
    count = valores(d)
    return count #le restamos el valor del diccionario global
    
def valores(elem): 
    '''
    function: valores(elem)
    input: 
        elem (any): elem puede ser cualquier tipo de dato, se consideran diccionarios, listas, tuplas, conjuntos,
        enteros, strings y floats. Es importante recalcar que cualquier valor que no sea un iterable (listas, tuplas, conjuntos)
        o un diccionario será tomado como un valor atómico, es decir, será tratado igual que los enteros, strings y floats.
    output:
        ans (int): regresa el conteo final de las llamadas recursivas para recorrer los anidamientos.
    '''
    if type(elem)==dict: 
        if elem:
            ans = 0
            for key in elem.keys(): #si el elemento es un diccionario no-vacío, recorremos cada llave
                ans += valores(elem[key])
            return ans #devolvemos los elementos anidados dentro del diccionario más el diccionario en sí
        else:
            return 0 #si el diccionario está vacío, regresamos 0 porque no contiene nada

    elif isIterable(elem): #llamamos a la función isIterable para ver si elem es un tipo iterable con el propósito de ver
        # si podemos recorrer sus valores o no
        if elem:
            ans = 0
            for val in elem:
                ans += valores(val)
            return ans 
        else:
            return 0 #si la lista está vacía, regresamos 0 porque no contiene nada
    else:
        return 1
            
        
            
def isIterable(elem):
    '''
    function isIterable(elem)
    input:
        elem (any): el elemento del cual deseamos conocer su naturaleza.
    '''
    tipo = type(elem)
    if tipo == list or tipo == tuple or tipo == set:
        return True #Es un tipo iterable
    else:
        return False #No es un tipo iterable

d = {'a': [2,3,4,[6,7,8]], 'b':{'c':[1,2,3,(4,5),'o']}}
print(cantvalores(d))

d = {1: [{3:[4,{5,6}]}]}
print(cantvalores(d))


#----------------- Ejercicio 10 -----------

def checaOrdenLex(str1,str2):  #Función que revisa que la primera cadena sea lexicográficamente menor que la segunda
    return True if str1<str2 else False

def inRange(s1,s2,cl): #Función que revisa si la clave cl se encuentra en el rango lexicográfico entre s1 y s2
    return (cl>=s1 and cl<=s2)

def procesa_archivo(str1,str2):
    '''
    función procesa_archivo(str1,str2)
        inputs
            str1 (str): cadena 1 que indica el límite inferior de las palabras
            str2 (str): cadena 2 que indica el límite superior de las palabras
        output:
            output_file (.txt): archivo .txt que contiene las palabras de las lineas
            cuyas claves estaban en el rango [str1,str2]
    '''
    text_file = open('datos_10.txt', "r",encoding='UTF-8') #Lee el archivo con encoding utf-8 para acentos
    lines = text_file.readlines() #guardamos linea por linea en una lista
    output_lines = [] #inicializamos lista vacía para las líneas que se vayan a incluir en el output
    
    for line in lines: #Recorremos linea por lista en la lista de lineas
        line = line.strip() #cuidamos no leer espacios en blanco al inicio y al final
        clave_lex = line[:7] #guardamos los primeros 7 caracteres como clave lexográfica
        if inRange(str1,str2,clave_lex): #llamamos función in range para checar si está en el rango de str1 y str2
            output_lines.append(line+'\n') #en caso de que esté, lo guardamos en la lista de output lines
            
    output_file = open("output.txt","w+",encoding='UTF-8') #creamos archivo output.txt con permisos de escritura
    output_file.writelines(output_lines) #escribimos las líneas que están en output lines
    output_file.close() #cerramos el archivo
    print('Puedes encontrar el output en el archivo output.txt')

def lee_palabras():
    '''
    funcion lee_palabras()
    
    Esta función no recibe inputs ni outputs porque su único propósito es leer del teclado las palabras
    que definirán el rango. Checa las condiciones especificadas en el problema:
    1. Que las dos palabras tengan longitud menor o igual a 7.
    2. Que la primera palabra sea lexicográficamente menor que la segunda.
    '''
    str1 = str(input('Ingresa una cadena de tamaño menor o igual a 7 para definir un límite inferior: '))
    str2 = str(input('Ingresa una cadena de tamaño menor o igual a 7 para definir un límite superior: '))
    
    if len(str1)>7 or len(str2)>7: #checamos tamaño
        print('Una de las palabras que ingresaste es mayor a 7 caracteres, vuelve a intentarlo.')
        lee_palabras()
    else:
        if not checaOrdenLex(str1,str2): #checamos el que el orden de str1 sea menor a str2
            print('Parece ser que la segunda palabra es lexicográficamente mayor que la primera, vuelve a intentarlo.')
            lee_palabras()
        else:
            procesa_archivo(str1,str2) #si todo está bien, pasamos a la función procesa archivo

lee_palabras()