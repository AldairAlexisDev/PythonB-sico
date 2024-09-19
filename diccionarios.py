
dic = {
    "Yellow":"Amarillo",
    "Blue":"Azul",
    "Red":"Rojo"
}

print(dic)

#Busqueda de valores
print(dic["Blue"])

#Modificar valores
dic["Red"] = "White"
dic.update({"Blue":"Azul Claro"})

#Eliminar un elemento
del dic["Blue"]
dic.pop("Yellow")