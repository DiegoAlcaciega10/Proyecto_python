
import datetime
import random
import os


class Persona:
    def __init__(self, nombre, edad, cedula, correo):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.correo = correo
        self.activo = True
        self.datos = []

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Cedula:", self.cedula)
        print("Correo:", self.correo)

    def verificar_edad(self):
        if self.edad >= 18:
            if self.edad <= 65:
                if self.activo == True:
                    return True
        return False

    def actualizar_correo(self, nuevo_correo):
        if nuevo_correo != "":
            self.correo = nuevo_correo
            return True
        else:
            return False


class Empleado(Persona):
    def __init__(self, nombre, edad, cedula, correo, salario, departamento):
        super().__init__(nombre, edad, cedula, correo)
        self.salario = salario
        self.departamento = departamento
        self.horas_trabajadas = 0
        self.bonificaciones = 0

    def calcular_salario(self):
        if self.horas_trabajadas > 160:
            extra = self.horas_trabajadas - 160
            return self.salario + (extra * 15)
        else:
            return self.salario

    def mostrar_informacion(self):
        print("Empleado:", self.nombre)
        print("Edad:", self.edad)
        print("Cedula:", self.cedula)
        print("Correo:", self.correo)
        print("Salario:", self.salario)
        print("Departamento:", self.departamento)

    def registrar_horas(self, horas):
        if horas > 0:
            self.horas_trabajadas = self.horas_trabajadas + horas
        else:
            print("Horas incorrectas")

    def calcular_bonificacion(self):
        if self.salario > 1000:
            if self.departamento == "TI":
                self.bonificaciones = self.salario * 0.15
            elif self.departamento == "Administracion":
                self.bonificaciones = self.salario * 0.10
            elif self.departamento == "Ventas":
                self.bonificaciones = self.salario * 0.05
            else:
                self.bonificaciones = 0
        else:
            self.bonificaciones = 0
        return self.bonificaciones


class Desarrollador(Empleado):
    def __init__(self, nombre, edad, cedula, correo, salario,
                 departamento, lenguaje, experiencia):
        super().__init__(nombre, edad, cedula, correo, salario, departamento)
        self.lenguaje = lenguaje
        self.experiencia = experiencia
        self.proyectos = []

    def trabajar(self):
        print(self.nombre, "esta programando en", self.lenguaje)

    def calcular_salario(self):
        if self.horas_trabajadas > 160:
            extra = self.horas_trabajadas - 160
            return self.salario + (extra * 20)
        else:
            return self.salario

    def mostrar_informacion(self):
        print("Desarrollador:", self.nombre)
        print("Edad:", self.edad)
        print("Cedula:", self.cedula)
        print("Correo:", self.correo)
        print("Salario:", self.salario)
        print("Lenguaje:", self.lenguaje)
        print("Experiencia:", self.experiencia)

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def evaluar_experiencia(self):
        if self.experiencia > 5:
            if self.lenguaje == "Python":
                if len(self.proyectos) > 3:
                    return "Senior"
                else:
                    return "Semi Senior"
            else:
                return "Especialista"
        else:
            return "Junior"


class Gerente(Empleado):
    def __init__(self, nombre, edad, cedula, correo, salario,
                 departamento, empleados_a_cargo):
        super().__init__(nombre, edad, cedula, correo, salario, departamento)
        self.empleados_a_cargo = empleados_a_cargo
        self.reuniones = []
        self.presupuesto = 5000

    def calcular_salario(self):
        return self.salario + (self.salario * 0.25)

    def mostrar_informacion(self):
        print("Gerente:", self.nombre)
        print("Edad:", self.edad)
        print("Cedula:", self.cedula)
        print("Correo:", self.correo)
        print("Salario:", self.salario)
        print("Empleados a cargo:", self.empleados_a_cargo)

    def asignar_presupuesto(self, cantidad):
        if cantidad > 0:
            self.presupuesto = self.presupuesto + cantidad
            print("Presupuesto actualizado")
        else:
            print("Cantidad incorrecta")

    def realizar_reunion(self, tema):
        self.reuniones.append(tema)
        print("Reunion realizada:", tema)


class Vendedor(Empleado):
    def __init__(self, nombre, edad, cedula, correo, salario,
                 departamento, ventas):
        super().__init__(nombre, edad, cedula, correo, salario, departamento)
        self.ventas = ventas
        self.comisiones = 0

    def calcular_comision(self):
        if self.ventas > 10000:
            self.comisiones = self.ventas * 0.10
        elif self.ventas > 5000:
            self.comisiones = self.ventas * 0.05
        else:
            self.comisiones = self.ventas * 0.02

        return self.comisiones

    def calcular_salario(self):
        return self.salario + self.calcular_comision()

    def mostrar_informacion(self):
        print("Vendedor:", self.nombre)
        print("Edad:", self.edad)
        print("Cedula:", self.cedula)
        print("Correo:", self.correo)
        print("Ventas:", self.ventas)
        print("Comisiones:", self.comisiones)


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.historial = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        self.historial.append("Empleado agregado")

    def eliminar_empleado(self, cedula):
        for empleado in self.empleados:
            if empleado.cedula == cedula:
                self.empleados.remove(empleado)
                print("Empleado eliminado")
                return True
        return False

    def buscar_empleado(self, cedula):
        for empleado in self.empleados:
            if empleado.cedula == cedula:
                return empleado
        return None

    def mostrar_empleados(self):
        for empleado in self.empleados:
            empleado.mostrar_informacion()
            print("----------------------")

    def calcular_nomina(self):
        total = 0
        for empleado in self.empleados:
            total = total + empleado.calcular_salario()
        return total

    def generar_reporte(self):
        contador = 0
        for empleado in self.empleados:
            if empleado.activo == True:
                if empleado.edad > 18:
                    if empleado.salario > 0:
                        contador = contador + 1
                        print("Empleado:", empleado.nombre)
                        print("Salario:", empleado.calcular_salario())
                        print("Departamento:", empleado.departamento)
                        print("----------------------")
        print("Total de empleados:", contador)

    def procesar_pagos(self):
        for empleado in self.empleados:
            try:
                salario = empleado.calcular_salario()
                if salario > 0:
                    print("Pago realizado a", empleado.nombre)
                    print("Valor:", salario)
            except:
                print("Error al procesar pago")


def crear_datos_prueba():
    empresa = Empresa("Tech Solutions")

    empleado1 = Desarrollador(
        "Carlos", 25, "123456", "carlos@gmail.com",
        1200, "TI", "Python", 6
    )

    empleado2 = Gerente(
        "Maria", 35, "654321", "maria@gmail.com",
        2500, "Administracion", 10
    )

    empleado3 = Vendedor(
        "Pedro", 28, "789123", "pedro@gmail.com",
        900, "Ventas", 12000
    )

    empleado4 = Empleado(
        "Juan", 19, "456789", "juan@gmail.com",
        750, "TI"
    )

    empresa.agregar_empleado(empleado1)
    empresa.agregar_empleado(empleado2)
    empresa.agregar_empleado(empleado3)
    empresa.agregar_empleado(empleado4)

    empleado1.registrar_horas(180)
    empleado2.registrar_horas(170)

    return empresa


def menu():
    empresa = crear_datos_prueba()

    while True:
        print("\n===== SISTEMA DE EMPLEADOS =====")
        print("1. Mostrar empleados")
        print("2. Buscar empleado")
        print("3. Calcular nomina")
        print("4. Generar reporte")
        print("5. Procesar pagos")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            empresa.mostrar_empleados()

        elif opcion == "2":
            cedula = input("Ingrese cedula: ")
            empleado = empresa.buscar_empleado(cedula)

            if empleado != None:
                empleado.mostrar_informacion()
            else:
                print("Empleado no encontrado")

        elif opcion == "3":
            print("Nomina total:", empresa.calcular_nomina())

        elif opcion == "4":
            empresa.generar_reporte()

        elif opcion == "5":
            empresa.procesar_pagos()

        elif opcion == "6":
            print("Saliendo del sistema")
            break

        else:
            print("Opcion incorrecta")


if __name__ == "__main__":
    menu()
