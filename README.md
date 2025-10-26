### Índice y Algoritmos de los Ejercicios

| N° | Ejercicio | Tag de Versión Final |
|----|------------|----------------------|
| 1 | Hola, variable | `v1.0-ejer1-hola` |
| 2 | Tu primer input | `v1.0-ejer2-input` |
| 3 | Edad correcta | `v1.0-ejer3-edad` |
| 4 | Captura el error | `v1.0-ejer4-error` |
| 5 | Sumadora mínima | `v1.0-ejer5-suma` |
| 6 | Operadores en acción | `v1.0-ejer6-op` |
| 7 | Longitud de palabra | `v1.0-ejer7-len` |
| 8 | Limpia y formatea | `v1.0-ejer8-format` |
| 9 | Mi primera f-string | `v1.0-ejer9-fstring` |
| 10 | Caracteres Unicode | `v1.0-ejer10-unicode` |

### Algoritmo Ejercicio 1: Hola, variable

1. Hola, variable
• Objetivo: declarar variables y print.
• Consigna: crea persona = "Pepe" y muestra “Hola, Pepe”. Comenta qué pasa si
cambias el valor.
• Referencia: variables y asignación (págs. 2–3).

### Procedimiento
-En este ejercicio primero le asignaremos el valor "Pepe" a la variable "persona", y luego con un print mostramos un mensaje acompañado de la variable "persona" que mostrara "Pepe"
Si cambiamos el valor de la variable persona, en el mensaje en el que mostramos "Hola, Pepe", nos saldra, lo que le asignemos a la variable persona.

### Algoritmo Ejercicio 2: Tu primer input

2. Tu primer input
• Objetivo: leer texto del usuario.
• Consigna: pide el nombre y muestra Hola <nombre>.
• Referencia: input y texto de prompt (pág. 4).

### Procedimiento
-En este ejercicio usaremos un input para pedir un nombre al usuario, a la misma vez que le asignamos ese nombre a un variable y luego le mostramos al usuario lo que a introducido.

### Algoritmo Ejercicio 3: Edad correcta

3. Edad correcta
• Objetivo: convertir tipos.
• Consigna: pide año de nacimiento, conviértelo con int() y calcula edad.
• Referencia: conversión de tipos y int()

### Procedimiento
-Primero pediremos al usuario el valor para la variable año_a¡nacimiento que sea numero entero y luego se lo calcularemos y se lo mostraremos.

### Algoritmo Ejercicio 4: Captura el error

4. Captura el error
• Objetivo: try/except básicos.
• Consigna: repite el ejercicio anterior; si el usuario no escribe un número, muestra “Introduce
un año válido”.
• Referencia: excepciones y try/except (págs. 8–9)

### Procedimiento
-Primero copiaremos el código del ejercicio anterior y luego utilizaremos las expresiones try y except para que nos muestre un mensaje de error.

### Algoritmo Ejercicio 5: Sumadora minima

5. Sumadora mínima
• Objetivo: operar con números vs cadenas.
• Consigna: pide dos números; demuestra qué ocurre si sumas como cadenas y luego corrígelo
con int().
• Referencia: diferencia entre "10" y 10 (págs. 5 y 10–11).

### Procedimiento
-Primero pedimos 2 variables para sumarlas, pero podemos ver que si sumamos las 2 variables sin el int, nos continua la variable 1 con la 2 (si ponemos num1= 1 y num2 = 5, nos pone 15, es decir que no los suma) y para que nos lo sume tenemos que poner el int antes del input.

## Algoritmo Ejercicio 6: Operadores en acción

6. Operadores en acción
• Objetivo: practicar + - * / // % ** y +=.
• Consigna: con dos enteros a y b imprime todas esas operaciones.
• Referencia: tabla de operadores (pág. 10).

### Procedimiento
-En este ejercicio pedimos dos variables que sean numeros, y realizamos todas las operaciones mencionadas anteriormente mostrando su resultado.

## Algoritmo Ejercicio 7: Longitud de una palabra

7. Longitud de una palabra
• Objetivo: len() y print.
• Consigna: pide una palabra y muestra su longitud.
• Referencia: len (pág. 11).

### Procedimiento
-Primero pediremos una palabra en forma de variable y luego calcularemos su longitud y por ultimo mostraremos la cantidad de caracteres que tiene.

## Algoritmo Ejercicio 8: Limpia y formatea

8. Limpia y formatea
• Objetivo: strip, lower, upper.
• Consigna: lee una frase con espacios delante y detrás; muestra: original, con strip(), en
minúsculas y en mayúsculas.
• Referencia: replace, strip, lower/upper

### Procedimiento
-Pide al usuario una cadena de caracteres y luego te lo muestra tal cual se a escrito, sin espacios al principio y al final, en minúsculas y en mayusculas.

## Algoritmo Ejercicio 9: Mi primera f-string

9. Mi primera f-string
• Objetivo: f-strings.
• Consigna: con nombre y edad, imprime: Pepe tiene 20 años.
• Extensión: muestra alineación de decimales :6.3f.
• Referencia: f-strings y formato (págs. 12–13).

### Procedimiento
-Muestra como funcionan los f-strings en varios casos.


## Algoritmo Ejercicio 10: Caracteres Unicode

10.Caracteres Unicode
• Objetivo: chr() y curiosidad por Unicode.
• Consigna: imprime 3 emojis usando sus códigos.
• Referencia: ejemplos chr(0x1F415)... (pág. 13).

### Procedimiento
-Utilizaremos  el print con el chr seguido del codigo del emoji para escribirlo.
