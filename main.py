from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("500x300")

primer_valor = None
operacion = None

def agregar_numero(numero):
    pantalla.delete(0, "end")
    contenido_pantalla = pantalla.get()
    pantalla.insert(0, contenido_pantalla + numero)

def guardar_operacion(operador):
    global primer_valor, operacion
    primer_valor = pantalla.get()
    operacion = operador
    pantalla.delete(0, "end")

def calcular_resultado():
    segundo_valor = pantalla.get()
    if primer_valor is not None and operacion is not None:
        if operacion == "+":
            resultado = float(primer_valor) + float(segundo_valor)
        elif operacion == "-":
            resultado = float(primer_valor) - float(segundo_valor)
        elif operacion == "*":
            resultado = float(primer_valor) * float(segundo_valor)
        elif operacion == "/":
            resultado = float(primer_valor) / float(segundo_valor)
        pantalla.delete(0, "end")
        pantalla.insert(0, str(resultado))
        

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=5, padx=0, pady=10)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("1")).grid(row=1, column=0, padx=1, pady=1,sticky="ew")
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("2")).grid(row=1, column=1, padx=1, pady=1,sticky="ew")
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("3")).grid(row=1, column=2, padx=1, pady=1,sticky="ew")
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("4")).grid(row=2, column=0, padx=1, pady=1,sticky="ew")
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("5")).grid(row=2, column=1, padx=1, pady=1,sticky="ew")
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("6")).grid(row=2, column=2, padx=1, pady=1,sticky="ew")
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("7")).grid(row=3, column=0, padx=1, pady=1,sticky="ew")
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("8")).grid(row=3, column=1, padx=1, pady=1,sticky="ew")
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("9")).grid(row=3, column=2, padx=1, pady=1,sticky="ew")
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command=calcular_resultado).grid(row=4, column=0, columnspan=2, padx=1, pady=1,sticky="ew")
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=lambda: agregar_numero(".")).grid(row=4, column=2, padx=1, pady=1,sticky="ew")
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: guardar_operacion("+")).grid(row=1, column=3, padx=1, pady=1,sticky="ew")
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda: guardar_operacion("-")).grid(row=2, column=3, padx=1, pady=1,sticky="ew")
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda: guardar_operacion("*")).grid(row=3, column=3, padx=1, pady=1,sticky="ew")
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda: guardar_operacion("/")).grid(row=4, column=3, padx=1, pady=1,sticky="ew")

root.mainloop()