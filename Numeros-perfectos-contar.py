import tkinter as tk 
import math 
 
def suma_divisores(num): 
    suma = 1 
    raiz_num = int(math.sqrt(num)) + 1 
    for i in range(2, raiz_num): 
        if num % i == 0: 
            suma += i 
            if i != num // i: 
                suma += num // i 
    return suma 
 
def contar_numeros_perfectos(fin): 
    contador = 0 
    numeros_perfectos = (num for num in range(2, fin+1) if suma_divisores(num) == num) 
    numeros_perfectos = list(numeros_perfectos) 
    contador = len(numeros_perfectos) 
    return contador, numeros_perfectos 
 
def calcular_numeros_perfectos(event=None): 
    value = entry.get() 
     
    try: 
        fin = int(value) 
    except ValueError: 
        result_label.config(text="Error: Por favor ingrese un número entero válido.") 
        perfectos_label.config(text="") 
        return 
 
    cantidad_perfectos, numeros_perfectos = contar_numeros_perfectos(fin) 
 
    result_label.config(text=f"La cantidad de números perfectos hasta el valor {fin} es: {cantidad_perfectos}") 
    perfectos_str = ", ".join(str(num) for num in numeros_perfectos) 
    perfectos_label.config(text=f"Números perfectos encontrados: {perfectos_str}" if cantidad_perfectos > 0 else "No se encontraron números perfectos en el rango.") 
 
# Crear la ventana 
root = tk.Tk() 
root.title("Calculadora de Números Perfectos") 
 
# Personalizar la apariencia de la ventana 
root.configure(bg="#C0C0C0")  # Establecer el color de fondo a azul claro 
root.geometry("600x400")  # Establecer el tamaño de la ventana a 30cm x 30cm 
 
# Crear etiqueta y entrada para el número 
label = tk.Label(root, text="Ingrese un número:") 
label.pack() 
 
entry = tk.Entry(root) 
entry.pack() 
entry.bind("<Return>", calcular_numeros_perfectos) 
 
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
root.mainloop()