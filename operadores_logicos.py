x = 2
y = 2
z = 5

print("COMPARACIONES")

#IGUALDAD - "x es igual que y/z"
print(x == y) #TRUE
print(x == z) #FALSE
 
#NO ES IGUAL / DIFERENTE QUE -  "x es diferente que z/y"
print (x != z) #TRUE
print (x != y) #FALSE 

#MAYOR - "x es mayor que y / z"
print (x > y) #FALSE
print (x > z) #FALSE

#MENOR - "x es menor que y / z"
print (x < y)
print (x < z)

#MAYOR IGUAL - "x es mayor o igual que y"
print (x >= y)

#MENOR IGUAL - "x es menor o igual que y"
print (x <= y)


print("OPERADORES LOGICOS")

# and
print (x < z and x > 1) # TRUE porque ambas comparaciones son verdaderas
print (x > y and z > x) # FALSE porque x no es mayor que y

# or
print (x <= y or z < x) #TRUE porque si solo uno es verdad ya se cumple.
print (x < y or x > z) #FALSE porque ninguna comparación es verdadera

# not
print(not(x < z and x > 1)) #Esta compración devuelve True pero al tener el not delante
                            #cambia a lo contrario, es decir sería FALSE