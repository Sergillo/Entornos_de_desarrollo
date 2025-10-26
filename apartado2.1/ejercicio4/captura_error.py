"""
4. Captura el error
• Objetivo: try/except básicos.
• Consigna: repite el ejercicio anterior; si el usuario no escribe un número, muestra “Introduce
un año válido”.
• Referencia: excepciones y try/except (págs. 8–9)
"""
try:
    año_nacimiento = (int(input("Introduce el año en el que naciste: ")))
    años= 2025 - año_nacimiento
    print("Tu edad es de", años, "años")