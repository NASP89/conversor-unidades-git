def convertir():
    print("--- Conversor de Unidades ---")
    valor = input("Ingrese el valor a convertir: ")

    try:
        n = float(valor)
    except ValueError:
        print("Error: Debe ingresar un valor numérico.")
        return

    c_a_f = (n * 9/5) + 32
    m_a_km = n / 1000

    print(f"{n}°C equivale a {c_a_f}°F")
    print(f"{n} metros equivalen a {m_a_km} km")

if __name__ == "__main__":
    convertir()
#Fin del programa de conversion 