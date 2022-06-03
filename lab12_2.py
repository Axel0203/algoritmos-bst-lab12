import random
import os
import tree as t
import bst12 as bst
from timeit import default_timer

lista = []
numeros_a_buscar = []
name_file = "C:/Users/Axel/Documents/COLLEGE/TECSUP/Estructura de datos y algoritmos/LAB12-Algoritmos/ejercicio2.txt"

for i in range(10001): # se crea la lista con 10000 numeros aleatorios entre 1 y 500000
    if i >= 1 and i <= 500000:
        lista.append(random.randint(1, 500000))

for i in range(50): # se crea la lista con 50 numeros aleatorios de la lista creada anteriormente
    numero_a_buscar = random.choice(lista)
    numeros_a_buscar.append(numero_a_buscar)

file = open(name_file, "w") # se escribe en el archivo ejercicio2.txt el contenido de la lista teniendo que cada elemento ocupará una linea	
for i in lista:
    file.write(str(i) + "\n")
file.close()

with open(name_file, "r") as file: # se lee el archivo ejercicio2.txt
    
    all_numbers = file.readlines() # se guarda en una lista todos los elementos que contiene el archivo

    all_numbers = [int(i.strip()) for i in all_numbers] # se usa strip para quitar los espacios en blanco de cada elemento de la lista dado que se tratan de cadenas con saltos de linea. Posteriormente, se iteran los elementos de la lista y se convierten a enteros usando int()

# Este dos impresiones por pantalla se realizaron para verificar la cantidad de elementos que las listas creadas tenían.
# print(len(all_numbers))
# print(len(numeros_a_buscar))

tree = bst.buildBSTFromArray(all_numbers) # se crea el arbol binario de busqueda a partir de la lista de numeros

# De la misma forma, este bloque de código fue usado para cotejar que el arbol haya sido creado correctamente.
# buf = []
# t.printLevelOrder(tree, buffer=buf)
# print(buf)

inicio = default_timer() # se inicia el contador de tiempo
resultado = bst.find(tree, numeros_a_buscar[0]) # se busca el primer elemento de la lista de numeros a buscar en el arbol binario de busqueda
fin = default_timer() # se termina el contador de tiempo

# busqueda de todos los elementos de la lista de numeros_a_buscar en el BST
# inicio = default_timer()
# for i in numeros_a_buscar:
#     resultado = bst.find(tree, i)
#     print(resultado)
# fin = default_timer()

if __name__ == "__main__":
    print("\nEl tiempo en segundos es: ",fin - inicio,"\n")
    print("\n\nEl resultado es: ",resultado,"\n")