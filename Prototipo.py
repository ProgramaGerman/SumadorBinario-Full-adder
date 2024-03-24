# importaciones
from tkinter import *

# Variables globales
output = []


# Funciones internas de operaciones
def Or(varx, vary):
    if varx | vary:
        return 1
    return 0


def And(varx, vary):
    if varx & vary:
        return 1
    return 0


def Not(var):
    if var == 0:
        return 1
    return 0


def Xor(varx, vary):
    return Or(And(Not(varx), vary), And(varx, Not(vary)))


def primerSuma(
    varx,
    vary,
):
    sum2 = Xor(varx, vary)
    carry = And(varx, vary)
    return (
        sum2,
        carry,
    )


def Sumador(varx, vary, Cin):
    """Sumador

    Args:
        varx (_type_): primer campo
        vary (_type_): segundo campo
        Cin (_type_): acarreo

    Returns:
        varSalida: la lista con los datos
    """
    xor1 = Xor(Xor(varx, vary), Cin)
    and1 = And(Xor(varx, vary), Cin)
    carrey = Or(and1, And(varx, vary))

    return xor1, carrey


def SumarMultiplesVariables(var1, var2):
    output = []  # Lista final de salida
    i = len(var1) - 1
    if i == len(var1) - 1:
        sum, carry = primerSuma(var1[i], var2[i])
        output.append(sum)
        i -= 1
    while i > -1:
        sum2, carry = Sumador(var1[i], var2[i], carry)
        output.append(sum2)
        i -= 1
    if carry == 1:
        output.append(carry)
    output.reverse()
    return output


# Funciones secundarias de manipulacion de las listas
def iniciarLista(varLista):
    for i in range(len(varLista)):
        if varLista[i] == "":
            varLista[i] = 0
    return varLista


def igualar_listas(lista1, lista2):
    cant1 = len(lista1)
    cant2 = len(lista2)

    if cant1 > cant2:
        i = cant2
        while i < cant1:
            lista2.append(0)
            i += 1
    elif cant2 > cant1:
        i = cant1
        while i < cant2:
            lista1.append(0)
            i += 1
    return lista1, lista2

def limpiar_campos():
  """Función para limpiar los campos de entrada de texto."""
  valor1.set("")
  valor2.set("")


# Interfaces
def asignar():
    acum = ""
    var1 = []
    var2 = []
    j = []
    indice1 = valor1.get()
    if indice1.isnumeric():
        for i in indice1:
            j += i.split()
        varaux = j
    else:
        Label(root, text="No se admite letras", background="red3").place(x=610, y=80)

    for i in range(len(varaux)):
        var1.append(int(varaux[i]))

    j = []
    indice2 = valor2.get()
    if indice2.isnumeric():
        for i in indice2:
            j += i.split()
        varaux = j
    else:
        Label(root, text="No se admite letras", bg="red3").place(x=610, y=100)
    for i in range(len(varaux)):
        var2.append(int(varaux[i]))

    var1, var2 = igualar_listas(var1, var2)

    var_salida = SumarMultiplesVariables(var1, var2)

    for i in var_salida:
        acum += str(i)
    # mensaje de salida
    salida1 = Label(root, text=acum, bg="goldenrod3")
    salida1.place(x=600, y=180)


# funcion de acerca de:
def acerca():
    """Funcion que genera una ventana llamada acerca de, con los datos de los creadores del software"""
    ventana = Toplevel()
    ventana.title("Acerca de")
    ventana.geometry("300x400")
    ventana.config(bg="goldenrod3")

    # Mostar Mensaje de Instrucciones
    Label(
        ventana,
        text="Realizado Por:\n German Gonzalez CI:30.707.833\nVictorialys Salazar CI:30.065.702",
        bg="goldenrod3",
        font="Calibri 9",
    ).place(x=70, y=20)
    Label(
        ventana,
        text="Universidad de Oriente\nNucleo Nueva Esparta\nDepartamento de Estudio de Ingeniería y\n Ciencias Aplicadas",
        bg="goldenrod3",
    ).place(x=40, y=100)
    Label(
        ventana,
        text="Este programa es de codigo abierto (Open Source)\n por lo que es libre de darle uso comercial\n o con fines educativos",
        bg="goldenrod3",
        font="calibri 9",
    ).place(x=20, y=230)
    Button(
        ventana,
        text="Cerrar",
        bg="goldenrod3",
        bd=3,
        anchor="sw",
        command=ventana.destroy,
    ).place(x=125, y=290)


# funcion para instrucciones
def instruccion():
    root2 = Toplevel()
    root2.geometry("300x250")
    root2.config(background="goldenrod3")
    root2.title("Instrucciones")
    Label(
        root2,
        text="Instrucciones\n1.Paso: Ingrese para los valores A y B\n 2.Paso: Presione el boton de Resultado\n para que le arroje la Suma.\n Importante: Solo acepta los numeros\n en Binarios (1,0)",
        bg="goldenrod3",
    ).pack(pady=20)
    Button(root2, text="Cerrrar", bg="goldenrod3", bd=3, command=root2.destroy).pack(
        pady=40
    )


# Inicio del programa
root = Tk()
valor1, valor2 = StringVar(), StringVar()
root.geometry("720x380")
root.resizable(0, 0)

root.title("Sumador")
root.config(bg="goldenrod3")
labelInicio = Label(
    root,
    text="Bienvenido al Simulador de un Sumador Completo",
    bg="goldenrod3",
    font="calibri 20",
)
labelInicio.pack()


Label(root, text="Ingrese el valor A:", bg="goldenrod3").place(x=20, y=80)
Entry(root, textvariable=valor1, bd=3).place(x=125, y=80)

Label(root, text="Ingrese el valor B:", bg="goldenrod3").place(x=20, y=100)
Entry(root, textvariable=valor2, bd=3).place(x=125, y=100)

# Boton para limpiar campos
boton_limpiar = Button(
    text="Limpiar",
    bg="goldenrod3",
    bd=3,
    command=limpiar_campos,
)
boton_limpiar.place(x=120, y=210)

# boton para operar
boton1 = Button(text="Resultado", bg="goldenrod3", command=asignar)
boton1.place(x=120, y=150)

# boton a mostrar la ventana acerca
botonAcerca = Button(text="Acerca de:", bg="goldenrod3", command=acerca)
botonAcerca.place(x=120, y=300)

# imagen del sumador
imagen = PhotoImage(file="imagen\Icono.gif ")
lblImg = Label(root, image=imagen, height=170, width=320)
lblImg.place(x=260, y=80)


# Boton para Instrucciones
Button(
    text="Instrucciones", bg="goldenrod3", font="callibri 9", command=instruccion
).place(x=120, y=180)

# boton de cierre
Button(
    text="Cerrar",
    bg="goldenrod3",
    bd=3,
    anchor="sw",
    command=root.destroy,
).place(x=600, y=300)


root.mainloop()
