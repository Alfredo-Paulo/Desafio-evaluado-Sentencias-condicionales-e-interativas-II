import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}
# ejecútalo en tu terminal con el comando"python mayor_a.py 40000"

def ventas_mayor_a(umbral):
    ventas_superiores = {}
    for mes, valor in ventas.items():
        if valor > umbral:
            ventas_superiores[mes] = valor
    return ventas_superiores

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python mayor_a.py <umbral>")
        sys.exit(1)

    umbral = int(sys.argv[1])
    resultado = ventas_mayor_a(umbral)
    print(resultado)
