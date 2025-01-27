from math import sqrt, pi  
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) #необходимо преобразование в число
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) # двойные кавычки в тексте print не были закрыты
di = a * sqrt(2) #math.sqr заменено на math.sqrt
print("Ruudu diagonaal", round(di,2))
#print() 
print("Ristküliku karakteristikud") #закрывающая скобка в print была лишней
b = float(input("Sisesta ristküliku 1. külje pikkus => "))
c = float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print("Ristküliku pindala", S) #пропущены кавычки в тексте print
P = 2 * (b + c) #пропущена  умножение
print("Ristküliku ümbermõõt", P)
di = sqrt(b**2 + c**2)
print("Ristküliku diagonaal", round(di)) #закрывающая скобка print была пропущена
print()

print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus => ')) #лишние кавычки в input, пропущено преобразование в число
d = 2 * r ##пропущено умножение в 2 * r
print("Ringi läbimõõt", d)
#  вызов pi() заменён на переменную pi
S = pi * r**2
print("Ringi pindala", round(S, 2))
#  вызов pi() заменён на переменную pi
C = 2 * pi * r
#  закрывающая скобка print была пропущена
print("Ringjoone pikkus", round(C, 2))