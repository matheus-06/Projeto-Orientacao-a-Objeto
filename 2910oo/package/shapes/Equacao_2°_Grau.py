import math

class SegundoGrau:
	def __init__(self, A, B, C):
		self.A = A
		self.B = B
		self.C = C
		
	def Delta(self):
		delta = math.pow(self.B, 2) - (4 * self.A * self.C)
		print(f"Delta = {delta}")
		return delta
		
		
	def Raiz(self, delta):
		if(delta > 0):
			equacao1.DuasRaizes(delta)
		elif(delta < 0):
			print("Raiz imaginária w.i.p")
			equacao1.RaizImaginaria(delta)
		else:
			equacao1.UmaRaiz(delta)
		
	def DuasRaizes(self, delta):
		x1 = ((-self.B)+(math.sqrt(delta)))/(2 * self.A)
		x2 = ((-self.B)-(math.sqrt(delta)))/(2 * self.A)
		print(f"X1 = {x1} \nX2 = {x2}")
		
	def UmaRaiz(self, delta):
		x =  ((-self.B)+(math.sqrt(delta)))/(2 * self.A)
		print(f"2 Raizes = {x}")
		
	def RaizImaginaria(self, delta):
		novodelta = delta * -1
		print(f"{-self.B}±√{novodelta}i\n    {2*self.A}")
		
#////////////////////////////////////////////////////////////////////

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

equacao1 = SegundoGrau(A, B, C)
delta1 = equacao1.Delta()
equacao1.Raiz(delta1)
