"""
Operadores en acción
• Objetivo: practicar + - * / // % ** y +=.
• Consigna: con dos enteros a y b imprime todas esas operaciones.
• Referencia: tabla de operadores (pág. 10).
"""
a = int(input("Introduce el primer numero: "))
b = int(input("Introduce el segundo numero: "))
print("La suma de", a, "y", b, "es", a + b)
print("La resta de", a, "y", b, "es", a - b)
print("La multiplicación de", a, "y", b, "es", a * b)
print("La división de", a, "y", b, "es", a / b)
print("La división entera de", a, "y", b, "es", a // b)
print("El resto de la división de", a, "y", b, "es", a % b)
print("La potencia de", a, "y", b, "es", a ** b)