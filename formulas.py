import math

a = int(input("informe um numero: \n"))
b = int(input("informe um numero: \n"))
c = int(input("informe um numero: \n"))

x1 = ((-b)+ math.sqrt(b**2- 4*a*c))/ 2*a
x2 = ((-b)- math.sqrt(b**2- 4*a*c)) / 2*a

print(x1)
print(x2)