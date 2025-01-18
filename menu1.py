
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

# us1 = ""
# us2 = ""
# us3 = ""
# pass1 = ""
# pass2 = ""
# pass3 = ""



# while True:
#     print("""Seleccione una opcion:
#           1. Registrar
#           2. Iniciar sesion
#           3. Salir
#           """)    
#     op = int(input("ingresa una opcion valida"))
#     match op:
#         case 1:
#             print("Ingrese su nombre de usuario")
#             us1 = input()
#             us2 = input()
#             us3 = input()
#             if us1 and us2 and us3 == "":
#                 print("No existen usuarios todavia")
#                 print("Si no tiene una cuenta creada, cree una")
#             else:
#                 us = input()
#         case 2:
#             while True:
#                 print("""Seleccione una opcion:
#                       1. Registrar usuario
#                       2. Crear contraseña
#                       3. Salir
#                       """)        
#                 ops = int(input())
#                 match ops:
#                     case 1:
#                         print("ingrese usuario nuevo")
#                         usu = input()
#                         print("usted creo un nuevo usuario")
#                         if usu  




##################################################################


# Realizar uan ruleta Rusa
# el barril del arma tiene 6 cavidades, deben ser solo 2 jugadores por turnos,
# cadda uno debe disparar. pierde a quien el toca la bala


# import random
# import time


# jug1 = 0
# jug2 = 0

# def ruleta():
#     return random.randint(1,6)

# print("Bienvenido a la Ruleta Rusa")
# bala = ruleta()


# for p in range(2):
#     print("Turno del jugador", p + 1)
#     print("Para disparar presione '0' ")
#     mov = input()
#     if mov == '0':
#         time.sleep(1)
#         print("*")
#         time.sleep(1)
#         print("*")
#         time.sleep(1)
#         print("*")
#         if p + 1 == bala:
#             print("BANG!")
#             break
#         else:
#             print("Sigue jugando.")
            
            
        
       
    ######################################
    
    
# Crear juego de pelea
# Solo 2 jugadores, caga jugador comienza con 60 de HP(puntos de vida)
# Cada ataque es por turnos, cada ataque infringe entre 2 y 10 de daño
# La pelea termina cuando uno de los jugadores llega a 0 Hp(puntos de vida)    
# Bonus: puede haber la posibilidad des que se haga u daño critico, vale decir, infringe 1.6 de daño


import random

vidajg1 = 60
vidajg2 = 60



print(" La pelea a comenzado")
print("Jugador 1",vidajg1)
print("Jugador 2",vidajg2)




while vidajg1 > 0 and vidajg2 > 0:
    input("Jugador 1, presiona 'P' para pegar: ")
    daño_jug1 = random.randint(2,10)
    vidajg2 -= daño_jug1
    print("Jugador 2 pierdes puntos de vida", daño_jug1," de daño")
    
    if vidajg2 <= 0:
        print("Jugador 1, has ganado la pelea")
        break
    print("Jugador 1",vidajg1)
    print("Jugador 2",vidajg2)
    
    
    input("Jugador 2, presiona 'P' para pegar: ")
    daño_jug2 = random.randint(2,10)
    vidajg1 -= daño_jug2
    print("Jugador 1 pierdes puntos de vida", daño_jug2,"de daño")
    
    if vidajg1 <= 0:
        print("Jugador 2, has ganado la pelea")
        break 
    print("Jugador 1",vidajg1)
    print("Jugador 2",vidajg2)
    
print("Finaliza la pelea")    
    
        























           