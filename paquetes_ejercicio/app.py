from clientes.busqueda import buscar_cliente


def main():
    nombre = input("Nombre de cliente a buscar: ")
    cliente = buscar_cliente(nombre)
    if cliente:
        print(f"Cliente encontrado: {cliente}")
    else:
        print("Cliente no encontrado")


main()
