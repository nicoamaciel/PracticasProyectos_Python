from tkinter import*

i = 0

def click(valor): #funcion entrada de datos y comando de botones
    global i
    entrada.insert(i, valor)
    i+=1 #indice 1 para vaya de izquierda a derencha en metodo de ingreso 

def borrar(): #Funcion borrar caracteres 
    entrada.delete(0, END)
    i=0

#FUNCION OPERACIONES
def operaciones():
    operacion = entrada.get()
    resultado = eval (operacion)
    entrada.delete(0,END)
    entrada.insert(0,resultado)
    i=0

root=Tk()
root.title("Calculadora Nicolas")

#Entrada
entrada = Entry(root, font=("Arial 20"))
entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=5) #Grid centrar columna y fila 

#Botones

boton1 = Button(root, text="1", width=5, height=2, command=lambda:click(1)) #1
boton2 = Button(root, text="2", width=5, height=2, command=lambda:click(2)) #2
boton3 = Button(root, text="3", width=5, height=2, command=lambda:click(3)) #3
boton4 = Button(root, text="4", width=5, height=2, command=lambda:click(4)) #4
boton5 = Button(root, text="5", width=5, height=2, command=lambda:click(5)) #5
boton6 = Button(root, text="6", width=5, height=2, command=lambda:click(6)) #6
boton7 = Button(root, text="7", width=5, height=2, command=lambda:click(7)) #7
boton8 = Button(root, text="8", width=5, height=2, command=lambda:click(8)) #8
boton9 = Button(root, text="9", width=5, height=2, command=lambda:click(9)) #9
boton0 = Button(root, text="0", width=13, height=2, command=lambda:click(0)) #0

boton_borrar = Button(root, text="DEL", width=5, height=2, command=lambda:borrar()) #BORRAR
boton_parentesis1 = Button(root, text="(", width=5, height=2, command=lambda:click("(")) #abre
boton_parentesis2 = Button(root, text=")", width=5, height=2, command=lambda:click(")")) #cierra
boton_punto = Button(root, text=".", width=5, height=2, command=lambda:click(".")) #punto

#Operaciones
boton_div = Button(root, text="/", width=5, height=2, command=lambda:click("/")) #division
boton_mult = Button(root, text="*", width=5, height=2, command=lambda:click("*")) #multiplicacion
boton_sum = Button(root, text="+", width=5, height=2, command=lambda:click("+")) #suma
boton_rest = Button(root, text="-", width=5, height=2, command=lambda:click("-")) #resta
boton_igual = Button(root, text="=", width=5, height=2, command=lambda:operaciones()) #igual

#Colocar botones
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_sum.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_rest.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5) #se inserta columnspan para que el boton ocupe dos columnas!
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)











root.mainloop()