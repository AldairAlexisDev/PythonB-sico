#BUCLE FOR
"""
#IMPRIMIR NUMEROS DEL 1 AL 10
for i in range(1,11): #Comienza en 1 y termina en 10
                      #Desde 1 considerandolo hasta 11
    print(i)


#Suma de Números del 1 al 10:
suma = 0
for i in range(1,11):
    suma+=i
print("La suma es: ", suma)


#Contar Vocales en una Cadena:
texto = input("Ingresa un texto: ")
contador = 0

for letra in texto:
    if letra.lower() in "aeiou": #Transformamos las letras a minusculas
                                 #luego verificamos si estan dentro del texto
        contador +=1   #contamos
print("Total de vocales: ",contador)

#Imprimir caracteres de una palabra en orden inverso:
palabra = input("Ingresa una palabra: ")
for inverso in reversed(palabra):
    print(inverso)
"""

#BUCLE WHILE

#Contar del 1 al 5
"""contador = 1
while contador <= 5:
    print(contador)
    contador += 1   #Si son impares se van aumentando de +=2
"""
#MENU

def mostrar_menu():
    print("=== POKEMONS === / 5 para salir")
    print("1. Charizard")
    print("2. Pikachu")
    print("3. Squitle")
    print("4. Caterpie")
    

opcion =""

while opcion != "5":
    mostrar_menu()
    opcion = input("Escoge un pokemon para ver sus detalles: ")

    if opcion == "1":
        print("Tipo: Fuego\nPoder: 100")
    elif opcion == "2":
        print("Tipo: Electrico\nPoder: 80")
    elif opcion == "3":
        print("Tipo: Agua\nPoder: 90")
    elif opcion == "4":
        print("Tipo: Planta\nPoder: 70")
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Seleccione una opcion del 1 al 5")
        continue

    
    input("Ingrese 'R' para regresar al menú principal...: ")