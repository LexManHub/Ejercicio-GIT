# Sistema de venta de billetes de avión

class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha, salida, llegada, precio, asientos_disponibles = 50):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.salida = salida
        self.llegada = llegada
        self.precio = precio
        self.asientos_disponibles = asientos_disponibles #Añadido para controlar disponibilidad real

class Pasajero:
    def __init__(self, nombre, apellido, edad, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.correo = correo

class Reserva:# <-- Cambiado de 'Informacion' a 'Reserva' para que se entienda mejor
    def __init__(self, vuelo, pasajero, asientos):
        self.vuelo = vuelo
        self.pasajero = pasajero
        self.asientos = asientos

def mostrar_vuelos_disponibles(vuelos):
    print("Vuelos disponibles:")
    for vuelo in vuelos:
        print(f"Número de vuelo: {vuelo.numero_vuelo}, Origen: {vuelo.origen}, Destino: {vuelo.destino}, Fecha: {vuelo.fecha}, Hora de salida: {vuelo.salida}, Hora de llegada: {vuelo.llegada}")
        print(f"Precio: {vuelo.precio}€, Asientos disponibles: {vuelo.asientos_disponibles}") # Mostramos disponibilidad real

def crear_pasajero():  # Extraído para que no se duplique
    n = input("Ingrese su nombre: ")
    a = input("Ingrese su apellido: ")
    while True:
        try:
            e = int(input("Ingrese su edad: "))  # evita el error al poner un string en  int
            break
        except ValueError:
            print("Edad no válida. Intente de nuevo.")
    t = input("Ingrese su número de teléfono: ")
    c = input("Ingrese su correo electrónico: ")
    return Pasajero(n, a, e, t, c)

def obtener_datos_reserva():  # Otra extaccion
    numero = input("Ingrese el número de vuelo que desea reservar: ")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de asientos (máximo 10): "))  # otra validacion
            return numero, cantidad
        except ValueError:
            print("Cantidad no válida. Intente de nuevo.")

def reservar_vuelo(vuelos, numero_vuelo, pasajero, cantidad):
    for vuelo in vuelos:
        if vuelo.numero_vuelo == numero_vuelo:
            if cantidad <= 0:
                print("La cantidad de asientos debe ser mayor que cero.")  # <-- Validación lógica
                return None
            elif cantidad > 10:
                print("No se pueden reservar más de 10 asientos.")  # <-- Límite de negocio establecido
                return None
            elif cantidad > vuelo.asientos_disponibles:
                print(f"Lo sentimos, solo hay {vuelo.asientos_disponibles} asientos disponibles.")  # <-- Verificación de disponibilidad
                return None
            else:
                vuelo.asientos_disponibles -= cantidad  # <-- Se actualiza el número de asientos disponibles
                reserva = Reserva(vuelo, pasajero, cantidad)
                print(f"\n¡Reserva exitosa para el vuelo {vuelo.numero_vuelo}!")
                print(f"Pasajero: {pasajero.nombre} {pasajero.apellido}, Asientos: {cantidad}")
                return reserva
    print("No se encontró ningún vuelo con ese número.")  # <-- Validación de vuelo inexistente
    return None


def main():
    vuelos = [
        Vuelo("AA123", "Nueva York", "Los Angeles", "2024-05-15", "08:00", "11:00", 250.00),
        Vuelo("AA456", "Los Angeles", "Chicago", "2024-05-20", "10:00", "13:00", 200.00),
        Vuelo("AA789", "Chicago", "Miami", "2024-05-25", "12:00", "15:00", 300.00)
    ]

    print("Bienvenido al sistema de venta de billetes de avión.")
    opcion = input("Seleccione una opción:\n1. Ver vuelos disponibles\n2. Reservar vuelo\nIngrese su opción: ")

    if opcion == '1':
        mostrar_vuelos_disponibles(vuelos)
    elif opcion == '2':
        #extraer método
        n = input("Ingrese su nombre: ")
        a = input("Ingrese su apellido: ")
        e = int(input("Ingrese su edad: "))
        t = input("Ingrese su número de teléfono: ")
        c = input("Ingrese su correo electrónico: ")

        pasajero = Pasajero(n, a, e, t, c)

        #extraer método
        numero = input("Ingrese el número de vuelo que desea reservar: ")
        cantidad = int(input("Ingrese la cantidad de asientos que desea reservar (máximo 10): "))

        reservar_vuelo(vuelos, numero, pasajero, cantidad)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
