"""
paises = ["Perú","Chile","Bolivia","Colombia"]

#CRUD

#INSERCCION DE ELEMENTOS
paises.append("Brasil")

#Insertar en una posicion
paises.insert(3,"Argentina")

#Eliminar por posicion
paises.pop(3)
#Eliminar por nombre
paises.remove("Bolivia")
#Otra forma de eliminar
#del paises[3]
#Para eliminar todo
#paises.clear()

#Actualizar elemento de la lista
paises[0] = "Uruguay"

#Cantidad de elementos de una lista
print(len(paises))
print(paises)

#Rango de valores
nuevos_paises = paises[1:3] #imprime los paises que estan desde el 1 hasta el 3 sin considea la ultima
print(nuevos_paises)

nuevos_paises = paises[1:] #imprime desde la primera posicion
print(nuevos_paises)

nuevos_paises = paises[-1:] #imprime desde la ultima posicion
print(nuevos_paises)


#Checkear elementos
existe = "Brasil" in paises
print(existe) #Devuelve True

#Verificar e ingresar elementos en una lista
pais = input("Ingrese el pais: ")
if pais in paises:
    print("El pais ya existe en la lista.")
else:
    paises.append(pais)
    print("Se añadió correctamente el pais")
    print(paises)

#Ordenar Lista
paises.sort()
paises.reverse() #orddenar de manera reversa

#listado de elementos
for item in paises:
    print(item)

"""




