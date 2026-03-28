# =============================================================
# Sistema de cronometraje para competencia de natacion
# =============================================================

# --- Datos de los nadadores (nombre, tiempo en segundos) ---
nadadores = [
    {"nombre": "Lucas Perez",    "tiempo": 58.34},
    {"nombre": "Sofia Gomez",    "tiempo": 55.12},
    {"nombre": "Martin Torres",  "tiempo": 60.05},
    {"nombre": "Valentina Ruiz", "tiempo": 53.87},
    {"nombre": "Elias Jacob","tiempo": 57.21},
]

# --- Funcion: convertir segundos a formato MM:SS.cc ---
def formatear_tiempo(segundos):
    minutos = int(segundos // 60)
    segs    = segundos % 60
    return f"{minutos:02d}:{segs:05.2f}"

# --- Funcion: ordenar nadadores por tiempo (burbuja) ---
def ordenar_por_tiempo(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j]["tiempo"] > lista[j + 1]["tiempo"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# --- Funcion: calcular promedio ---
def calcular_promedio(lista):
    total = 0
    for nadador in lista:
        total += nadador["tiempo"]
    return total / len(lista)

# --- Funcion: mostrar resultados con medallas ---
def mostrar_resultados(lista):
    medallas = ["Oro", "Plata", "Bronce"]
    print("\n===== RESULTADOS DE LA COMPETENCIA =====")
    print(f"{'Pos':<5} {'Nadador':<22} {'Tiempo':<12} {'Medalla'}")
    print("-" * 50)
    for i, nadador in enumerate(lista):
        tiempo_fmt = formatear_tiempo(nadador["tiempo"])
        medalla    = medallas[i] if i < 3 else "-"
        print(f"{i+1:<5} {nadador['nombre']:<22} {tiempo_fmt:<12} {medalla}")
    print("-" * 50)
    promedio = calcular_promedio(lista)
    print(f"  Tiempo promedio: {formatear_tiempo(promedio)}")
    print(f"  Ganador: {lista[0]['nombre']} con {formatear_tiempo(lista[0]['tiempo'])}")
    print("=========================================\n")

# --- Programa principal (flujo imperativo paso a paso) ---
clasificados = ordenar_por_tiempo(nadadores)
mostrar_resultados(clasificados)
