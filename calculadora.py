#Crear una calculadora mediante los siguiente requirimientos:
#1 La calculadora debe ser capaz de operar las 4 operaciones básica (suma, resta, multiplicación y división)
#2 La calculadora debe ser construida mediante una instancia de la clase CalculadoraBasica --Programada por el desarrollador--
   #Dicha clase debe contener todas las funciones --métodos-- necesarios para soportar todo el funcionamiento requirido.
#3Los números deben ser solicitados e ingresados por el usuario --puede ser por la función input--

#4 Al terminar debe dar el resultado esperado de la siguiente manera: 'la suma de 4 + 6 = 10'

class Calculadora:
    def __init__(self):
        self.numero_1 = int(input('Digite el primer numero: '))
        self.numero_2 = int(input('Digite el segundo numero: '))

    def suma(self):
        self.resultado = self.numero_1+self.numero_2
        print ('La suma de {} + {} = {}' .format(self.numero_1, self.numero_2, self.resultado))
    def resta(self):
        self.resultado = self.numero_1 - self.numero_2
        print('La resta de {} - {} = {}'.format(self.numero_1, self.numero_2, self.resultado))
    def multi(self):
        self.resultado = self.numero_1 * self.numero_2
        print('La multiplicacion de {} * {} = {}'.format(self.numero_1, self.numero_2, self.resultado))
    def divi(self):
        self.resultado =self.numero_1 / self.numero_2
        print('La division de {} / {} = {}'.format(self.numero_1, self.numero_2, self.resultado))



casio = Calculadora()
casio.suma()
casio.resta()
casio.multi()
casio.divi()




