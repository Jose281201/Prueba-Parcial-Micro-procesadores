#Calcular Numeros perfectos

import tkinter as tk

def es_numero_perfecto(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    return suma == num

def verificar_numero():
    num = int(entry.get())
    if es_numero_perfecto(num):
        result_label.config(text=f"El número {num} es perfecto.")
    else:
        result_label.config(text=f"El número {num} no es perfecto.")

root = tk.Tk()
root.title("Verificador de Números Perfectos")

label = tk.Label(root, text="Ingrese un número:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Verificar", command=verificar_numero)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
