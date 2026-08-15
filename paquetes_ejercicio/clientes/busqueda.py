from clientes.datos import base_datos  # importación absoluta

# from .datos import base_datos  # importación relativa


def buscar_cliente(nombre):
    for cliente in base_datos["clientes"]:
        if cliente["Nombre"].lower() == nombre.lower():
            return f"{cliente['Nombre']} {cliente['Apellido']}"
    return None
