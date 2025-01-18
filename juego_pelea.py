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
    
        