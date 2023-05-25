import math

def calcular_distancia(ciudad_origen, ciudad_destino):
    # Distancias en kilómetros
    distancias = {
        "Santiago": 350,
        "Ovalle": 400
    }
    distancia = abs(distancias[ciudad_origen] - distancias[ciudad_destino])
    return distancia

def calcular_duracion(distancia):
    velocidad_promedio = 80  # km/h
    tiempo = distancia / velocidad_promedio
    horas = int(tiempo)
    minutos = int((tiempo * 60) % 60)
    segundos = int((tiempo * 3600) % 60)
    return horas, minutos, segundos

def calcular_combustible(distancia):
    rendimiento = 12  # km/l
    litros = distancia / rendimiento
    return litros

while True:
    origen = input("Ciudad de Origen (q para salir): ")
    if origen == "q":
        break

    destino = input("Ciudad de Destino (q para salir): ")
    if destino == "q":
        break

    distancia = calcular_distancia(origen, destino)
    duracion_horas, duracion_minutos, duracion_segundos = calcular_duracion(distancia)
    combustible = calcular_combustible(distancia)

    print("--------------------------------------------------")
    print("Narrativa del Viaje:")
    print(f"Desde {origen} hasta {destino}")
    print(f"Distancia: {distancia:.2f} km")
    print(f"Duración: {duracion_horas} horas, {duracion_minutos} minutos, {duracion_segundos} segundos")
    print(f"Combustible requerido: {combustible:.2f} litros")
    print("--------------------------------------------------")

print("¡Hasta luego!")