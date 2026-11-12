class Estudiante:
    # Constructor
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    # Método para mostrar información
    def mostrar_informacion(self):
        print("Información del estudiante")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")

    # Método para estudiar
    def estudiar(self, materia):
        print(f"{self.nombre} está estudiando {materia}.")


# Crear objetos
estudiante1 = Estudiante("Carlos", 22, "Ingeniería en TI")
estudiante2 = Estudiante("María", 21, "Ingeniería de Software")

# Utilizar métodos
estudiante1.mostrar_informacion()
estudiante1.estudiar("Programación Orientada a Objetos")

print("-------------------------")

estudiante2.mostrar_informacion()
estudiante2.estudiar("Bases de Datos")