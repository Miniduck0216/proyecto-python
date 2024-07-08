def ingresar_cliente(clientes):
    # Esta función permite ingresar un nuevo cliente en la lista de clientes
    for i in range(len(clientes)):
        if clientes[i][0] == "":
            #Encuentra el primer espacio vacío en la lista de clientes
            nombre = input("Ingrese nombre del nuevo cliente: ")
            dni = input("Ingrese cédula del nuevo cliente: ")
            # Ingresa el nombre y cédula del nuevo cliente
            clientes[i] = [nombre, dni]
            break
    imprimir_clientes(clientes)
    # Imprime la lista de clientes actualizada.

def imprimir_clientes(clientes):
    # Esta función imprime la lista de clientes.
    for cliente in clientes:
        print(f"{cliente[0]}\t\t{cliente[1]}")

def listar_peliculas(peliculas):
    # Esta función lista todas las películas disponibles
    for pelicula in peliculas:
        print(f"ID: {pelicula[0]}, Nombre: {pelicula[1]}, Hora: {pelicula[2]}, Género: {pelicula[3]}")

def buscar_por_nombre(peliculas):
    # Esta función permite buscar una película por nombre
    nombre = input("Ingrese el nombre de la película: ")
    for pelicula in peliculas:
        if nombre.lower() in pelicula[1].lower():
            # Imprime las películas que coinciden con el nombre ingresado
            print(f"ID: {pelicula[0]}, Nombre: {pelicula[1]}, Hora: {pelicula[2]}, Género: {pelicula[3]}")

def buscar_por_genero(peliculas):
    # Esta función permite buscar una película por género
    genero = input("Ingrese el género de la película: ")
    for pelicula in peliculas:
        if genero.lower() in pelicula[3].lower():
            # Imprime las películas que coinciden con el género ingresado
            print(f"ID: {pelicula[0]}, Nombre: {pelicula[1]}, Hora: {pelicula[2]}, Género: {pelicula[3]}")

def comprar_ticket(peliculas, precio, clientes, reserva):
    # Esta función permite comprar un ticket para una película
    cliente_id = int(input("Ingrese el ID del cliente: ")) - 1
    pelicula_id = int(input("Ingrese el ID de la película: ")) - 1
    cantidad = int(input("Ingrese la cantidad de boletos: "))
    
    tipo_boleto = int(input("Ingrese el tipo de boleto (0: General, 1: Estudiante, 2: Niño): "))
    total = precio[tipo_boleto] * cantidad
    # Calcula el total a pagar según el tipo de boleto y la cantidad

    for i in range(len(reserva)):
        if reserva[i][0] == -1:
            # Encuentra el primer espacio vacío en la lista de reservas
            reserva[i] = [cliente_id, pelicula_id, cantidad, tipo_boleto]
            break
    
    print(f"Total a pagar: ${total:.2f}")
    # Imprime el total a pagar.

def imprimir_factura(cliente, pelicula, cantidad, tipo_boleto, total):
    # Esta función imprime una factura detallada para el cliente
    tipo_boleto_str = ["General", "Estudiante", "Niño"]
    print("\nFactura:")
    print(f"Cliente: {cliente[0]}")
    print(f"Cédula: {cliente[1]}")
    print(f"Película: {pelicula[1]}")
    print(f"Hora: {pelicula[2]}")
    print(f"Género: {pelicula[3]}")
    print(f"Tipo de boleto: {tipo_boleto_str[tipo_boleto]}")
    print(f"Cantidad: {cantidad}")
    print(f"Total a pagar: ${total:.2f}\n")

def imprimir_factura_por_id(peliculas, precio, clientes, reserva):
    # Esta función imprime la factura de una reserva específica por su id
    reserva_id = int(input("Ingrese el ID de la reserva: "))
    if reserva_id < len(reserva) and reserva[reserva_id][0] != -1:
        r = reserva[reserva_id]
        cliente = clientes[r[0]]
        pelicula = peliculas[r[1]]
        total = precio[r[3]] * r[2]
        imprimir_factura(cliente, pelicula, r[2], r[3], total)
    else:
        print("Reserva no encontrada.")

# Lista de películas disponibles
peliculas = [["1", "Avatar", "10:20", "Fantasia"],
             ["2", "REC", "8:30", "Terror"],
             ["3", "Angry Birds", "11:00", "Animacion"],
             ["4", "Elementos", "12:30", "Animacion"],
             ["5", "Shrek", "9:30", "Fantasia"],
             ["6", "IT", "13:00", "Terror"],
             ["7", "El Aro", "14:30", "Terror"],
             ["8", "Garfield", "15:00", "Animacion"],
             ["9", "Las 50 sombras de Grey", "16:00", "Fantasia"],
             ["10", "Sing", "17:30", "Animacion"]]

# Precios de los boletos según el tipo
precio = [7, 3.5, 3]

# Lista de clientes, inicialmente vacía
clientes = [["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""]]

# Lista de reservas, inicialmente vacía
reserva = [[-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, -1, -1, -1],
           [-1, -1, -1, -1]]

# Bucle principal del programa
while True:
    print("Escoja una opción:\n1. Ingresar Cliente\n2. Ver Películas\n3. Buscar Película\n4. Comprar Ticket\n5. Imprimir Factura")
    opcion2 = int(input(">> "))

    if opcion2 == 1:
        ingresar_cliente(clientes)
    elif opcion2 == 2:
        listar_peliculas(peliculas)
    elif opcion2 == 3:
        print("1. Por nombre\n2. Por Género")
        opcion3 = int(input(">> "))
        if opcion3 == 1:
            buscar_por_nombre(peliculas)
        elif opcion3 == 2:
            buscar_por_genero(peliculas)
    elif opcion2 == 4:
        comprar_ticket(peliculas, precio, clientes, reserva)
    elif opcion2 == 5:
        imprimir_factura_por_id(peliculas, precio, clientes, reserva)
    
    # Pregunta si el usuario desea realizar otra operación
    opcion1 = int(input("¿Desea escoger una nueva opción? 1. Sí / 2. No\n>> "))
    if opcion1 != 1:
        break