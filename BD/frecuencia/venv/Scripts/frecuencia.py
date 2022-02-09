import math
from tkinter import *

raiz = Tk()
raiz.title("Conversor de wt a Tiempo")
#raiz.resizable(0,0) # Para que pueda o no redimensionarse

#raiz.geometry("650x350")
raiz.config(bg = "white")
raiz.iconbitmap("pp.ico")

tiempovar = StringVar()
ff = StringVar()
wtvar = StringVar()


miFrame = Frame()
miFrame.pack()
miFrame.config(bg = "white")
miFrame.config(width = "450",height = "400")
Label(miFrame,text = "Conversor de wt a Tiempo",fg="black",font=("Times New Roman",15),bg = "white").grid(row = 0,column=1)

Label(miFrame,text = "Frecuencia",fg="black",font=("Times New Roman",15),bg = "white").grid(row=1,column=0)
frecuencia = Entry(miFrame,fg="black",font=("Times New Roman",15),bg = "white",justify = "center",textvariable = ff)
frecuencia.grid(row = 2,column=0,padx = 20,pady =10)

Label(miFrame,text = "wt",fg="black",font=("Times New Roman",15),bg = "white").grid(row=1,column=2)
wt = Entry(miFrame,fg="black",font=("Times New Roman",15),bg = "white",justify = "center",textvariable = wtvar)
wt.grid(row = 2,column=2,padx = 20,pady =10)

Label(miFrame,text = "tiempo [ms] ",fg="black",font=("Times New Roman",15),bg = "white").grid(row=3,column=1)
tiempo = Entry(miFrame,fg="black",font=("Times New Roman",15),bg = "white",justify = "center", textvariable = tiempovar)
tiempo.grid(row = 4,column=1,padx = 20,pady =10)

def codigoBoton():
    algo = wtvar.get()
    algo = S
    tiempo_en_ms = ((1/int(ff.get()))*float(wtvar.get()))/2*math.pi
    tiempovar.set(tiempo_en_ms)

boton_cal = Button(raiz,text = "Calcular", command = codigoBoton)
boton_cal.pack(padx = 20,pady =10)





raiz.mainloop()