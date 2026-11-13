class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ganados = 0
        self.perdidos = 0
        self.empates = 0
        self.puntos = 0


# Equipos ya establecidos
equipos = [
    Equipo("Gladiadores"),
    Equipo("Tiburones"),
    Equipo("Halcones"),
    Equipo("Toros"),
]

matriz = []  # cada fila: [ganados, perdidos, empates, puntos]

# Pedir los datos de cada equipo
for equipo in equipos:
    print(f"Equipo: {equipo.nombre}")

    while True:
        try:
            equipo.ganados = int(input("partidos ganados: "))
            break
        except ValueError:
            print("Debes escribir un número entero.")

    while True:
        try:
            equipo.perdidos = int(input("partidos perdidos: "))
            break
        except ValueError:
            print("Debes escribir un número entero.")

    while True:
        try:
            equipo.empates = int(input("partidos empatados: "))
            break
        except ValueError:
            print("Debes escribir un número entero.")

    # ganado = 3, empate = 1, perdido = 0
    equipo.puntos = equipo.ganados * 3 + equipo.empates * 1 + equipo.perdidos * 0

    matriz.append([equipo.ganados, equipo.perdidos, equipo.empates, equipo.puntos])
    print("-" * 30)

# Mostrar la matriz
print("MATRIZ (ganados, perdidos, empates, puntos)")
for i in range(len(equipos)):
    print(f"{equipos[i].nombre}: {matriz[i]}")

# Mostrar la tabla de posiciones
print("-" * 30)
print("TABLA DE POSICIONES")
for equipo in equipos:
    print(f"{equipo.nombre} -> G:{equipo.ganados} P:{equipo.perdidos} E:{equipo.empates} Puntos:{equipo.puntos}")

# Buscar los puntos más altos
mayor = equipos[0].puntos
for equipo in equipos:
    if equipo.puntos > mayor:
        mayor = equipo.puntos

# Guardar todos los equipos que tengan esos puntos
lideres = []
for equipo in equipos:
    if equipo.puntos == mayor:
        lideres.append(equipo)

print("-" * 30)
if len(lideres) == 1:
    print(f"El líder es {lideres[0].nombre} con {mayor} puntos")
else:
    print(f"Hay un empate en el primer lugar con {mayor} puntos:")
    for equipo in lideres:
        print(f"- {equipo.nombre}")
