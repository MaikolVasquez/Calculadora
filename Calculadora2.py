from tkinter import *

root = Tk()
root.geometry("450x400")

primernumero=0
segundonumero=0
operacion=0


txtentry = Entry(root, width=30, font=(None,20))
txtentry.grid(columnspan=10, row=0, column=0, pady=10)


def Clear():
    txtentry.delete(first=0,last=END)
    global primernumero,segundonumero,operacion
    primernumero = 0
    segundonumero = 0
    operacion = 0
    

limpiar=Button(root,command=Clear)
limpiar.place(x=150,y=50)
limpiar.configure(text="C",font=("Brush Script MT",20))

cero0=Button(root, command=lambda : txtentry.insert(END,"0"))
cero0.place(x=0,y=200)
cero0.configure(text="0",font=("Brush Script MT",20))


uno1=Button(root,command=lambda : txtentry.insert(END,"1"))
uno1.place(x=0,y=50)
uno1.configure(text="1",font=("Brush Script MT",20))


dos2=Button(root,command=lambda : txtentry.insert(END,"2"))
dos2.place(x=50,y=50)
dos2.configure(text="2",font=("Brush Script MT",20))


tres3=Button(root,command=lambda : txtentry.insert(END,"3"))
tres3.place(x=100,y=50)
tres3.configure(text="3",font=("Brush Script MT",20))


cuatro4=Button(root,command=lambda : txtentry.insert(END,"4"))
cuatro4.place(x=0,y=100)
cuatro4.configure(text="4",font=("Brush Script MT",20))


cinco5=Button(root,command=lambda : txtentry.insert(END,"5"))
cinco5.place(x=50,y=100)
cinco5.configure(text="5",font=("Brush Script MT",20))


seis6=Button(root,command=lambda : txtentry.insert(END,"6"))
seis6.place(x=100,y=100)
seis6.configure(text="6",font=("Brush Script MT",20))


siete7=Button(root,command=lambda : txtentry.insert(END,"7"))
siete7.place(x=0,y=150)
siete7.configure(text="7",font=("Brush Script MT",20))


ocho8=Button(root,command=lambda : txtentry.insert(END,"8"))
ocho8.place(x=50,y=150)
ocho8.configure(text="8",font=("Brush Script MT",20))


nueve9=Button(root,command=lambda : txtentry.insert(END,"9"))
nueve9.place(x=100,y=150)
nueve9.configure(text="9",font=("Brush Script MT",20))


def sumar():
    global primernumero,operacion
    primernumero=int(txtentry.get())
    txtentry.delete(first=0, last=END)
    operacion="sumar"
    

suma=Button(root,command=sumar)
suma.place(x=0,y=250)
suma.configure(text="+",font=("Brush Script MT",20))

def restar():
    global primernumero,operacion
    primernumero=int(txtentry.get())
    txtentry.delete(first=0, last=END)
    operacion="resta"

resta=Button(root,command=restar)
resta.place(x=50,y=250)
resta.configure(text="-",font=("Brush Script MT",20))

def multiplicar():
    global primernumero,operacion
    primernumero=int(txtentry.get())
    txtentry.delete(first=0, last=END)
    operacion="multiplica"

multi=Button(root,command=multiplicar)
multi.place(x=100,y=250)
multi.configure(text="*",font=("Brush Script MT",20))

def dividir():
    global primernumero,operacion
    primernumero=int(txtentry.get())
    txtentry.delete(first=0, last=END)
    operacion="divide"

divid=Button(root,command=dividir)
divid.place(x=150,y=250)
divid.configure(text="/",font=("Brush Script MT",20))

def igualar():
    global segundonumero
    segundonumero = int(txtentry.get())
    txtentry.delete(first=0,last=END)
    if operacion == "sumar":
        resultado=primernumero+segundonumero
        txtentry.insert(0,str(resultado))
    elif operacion == "resta":
        resultado=primernumero-segundonumero
        txtentry.insert(0,str(resultado))
    elif operacion == "multiplica":
        resultado=primernumero*segundonumero
        txtentry.insert(0,str(resultado))
    elif operacion == "divide":
        resultado=primernumero/segundonumero
        txtentry.insert(0,str(resultado))


igual=Button(root,command=igualar)
igual.place(x=200,y=250)
igual.configure(text="=",font=("Brush Script MT",20))


root.mainloop()

