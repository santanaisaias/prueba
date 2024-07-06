
def menu():
    opciones = [
        "Registrar Cliente",
        "Listar Clientes Registrados",
        "Registrar Compra",
        "Enviar Información de Puntos Acumulados a un Cliente",
        "Salir",
    ]
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")

def registrar_cliente(bd):
    nombre = input("Ingrese primer nombre del cliente: ").upper()
    apellido = input("Ingrese primer apellido del cliente: ").upper()
    correo = input("Ingrese correo electrónico del cliente: ")
    
    if nombre and apellido and correo:
        id_cliente = len(bd) + 1
        bd.append(
            {
                "nombre": nombre,
                "apellido": apellido,
                "correo": correo,
                "ID": id_cliente,
                "compras": []
            }
        )
        print("\n¡Se ha registrado un nuevo cliente en la base de datos!\n")
    else:
        print("Error: Todos los datos son obligatorios.")

def listar_clientes(bd):
    if not bd:
        print("\nNo hay clientes registrados.\n")
    else:
        print("\nClientes registrados:\n")
        print("ID\tNombre\t\t\tCorreo")
        for cliente in bd:
            print(f"{cliente['ID']}\t{cliente['nombre']} {cliente['apellido']}\t\t{cliente['correo']}")
        print("\nListado creado exitosamente.\n")

def registrar_compra(bd):
    if not bd:
        print("\nNo hay clientes registrados para registrar compras.\n")
        return
    
    id_cliente = int(input("Ingrese el ID del cliente que realizó la compra: "))
    cliente_encontrado = False
    for cliente in bd:
        if cliente["ID"] == id_cliente:
            fecha = input("Ingrese la fecha de la compra (AAAA-MM-DD): ")
            monto = float(input("Ingrese el monto total de la compra: "))
            puntos_acumulados = int(monto * 0.01)
            cliente["compras"].append(
                {
                    "fecha": fecha,
                    "monto": monto,
                    "puntos_acumulados": puntos_acumulados
                }
            )
            print(f'\nSe ha registrado una compra para {cliente["nombre"]} {cliente["apellido"]}.\n')
            cliente_encontrado = True
            break
    
    if not cliente_encontrado:
        print(f"No se encontró ningún cliente con el ID = {id_cliente}.")

def enviar_resumen_puntos(bd):
    if not bd:
        print("\nNo hay clientes registrados para enviar resumen de puntos acumulados.\n")
        return
    
    id_cliente = int(input("Ingrese el ID del cliente para el cual desea enviar el resumen: "))
    cliente_encontrado = False
    for cliente in bd:
        if cliente["ID"] == id_cliente:
            texto = f"ID CLIENTE: {id_cliente}\n"
            texto += f"NOMBRE CLIENTE: {cliente['nombre']} {cliente['apellido']}\n"
            texto += f"Fecha de Compra\tMonto Total\tPuntos\n"
            
            puntos_totales = 0
            for compra in cliente["compras"]:
                texto += f"{compra['fecha']}\t${compra['monto']}\t{compra['puntos_acumulados']} puntos\n"
                puntos_totales += compra['puntos_acumulados']
            
            texto += f"\nPUNTOS TOTALES A CANJEAR: {puntos_totales} pesos"
            
            with open(f"RESUMEN_CLIENTE_ID_{id_cliente}.txt", "w", encoding='utf-8') as archivo:
                archivo.write(texto)
            
            print(f"Se ha creado el archivo 'RESUMEN_CLIENTE_ID_{id_cliente}.txt' correctamente.\n")
            cliente_encontrado = True
            break
    
    if not cliente_encontrado:
        print(f"No se encontró ningún cliente con el ID = {id_cliente}.")
