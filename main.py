# Clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, ruedas, velocidad, cilindraje):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def mostrar_datos(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Número de ruedas: {self.ruedas}")
        print(f"Velocidad: {self.velocidad} km/h")
        print(f"Cilindraje: {self.cilindraje} cc")
        print("-" * 30)


# Función para capturar datos del vehículo
def capturar_datos_vehiculo(numero):
    print(f"\nDatos del automóvil {numero}")
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindraje = int(input("Inserte el cilindraje en cc: "))
    return Vehiculo(marca, modelo, ruedas, velocidad, cilindraje)


# Función principal
def main():
    cantidad = int(input("Cuantos Vehiculos desea insertar: "))
    vehiculos = []

    for i in range(cantidad):
        vehiculo = capturar_datos_vehiculo(i + 1)
        vehiculos.append(vehiculo)

    # Mostrar datos de los vehículos
    print("\nImprimiendo por pantalla los Vehículos:")
    for vehiculo in vehiculos:
        vehiculo.mostrar_datos()


if __name__ == "__main__":
    main()

# Clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, ruedas, velocidad, cilindraje):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def mostrar_datos(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, {self.ruedas} ruedas {self.velocidad} Km/h, {self.cilindraje} cc")

# Clase Automovil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, ruedas, velocidad, cilindraje)

# Automóvil particular
class Particular(Automovil):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindraje, puestos):
        super().__init__(marca, modelo, ruedas, velocidad, cilindraje)
        self.puestos = puestos

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Puestos: {self.puestos}")

# Automóvil de carga
class Carga(Automovil):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindraje, peso_carga):
        super().__init__(marca, modelo, ruedas, velocidad, cilindraje)
        self.peso_carga = peso_carga

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Peso de carga: {self.peso_carga} Kg")

# Clase Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, ruedas, None, None)
        self.tipo_bicicleta = tipo_bicicleta

    def mostrar_datos(self):
        print(f"Marca {self.marca}, Modelo {self.modelo}, {self.ruedas} ruedas Tipo: {self.tipo_bicicleta}")

# Clase Motocicleta
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, ruedas, tipo_bicicleta, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, ruedas, tipo_bicicleta)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}")

# Ejemplo de instancias
particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

# Mostrar datos
particular.mostrar_datos()
carga.mostrar_datos()
bicicleta.mostrar_datos()
motocicleta.mostrar_datos()

# Verificación de instancias
print("\nVerificación de instancias:")
print(f"Motocicleta es instancia con relación a Vehiculo: {isinstance(motocicleta, Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
print(f"Motocicleta es instancia con relación a Vehiculo particular: {isinstance(motocicleta, Particular)}")
print(f"Motocicleta es instancia con relación a Vehiculo de Carga: {isinstance(motocicleta, Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")

import csv


# Función para guardar datos en CSV
def guardar_datos_csv(vehiculos, nombre_archivo='vehiculos.csv'):
    with open(nombre_archivo, mode='w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        for vehiculo in vehiculos:
            if isinstance(vehiculo, Particular):
                escritor_csv.writerow(["Particular", vehiculo.marca, vehiculo.modelo, vehiculo.ruedas, vehiculo.velocidad, vehiculo.cilindraje, vehiculo.puestos])
            elif isinstance(vehiculo, Carga):
                escritor_csv.writerow(["Carga", vehiculo.marca, vehiculo.modelo, vehiculo.ruedas, vehiculo.velocidad, vehiculo.cilindraje, vehiculo.peso_carga])
            elif isinstance(vehiculo, Bicicleta):
                escritor_csv.writerow(["Bicicleta", vehiculo.marca, vehiculo.modelo, vehiculo.ruedas, vehiculo.tipo_bicicleta])
            elif isinstance(vehiculo, Motocicleta):
                escritor_csv.writerow(["Motocicleta", vehiculo.marca, vehiculo.modelo, vehiculo.ruedas, vehiculo.tipo_bicicleta, vehiculo.motor, vehiculo.cuadro, vehiculo.nro_radios])


# Función para leer y mostrar datos desde un archivo CSV
def leer_datos_csv(nombre_archivo='vehiculos.csv'):
    try:
        with open(nombre_archivo, mode='r') as archivo:
            lector_csv = csv.reader(archivo)
            for fila in lector_csv:
                if fila[0] == "Particular":
                    print(f"Particular: Marca: {fila[1]}, Modelo: {fila[2]}, Ruedas: {fila[3]}, Velocidad: {fila[4]} km/h, Cilindraje: {fila[5]} cc, Puestos: {fila[6]}")
                elif fila[0] == "Carga":
                    print(f"Carga: Marca: {fila[1]}, Modelo: {fila[2]}, Ruedas: {fila[3]}, Velocidad: {fila[4]} km/h, Cilindraje: {fila[5]} cc, Peso carga: {fila[6]} Kg")
                elif fila[0] == "Bicicleta":
                    print(f"Bicicleta: Marca: {fila[1]}, Modelo: {fila[2]}, Ruedas: {fila[3]}, Tipo: {fila[4]}")
                elif fila[0] == "Motocicleta":
                    print(f"Motocicleta: Marca: {fila[1]}, Modelo: {fila[2]}, Ruedas: {fila[3]}, Tipo: {fila[4]}, Motor: {fila[5]}, Cuadro: {fila[6]}, Nro radios: {fila[7]}")
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")


# Ejemplo de uso e instancias
if __name__ == "__main__":
    # Lista de vehículos
    vehiculos = [
        Particular("Ford", "Fiesta", 4, 180, 500, 5),
        Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000),
        Bicicleta("Shimano", "MT Ranger", 2, "Carrera"),
        Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
    ]

    # Guardar los datos de los vehículos en un archivo CSV
    guardar_datos_csv(vehiculos)

    # Leer y mostrar los datos desde el archivo CSV
    leer_datos_csv()

    # Mostrar los datos de los vehículos en consola
    print("\nDatos de los vehículos ingresados:")
    for vehiculo in vehiculos:
        vehiculo.mostrar_datos()

    # Verificación de instancias
    print("\nVerificación de instancias:")
    print(f"Motocicleta es instancia de Vehiculo: {isinstance(vehiculos[-1], Vehiculo)}")
    print(f"Motocicleta es instancia de Bicicleta: {isinstance(vehiculos[-1], Bicicleta)}")
    print(f"Motocicleta es instancia de Automovil: {isinstance(vehiculos[-1], Automovil)}")  # Debería ser False
    print(f"Motocicleta es instancia de Motocicleta: {isinstance(vehiculos[-1], Motocicleta)}")
