# Sistema de venta de billetes de avión

class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha, salida, llegada, precio):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.salida = salida
        self.llegada = llegada
        self.precio = precio

class Pasajero:
    def __init__(self, nombre, apellido, edad, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.correo = correo

class Informacion:
    def __init__(self, vuelo, pasajero, asientos):
        self.vuelo = vuelo
        self.pasajero = pasajero
        self.asientos = asientos

def mostrar_vuelos_disponibles(vuelos):
    print("Vuelos disponibles:")
    for vuelo in vuelos:
        print(f"Número de vuelo: {vuelo.numero_vuelo}, Origen: {vuelo.origen}, Destino: {vuelo.destino}, Fecha: {vuelo.fecha}, Hora de salida: {vuelo.salida}, Hora de llegada: {vuelo.llegada}, Precio: {vuelo.precio}")

def reservar_vuelo(lista, numero_vuelo, pasajero, cantidad):
    
    for v in lista:
        if v.numero_vuelo == numero_vuelo:
            if cantidad <= 0:
                print("La cantidad de asientos debe ser mayor que cero.")
                return
            elif cantidad > 10:
                print("Lo sentimos, no se pueden reservar más de 10 asientos por reserva.")
                return
            elif cantidad > 0 and cantidad <= 10:
                reserva = Informacion(v, pasajero, cantidad)
                print(f"¡Reserva exitosa para el vuelo {v.numero_vuelo}!")
                print(f"Nombre del pasajero: {pasajero.nombre} {pasajero.apellido}, Asientos reservados: {cantidad}")
                return
    print("No se encontró ningún vuelo con el número especificado.")


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
