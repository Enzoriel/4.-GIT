from matematicas.calculo_areas import calcular_area_circulo
from matematicas.operaciones import sumar


def main():
    sumar(5, 4)

    area = calcular_area_circulo(radio=5)
    print(f"Área del círculo: {area}")


main()
