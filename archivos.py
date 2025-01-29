


# import json
# # Datos JSON
# datos = {
# "nombre": "Esteban",
# "edad": 25,
# "comuna": "Santiago",
# "estudios": ["colegio Arturo Prat", "liceo el bosque",
# "Duoc UC", "Diplomado Duoc UC"]
# }
# # Abre el archivo, w es escritura
# with open('archivo.json', 'w') as archivo:
#     json.dump(datos, archivo)
# import json
# # Abrir archivo, r es permiso de lectura
# with open('archivo.json', 'r') as archivo:
#     datos_leidos = json.load(archivo)
# print(datos_leidos)



# fut = "algo mas de txt"

# lista = ["Mario","Luigi","Peach"]


# with open('mi archivo.txt', 'a') as archivo:
#     for i in lista:
#         archivo.write(f"{i}\n")




# datos = """Este es un archivo de texto simple que no tiene
# ningún formato en particular, lo podemos utilizar
# para guardar todo tipo de texto.
# """
# with open('archivo.txt', 'w') as archivo:
#     archivo.write(datos)








valor_cuenta = 0
variable_nombre = input("Cual es tu nombre: ")
print(f"Hola {variable_nombre}, que desea llevar hoy:")

compra = """                Opcion 1.- Arroz / Valor $3150
                Opcion 2.- Aceite / Valor $1990
                Opcion 3.- Queso / Valor $2150
                Opcion 4.- Leche / Valor $1190
                Opcion 5.- Salir del programa
             """
            
with open('archivo.txt', 'w') as archivo:
    archivo.write(compra)

try:
    while True:
        print(compra)
        opcion_usuario= int(input("Ingrese el numero del producto que desea comprar(o sleccione'5' para salir): "))
 
 
        match opcion_usuario:
 
            case 1:
        
                print("Usted ha elegido la opcion 1 - Arroz.")
        
                valor_cuenta += 3150
        
                print(f"El valor a pagar es: ${valor_cuenta}")
 
            case 2:
            
                print("Usted ha elegido la opcion 2 - Aceite.")
            
                valor_cuenta += 1990
            
                print(f"El valor a pagar es: ${valor_cuenta}")
            
            case 3:
            
                print("Usted ha elegido la opcion 3 - Queso.")
            
                valor_cuenta += 2150
            
                print(f"El valor a pagar es: ${valor_cuenta}")
                        
            case 4:
            
                print("Usted ha elegido la opcion 3 - Leche.")
            
                valor_cuenta += 1190
            
                print(f"El valor a pagar es: ${valor_cuenta}")
 
            case 5:
            
                print("Si no deseas llevar nada, presiona '5' para salir.") 
            
                break
            
        total_con_iva = valor_cuenta * 1.19
 
        print(f"El total a pagar, incluyendo el IVA del 19%, es: ${total_con_iva:.2f}")
 
except ValueError:
 
    print("Ha ingresado un dato incorrecto.")
    
    
    
    
    
 
