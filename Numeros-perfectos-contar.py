#Numeros-perfectos-contar

import tkinter as tk  # Importa la librería tkinter y la renombra como tk para facilitar su uso en el código.

def suma_divisores(num):  #Define una función llamada suma_divisores que recibe un número num como argumento.
    suma = 0  #Inicializa una variable suma en 0.
    for i in range(1, num):  # Inicia un bucle for que recorre los números desde 1 hasta num-1.
        if num % i == 0:  #Verifica si num es divisible entre i.
            suma += i  #Si i es divisor de num, se suma a la variable suma.
    return suma  #Retorna la suma de los divisores de num.

def contar_numeros_perfectos(fin):  #Define una función llamada contar_numeros_perfectos que recibe un límite superior fin.
    contador = 0  #Inicializa un contador en 0.
    numeros_perfectos = []  # Inicializa una lista vacía para almacenar los números perfectos encontrados.

    for num in range(1, fin+1): # Inicia un bucle que recorre los números desde 1 hasta fin.
        if suma_divisores(num) == num:  #Verifica si la suma de los divisores de num es igual a num.
            contador += 1  # Incrementa el contador si num es un número perfecto.
            numeros_perfectos.append(num)  #Agrega el número perfecto a la lista.

    return contador, numeros_perfectos  #Retorna la cantidad de números perfectos encontrados y la lista de números perfectos.

def calcular_numeros_perfectos():  #Define una función para calcular los números perfectos basándose en el valor ingresado por el usuario.
    fin = int(entry.get())  #Obtiene el valor ingresado por el usuario en la entrada y lo convierte a entero.
    cantidad_perfectos, numeros_perfectos = contar_numeros_perfectos(fin)  #Llama a la función para contar los números perfectos hasta el valor ingresado.

    result_label.config(text=f"La cantidad de números perfectos hasta el valor {fin} es: {cantidad_perfectos}")  #Actualiza el texto de la etiqueta de resultado con la cantidad de números perfectos encontrados.
    
    if cantidad_perfectos > 0:  
        perfectos_str = ", ".join(str(num) for num in numeros_perfectos)  #Convierte los números perfectos encontrados en una cadena separada por comas.
        perfectos_label.config(text=f"Números perfectos encontrados: {perfectos_str}")  #Actualiza el texto de la etiqueta con la lista de números perfectos si se encontraron algunos.
    else:
        perfectos_label.config(text="No se encontraron números perfectos en el rango.")  

# Crear la ventana
root = tk.Tk()  #Crea la ventana principal de la interfaz gráfica.
root.title("Calculadora de Números Perfectos")

# Crear etiqueta y entrada para el número
label = tk.Label(root, text="Ingrese un número:")
label.pack()

entry = tk.Entry(root)
entry.pack()

# Botón para calcular los números perfectos
button = tk.Button(root, text="Calcular", command=calcular_numeros_perfectos)
button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="")
result_label.pack()

# Etiqueta para mostrar los números perfectos encontrados
perfectos_label = tk.Label(root, text="")
perfectos_label.pack()

# Ejecutar la ventana
root.mainloop()  #Inicia el bucle principal de eventos para mostrar la ventana y esperar interacciones del usuario.
