
from FUNCIONES_ISAIAS_SANTANA_APELLIDO_005 import menu, registrar_cliente, listar_clientes, registrar_compra, enviar_resumen_puntos

BD = []

print("¡Bienvenido al programa de puntos canjeables del Supermercado!")

while True:
    menu()
    opcion = input("Ingrese la opción a ejecutar: ")

    if opcion == "1":
        registrar_cliente(BD)

    elif opcion == "2":
        listar_clientes(BD)

    elif opcion == "3":
        registrar_compra(BD)

    elif opcion == "4":
        enviar_resumen_puntos(BD)

    elif opcion == "5":
        print("¡Hasta la próxima!")
        break

    else:
        print("Opción inválida. Por favor ingrese una opción válida.")
