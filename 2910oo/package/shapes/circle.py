import math

class Circle:
	def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r
		
	def imprimir(self):
		print(f"Centro = ({self.x},{self.y})")
		print(f"Raio = {self.r}")
		
	def area(self):
		area = 3.1415 * math.pow(self.r, 2)
		print(f"Area = {area}")
		
	def circunferencia(self):
		circ = 2*3.1415*self.r
		print(f"Circunferencia = {circ}")
		
x = int(input("X = "))
y = int(input("Y = "))
r = float(input("Raio = "))

circulo = Circle(x, y, r)
circulo.imprimir()
circulo.area()
circulo.circunferencia()
