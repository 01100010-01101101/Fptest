
# dd=100000

# while True:
#     print("""
#           1.- Pago de Tarjeta de Crédito:
#           2.- Simulación de Compras:
#           3.- Salir
#           """)
#     op=int(input("Seleccione una opcion"))
#     match op:
#         case 1:
#             print("Su deud actual es de ", dd)
#             pago=int(input())
#             if pago<=0 or pago>dd:
#                 print("El pago debe ser mayor a cero y menor que la deuda")
#             else:
#                 dd=dd-pago
#             print("El saldo a pagar es ", dd)
#         case 2:
#             while True :
#                 print("""Seleccione un item
#                     1.- Monitor
#                     2.- Teclalo
#                     3.- Laptop
#                     4.Salir
#                     """)
#                 ops=int(input())
#                 match ops:
#                     case 1:
#                        valor=80000
#                        dd=valor+dd
#                        print("Usted añadio un nuevo articulo, su nuevo salfo es ", dd)
#                     case 2:
#                         valor=50000
#                         dd=valor+dd
#                         print("Usted añadio un nuevo articulo, su nuevo salfo es ", dd)
#                     case 3:
#                         valor=1180000
#                         dd=valor+dd
#                         print("Usted añadio un nuevo articulo, su nuevo salfo es ", dd)
#                     case 4:
#                         print("Gracias por su compra")
#                         break
#                     case _:
#                         print("Seleccione una opcion valida 1-3")
#         case 3:
#             print("Gracias por usar el sistema de Crédito")
#             break
#         case _:
#             print("Seleccione una opcion valida 1-3")
    
    
#################################################################


# num = int(input("ingresa un numero: "))
# print(f'cuenta regresiva desde {num}:')
# for i in range(num,num -5, -1):
#     print(i)    
    

######################################

us1 = ""
us2 = ""
us3 = ""
pass1 = ""
pass2 = ""
pass3 = ""



while True:
    print("""Seleccione una opcion:
          1. Registrar
          2. Iniciar sesion
          3. Salir
          """)    
    op = int(input("ingresa una opcion valida"))
    match op:
        case 1:
            print("Ingrese su nombre de usuario")
            us1 = input()
            us2 = input()
            us3 = input()
            if us1 and us2 and us3 == "":
                print("No existen usuarios todavia")
                print("Si no tiene una cuenta creada, cree una")
            else:
                us = input()
        case 2:
            while True:
                print("""Seleccione una opcion:
                      1. Registrar usuario
                      2. Crear contraseña
                      3. Salir
                      """)        
                ops = int(input())
                match ops:
                    case 1:
                        print("ingrese usuario nuevo")
                        usu = input()
                        print("usted creo un nuevo usuario")
                        if usu  
            