"""
3. Edad correcta
• Objetivo: convertir tipos.
• Consigna: pide año de nacimiento, conviértelo con int() y calcula edad.
• Referencia: conversión de tipos y int()
"""
try:
    año_nacimiento = (int(input("Introduce el año en el que naciste: ")))
    años= 2025 - año_nacimiento
    print("Tu edad es de", años, "años")
except ValueError:
    print("Por favor, introduce valores numericos")