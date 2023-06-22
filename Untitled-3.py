# Importar tkinter para crear la interfaz gráfica
import tkinter as tk
# Importar math para usar las funciones matemáticas
import math

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Científica")

# Crear una variable para almacenar el resultado
resultado = tk.StringVar()

# Crear una función para actualizar el resultado según los botones presionados
def actualizar_resultado(digito):
    # Obtener el valor actual del resultado
    valor = resultado.get()
    # Si el valor es 0, reemplazarlo por el dígito
    if valor == "0":
        resultado.set(digito)
    # Si el valor no es 0, concatenar el dígito
    else:
        resultado.set(valor + digito)

# Crear una función para borrar el resultado
def borrar_resultado():
    # Establecer el resultado a 0
    resultado.set("0")

# Crear una función para evaluar la expresión del resultado
def evaluar_resultado():
    # Obtener el valor actual del resultado
    valor = resultado.get()
    # Intentar evaluar la expresión usando la función eval
    try:
        # Si la evaluación es exitosa, establecer el resultado al valor evaluado
        resultado.set(eval(valor))
    # Si la evaluación falla, mostrar un mensaje de error
    except:
        # Establecer el resultado a "Error"
        resultado.set("Error")

# Crear una función para calcular el seno del resultado
def seno_resultado():
    # Obtener el valor actual del resultado
    valor = resultado.get()
    # Intentar calcular el seno usando la función math.sin
    try:
        # Si el cálculo es exitoso, establecer el resultado al valor del seno en grados
        resultado.set(math.sin(math.radians(float(valor))))
    # Si el cálculo falla, mostrar un mensaje de error
    except:
        # Establecer el resultado a "Error"
        resultado.set("Error")

# Crear una función para calcular el coseno del resultado
def coseno_resultado():
    # Obtener el valor actual del resultado
    valor = resultado.get()
    # Intentar calcular el coseno usando la función math.cos
    try:
        # Si el cálculo es exitoso, establecer el resultado al valor del coseno en grados
        resultado.set(math.cos(math.radians(float(valor))))
    # Si el cálculo falla, mostrar un mensaje de error
    except:
        # Establecer el resultado a "Error"
        resultado.set("Error")

# Crear una función para calcular la tangente del resultado
def tangente_resultado():
    # Obtener el valor actual del resultado
    valor = resultado.get()
    # Intentar calcular la tangente usando la función math.tan
    try:
        # Si el cálculo es exitoso, establecer el resultado al valor de la tangente en grados
        resultado.set(math.tan(math.radians(float(valor))))
    # Si el cálculo falla, mostrar un mensaje de error
    except:
        # Establecer el resultado a "Error"
        resultado.set("Error")

# Crear una función para calcular la raíz cuadrada del resultado
def raiz_resultado():
    # Obtener el valor actual del resultado
    valor = resultado.get()
    # Intentar calcular la raíz cuadrada usando la función math.sqrt
    try:
        # Si el cálculo es exitoso, establecer el resultado al valor de la raíz cuadrada
        resultado.set(math.sqrt(float(valor)))
    # Si el cálculo falla, mostrar un mensaje de error
    except:
        # Establecer el resultado a "Error"
        resultado.set("Error")

# Crear una función para calcular el logaritmo del resultado
def log_resultado():
    # Obtener el valor actual del resultado
    valor = resultado.get()
    # Intentar calcular el logaritmo usando la función math.log10
    try:
        # Si el cálculo es exitoso, establecer el resultado al valor del logaritmo en base 10
        resultado.set(math.log10(float(valor)))
    # Si el cálculo falla, mostrar un mensaje de error
    except:
        # Establecer el resultado a "Error"
        resultado.set("Error")

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, textvariable=resultado, font=("Arial", 20), bg="white", anchor="e")
etiqueta_resultado.grid(row=0, column=0, columnspan=5, sticky="nsew")

# Crear los botones de los dígitos y los operadores
boton_1 = tk.Button(ventana, text="1", font=("Arial", 20), command=lambda: actualizar_resultado("1"))
boton_2 = tk.Button(ventana, text="2", font=("Arial", 20), command=lambda: actualizar_resultado("2"))
boton_3 = tk.Button(ventana, text="3", font=("Arial", 20), command=lambda: actualizar_resultado("3"))
boton_4 = tk.Button(ventana, text="4", font=("Arial", 20), command=lambda: actualizar_resultado("4"))
boton_5 = tk.Button(ventana, text="5", font=("Arial", 20), command=lambda: actualizar_resultado("5"))
boton_6 = tk.Button(ventana, text="6", font=("Arial", 20), command=lambda: actualizar_resultado("6"))
boton_7 = tk.Button(ventana, text="7", font=("Arial", 20), command=lambda: actualizar_resultado("7"))
boton_8 = tk.Button(ventana, text="8", font=("Arial", 20), command=lambda: actualizar_resultado("8"))
boton_9 = tk.Button(ventana, text="9", font=("Arial", 20), command=lambda: actualizar_resultado("9"))
boton_0 = tk.Button(ventana, text="0", font=("Arial", 20), command=lambda: actualizar_resultado("0"))
boton_punto = tk.Button(ventana, text=".", font=("Arial", 20), command=lambda: actualizar_resultado("."))
boton_suma = tk.Button(ventana, text="+", font=("Arial", 20), command=lambda: actualizar_resultado("+"))
boton_resta = tk.Button(ventana, text="-", font=("Arial", 20), command=lambda: actualizar_resultado("-"))
boton_multiplicacion = tk.Button(ventana, text="*", font=("Arial", 20), command=lambda: actualizar_resultado("*"))
boton_division = tk.Button(ventana, text="/", font=("Arial", 20), command=lambda: actualizar_resultado("/"))
boton_borrar = tk.Button(ventana, text="C", font=("Arial", 20), command=borrar_resultado)
boton_igual = tk.Button(ventana, text="=", font=("Arial", 20), command=evaluar_resultado)
boton_seno = tk.Button(ventana, text="sin", font=("Arial", 20), command=seno_resultado)
boton_coseno = tk.Button(ventana, text="cos", font=("Arial", 20), command=coseno_resultado)
boton_tangente = tk.Button(ventana, text="tan", font=("Arial", 20), command=tangente_resultado)
boton_raiz = tk.Button(ventana, text="√", font=("Arial", 20), command=raiz_resultado)
boton_log = tk.Button(ventana, text="log", font=("Arial", 20), command=log_resultado)

# Colocar los botones en la cuadrícula de la ventana
boton_1.grid(row=4, column=0, sticky="nsew")
boton_2.grid(row=4, column=1, sticky="nsew")
boton_3.grid(row=4, column=2, sticky="nsew")
boton_4.grid(row=3, column=0, sticky="nsew")
boton_5.grid(row=3, column=1, sticky="nsew")
boton_6.grid(row=3, column=2, sticky="nsew")
boton_7.grid(row=2, column=0, sticky="nsew")
boton_8.grid(row=2, column=1, sticky="nsew")
boton_9.grid(row=2, column=2, sticky="nsew")
boton_0.grid(row=5, column=0, columnspan=2, sticky="nsew")
boton_punto.grid(row=5, column=2, sticky='nsew')