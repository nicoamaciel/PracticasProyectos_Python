from tkinter import*
#Ejercicio mini calculadora - interfaz grafica - Maciel Nicolas
"""////////////////////////////////////////////////////////////////////////"""
#Funcion que reciben los botones (proceso y cambio de variable)

def sumar():
    resultado.set(int(var1.get())+ int(var2.get()))

def restar():
    resultado.set(int(var1.get())- int(var2.get()))
"""////////////////////////////////////////////////////////////////////////"""




root=Tk()#Raiz principal de ventana //////////////////////////////////////////////////////

root.title("Mini calculadora") #Titulo de ventana


frame = Frame(root)#Marco 
frame.pack()

frame.config(width=400, height=600) #Tamaño de marco

frame.config(cursor="pirate") #Por dentro del Frame(Marco) el cursor se transforma en un barco
frame.config(bg="green") #Color de Frame(Marco)
frame.config(bd="20")#tamaño de borde (Aplicar formato para visualizar)
#miFrame.config(relief="sunken") #Viusalizacion de medio marco
frame.config(relief="ridge") #Viusalizacion de marco completo

root.config(cursor="boat")#Modificacion de cursor en raiz 
root.config(bg="gray50")#Color de raiz 
root.config(bd="25")#tamaño de raiz
root.config(relief="sunken")#Visualizacion de medio marco

#Variable y rotorno. Configurar con entradas
var1 = StringVar() 
var2 = StringVar()
resultado = StringVar()

entrada1 = Entry (frame) #Ingreso de datos 1
entrada1.pack()
entrada1.config(bd=5, font=("Arial 10"), textvariable=var1)

entrada2 = Entry (frame) #Ingreso de datos 2
entrada2.pack()
entrada2.config(bd=5, font=("Arial 10"), textvariable=var2)

entrada3 = Entry (frame) #Salida de datos (Resultado) 
entrada3.pack()
entrada3.config(bd=10, font=("Arial 10"), state="disabled", textvariable=resultado) 
#Cancelar ingreso en entrada 3 para que no se manipule con state="disabled"

boton1 = Button(frame, text="Sumar") #Boton de suma
boton1.pack()
boton1.config(bd=5, font=("Arial 10"), command=sumar)


boton2 = Button(frame, text="Restar") #Boton de suma
boton2.pack()
boton2.config(bd=5, font=("Arial 10"), command=restar)





root.mainloop() #//////////////////////////////////////////////////////////////
