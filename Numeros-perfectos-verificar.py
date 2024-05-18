#Calcular Numeros perfectos

import tkinter as tk 
 
def es_numero_perfecto(num): 
    suma = 0 
    for i in range(1, num): 
        if num % i == 0: 
            suma += i 
    return suma == num 
 
def verificar_numero(event=None): 
    try: 
        num = int(entry.get()) 
    except ValueError: 
        result_label.config(text="Error: Por favor ingrese un número entero válido.") 
        return 
     
    if es_numero_perfecto(num): 
        result_label.config(text=f"El número {num} es perfecto.") 
    else: 
        result_label.config(text=f"El número {num} no es perfecto.") 
 
root = tk.Tk() 
root.title("Verificador de Números Perfectos") 
root.configure(bg='#C0C0C0')  # Color azul plateado 
root.geometry("600x400")

label = tk.Label(root, text="Ingrese un número:", bg='#C0C0C0') 
label.pack() 
 
entry = tk.Entry(root) 
entry.pack() 
entry.bind("<Return>", verificar_numero)  # Funciona al presionar Enter 
 
button = tk.Button(root, text="Verificar", command=verificar_numero) 
button.pack() 
 
result_label = tk.Label(root, text="", bg='#C0C0C0') 
result_label.pack() 
 
root.mainloop()
