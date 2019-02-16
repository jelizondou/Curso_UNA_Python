import random, math


class Vehiculo:
        def __init__(self):
            print ('creando un vehiculo')
            self.fuerzamotor = random.randint(0,9)
            self.distancia = 0
            self.meta = 1000
        def calcularfuerzamotor(self):
            self.fuerzamotor = random.randint(0, 9)


class Camion(Vehiculo):
        def __init__(self):
            super().__init__()
            self.avance = 2 * (self.fuerzamotor) + 1
            self.distancia = self.distancia + self.avance



class Tractor(Vehiculo):
        def __init__(self):
            super().__init__()
            self.avance = int(math.log(self.fuerzamotor, 2))
            self.distancia = self.distancia + self.avance



class Sedan(Vehiculo):
        def __init__(self):
            super().__init__()
            self.avance = 3 * (self.fuerzamotor)**2
            self.distancia = self.distancia + self.avance
        def avanzar(self):# Esteban agrego esta funcion para el calculo del siguiente avance, meter esta misma en los demas
            self.fuerzamotor = random.randint(0, 9)
            self.avance = 3 * (self.fuerzamotor) ** 2
            self.distancia = self.distancia + self.avance

class Bus(Vehiculo):
        def __init__(self):
            super().__init__()
            self.avance = 5 * self.fuerzamotor
            self.distancia = self.distancia + self.avance


#crear la funcion que haga la carrera

pass






