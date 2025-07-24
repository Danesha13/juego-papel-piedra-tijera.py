# Juego: Piedra, Papel o Tijeras (2 jugadores)
# # Pedir los nombres de los jugadores
nombre1 = input("¿Cómo se llamará el jugador 1?: ")
nombre2 = input("¿Cómo se llamará el jugador 2?: ")

# Pedir las elecciones (en minúsculas)
jugador1 = input(f"{nombre1}, ¿qué eliges? ¿Piedra, papel o tijeras?: ").lower()
jugador2 = input(f"{nombre2}, ¿qué eliges? ¿Piedra, papel o tijeras?: ").lower()

# Determinar condiciones de victoria para jugador1
condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

# Verificar resultado
if jugador1 == jugador2:
    print("🟰 ¡Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print(f"🏆 Ha ganado: {nombre1}")
else:
    print(f"🏆 Ha ganado: {nombre2}")
