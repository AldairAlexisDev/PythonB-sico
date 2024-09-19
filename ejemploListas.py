
clientes = [
    {"cuenta":"111111" ,"apellido": "Medina","nombre":"Alexis","saldo":10000},
    {"cuenta":"111112" ,"apellido": "Cisneros","nombre":"Jade","saldo":20000},
    {"cuenta":"111113" ,"apellido": "Paucar","nombre":"Angie","saldo":24000},
    {"cuenta":"111114" ,"apellido": "Condemayta","nombre":"Maribel","saldo":30000}
]

ingrese_cuenta = input("Ingrese su numero de cuenta: ")

for item in clientes:
    if ingrese_cuenta == item["cuenta"]:
        print("{} {} tu saldo actual es {}".format(item["nombre"], item["apellido"],item["saldo"]))
        break


