
#Verificar si una persona es mayor de edad:

"""edad = int(input("Ingrese su edad: "))

if(edad >= 18):
    print("Usted es mayor de edad.")
else:
    print("Usted aún es menor de edad.")"""


#Validación de usuario y contraseña:
"""
user = "alex"
password = "pass123"

input_user = input("Ingrese su usuario: ")
input_password = input("Ingrese su contraseña: ")

if user == input_user and password == input_password:
    print("Bienvenido " + user)
else:
    print("Usuario o contraseña incorrectos.")
"""

#Determinación de tipo de triángulo:
lado1 = int(input("Ingrese la longitud del primer lado: "))
lado2 = int(input("Ingrese la longitud del segundo lado: "))
lado3 = int(input("Ingrese la longitud del tercer lado: "))

if lado1 == lado2 == lado3:
    print("Es un triangulo equilatero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Es un triangulo isosceles.")
else:
    print("Es un triangulo escaleno.")
