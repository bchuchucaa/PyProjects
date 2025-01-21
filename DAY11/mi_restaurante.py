from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operator = ''

def click_boton(numero):
    global operator
    operator = operator + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operator)

def borrar():
    global operator
    operator = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operator
    resultado = str(eval(operator))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operator = ''   



def revisar_check():
    contador_c = 0
    contador_b = 0
    contador = 0
    total_comida = 0
    for comida in cuadros_comida:
        if(variables_comida[contador_c].get() == 1):
            cuadros_comida[contador_c].config(state = NORMAL)
            if(cuadros_comida[contador_c].get()== 0):
                cuadros_comida[contador_c].delete(0, END)
            cuadros_comida[contador_c].focus()
        else:
            cuadros_comida[contador_c].config(state = DISABLED)
            texto_comida[contador_c].set('0')
        # total_comida += float(texto_comida[contador_c])
        contador_c+=1
    for bebida in cuadros_bebida:
        if(variables_bebida[contador_b].get() == 1):
            cuadros_bebida[contador_b].config(state = NORMAL)
            if(cuadros_comida[contador_b].get()== 0):
                cuadros_bebida[contador_b].delete(0, END)
            cuadros_bebida[contador_b].focus()
        else:
            cuadros_bebida[contador_b].config(state = DISABLED)
            texto_bebida[contador_b].set('0')
        contador_b+=1
    
    for postre in cuadros_postre:
        if(variables_postres[contador].get() == 1):
            cuadros_postre[contador].config(state = NORMAL)
            cuadros_postre[contador].delete(0, END)
            cuadros_postre[contador].focus()
        else:
            cuadros_postre[contador].config(state = DISABLED)
            texto_postre[contador].set('0')

        contador+=1

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65,2.20]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58, 2,50]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74,10.20]        
    
def calcular_totales():
    sub_total_comida = 0
    sub_total_bebida = 0
    sub_total_postre = 0
    p = 0
    for cantidad in texto_comida:
         sub_total_comida+= float(float(cantidad.get())*precios_comida[p])
         p += 1
    pb = 0
    for bebida in texto_bebida:
         sub_total_bebida+= float(float(bebida.get())*precios_bebida[pb])
         pb += 1
    pp = 0
    for postre in texto_postre:
         sub_total_postre+= float(float(postre.get())*precios_postres[pp])
         pp += 1
    subtotal = sub_total_postre + sub_total_bebida + sub_total_comida
    impuesto = subtotal * 0.07
    total = subtotal + impuesto

    var_costo_comida.set(f'${round(sub_total_comida,2)}')
    var_costo_bebida.set(f'${round(sub_total_bebida,2)}')
    var_costo_postre.set(f'${round(sub_total_postre,2)}')
    var_costo_subtotal.set(f'${round(subtotal,2)}')
    var_impuesto.set(f'{round(impuesto,2)}')
    var_total.set(f'{round(total,2)}')

def generar_recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 999999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{ fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t {num_recibo}\t\t{fecha_recibo}'+'\n')
    texto_recibo.insert(END,f'*' * 60 + '\n')
    texto_recibo.insert(END,'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END,f'-'*68+'\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{comida_list[x]}\t\t{comida.get()}\t'+
                                f'${int(comida.get())* precios_comida[x]}\n')
        x += 1
    y = 0    
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{bebida_list[y]}\t\t{bebida.get()}\t'+
                                f'${int(bebida.get())* precios_bebida[y]}\n')
        y += 1 
    z = 0 
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{postres_list[z]}\t\t{postre.get()}\t'+
                                f'${int(postre.get())* precios_postres[z]}\n')
        z += 1  
    texto_recibo.insert(END, f'Costo de la comida\t\t\t {var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la bebida\t\t\t {var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de la postre\t\t\t {var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'*'*65+'\n')
    
    texto_recibo.insert(END, f'Subtotal\t\t\t{var_costo_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos\t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total\t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, 'Gracias por tu compra')

def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion','Su recibo ha sido guardado')

def reset():
    texto_recibo.delete(0.1, END)
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state = DISABLED)
    
    for cuadro in cuadros_bebida:
        cuadro.config(state = DISABLED)
    
    for cuadro in cuadros_postre:
        cuadro.config(state = DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in var_costo_postre:
        v.set(0)
    
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_costo_subtotal('')
    var_impuesto('')
    var_total('')

application = Tk()

#Screen size

application.geometry('1220x630+0+0')

#avoid maximizer
application.resizable(0,0)

#title
application.title("BRYAN DELI")

#BACKGROUND COLOR
application.config(bg='burlywood')

#panel superior
panel_superior = Frame(application, bd=1,relief=RAISED)
panel_superior.pack(side=TOP)

#TITLE
tag_tittle = Label(panel_superior,text="Sistema de Facturacion",fg='azure4'
                   ,font=('Dosis',58), bg='burlywood',width=27)

tag_tittle.grid(row=0,column=0)

#panel izquierdo
panel_izquierdo = Frame(application, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#PANEL COSTOS
panel_costos = Frame(panel_izquierdo, bd=1, relief=RAISED,bg='azure4',padx='50')
panel_costos.pack(side=BOTTOM)

#PANEL COMIDAS 
panel_comidas = LabelFrame(panel_izquierdo,text='COMIDA',
                           font=('Dosis',19,'bold'), bd=1, relief=RAISED,foreground='azure4')
panel_comidas.pack(side=LEFT)

#PANEL BEBIDAS
panel_bebidas = LabelFrame(panel_izquierdo,text='BEBIDAS',
                           font=('Dosis',19,'bold'), bd=1, relief=RAISED,foreground='azure4')
panel_bebidas.pack(side=LEFT)

#PANEL postres 
panel_postres = LabelFrame(panel_izquierdo,text='POSTRES',
                           font=('Dosis',19,'bold'), bd=1, relief=RAISED,foreground='azure4')
panel_postres.pack(side=LEFT)

#PANEL DERECHO
panel_derecho = Frame(application, bd=1,relief=FLAT)
panel_derecho.pack(side=RIGHT)



#PANEL calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief=RAISED, bg='burlywood')
panel_calculadora.pack(side=TOP)

#PANEL RECIBO
panel_RECIBO = Frame(panel_derecho, bd=1, relief=RAISED, bg='burlywood')
panel_RECIBO.pack(side=TOP)

#PANEL BOTONES
panel_botones = Frame(panel_derecho, bd=1, relief=RAISED, bg='burlywood')
panel_botones.pack(side=TOP,padx=5)

#lista de comidas
comida_list = [
        "Chicken", "Beef", "Salmon", "Tofu", "Eggs", 
        "Pork", "Lentils", "Chickpeas", "Tempeh"
    ]

bebida_list = [
        "Coffee", "Tea", "Water", "Orange juice", "Milkshake", 
        "Smoothie", "Soda", "Lemonade", "Iced tea"
    ]
postres_list = [
        "Chocolate", "Cake", "Pie", "Cookies", "Cupcakes", 
        "Donuts", "Ice cream", "Brownies", "Pastries"
    ]   

#generar items comida
variables_comida = []
variables_bebida = []
variables_postres = []

#cantidad items
cuadros_comida = []
texto_comida = []
cuadros_bebida = []
texto_bebida = []
cuadros_postre = []
texto_postre = []

#contadores
counter = 0
counter_bebida = 0
counter_postres = 0

for comida in comida_list:
    #crear los checkbutton
    variables_comida.append('')
    variables_comida[counter] = IntVar()
    comida = Checkbutton(panel_comidas, text= comida.title(),
                         font=('Dosis',19,'bold'),
                         offvalue=0,
                         onvalue=1, variable=variables_comida[counter],
                         command=revisar_check)
    comida.grid(row=counter,column=0, sticky=W) 
    #crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[counter] = StringVar()
    texto_comida[counter].set('0')
    cuadros_comida[counter] = Entry(panel_comidas,
                                    font='Dosis',
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_comida[counter])
    cuadros_comida[counter].grid(row=counter,column=1)
    counter+=1

for bebida in bebida_list:
    variables_bebida.append('')
    variables_bebida[counter_bebida] = IntVar()
    bebida = Checkbutton(panel_bebidas, text= bebida.title(),font=('Dosis',19,'bold'),
                         offvalue=0, onvalue=1,
                         variable=variables_bebida[counter_bebida],
                         command=revisar_check)
    bebida.grid(row=counter_bebida,column=1, sticky=W)
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[counter_bebida] = StringVar()
    texto_bebida[counter_bebida].set('0')
    cuadros_bebida[counter_bebida] = Entry(panel_bebidas,
                                    font='Dosis',
                                    bd=1,
                                    width=4,
                                    state=DISABLED,
                                    textvariable=texto_bebida[counter_bebida])
    cuadros_bebida[counter_bebida].grid(row=counter_bebida,column=2)
    counter_bebida+=1

for postre in postres_list:
    variables_postres.append('')
    variables_postres[counter_postres] = IntVar()
    postre = Checkbutton(panel_postres, text= postre.title(),font=('Dosis',19,'bold'),
                         offvalue=0, onvalue=1,
                         variable=variables_postres[counter_postres],
                         command=revisar_check)
    postre.grid(row=counter_postres,column=1, sticky=W)
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[counter_postres] = StringVar()
    texto_postre[counter_postres].set('0')
    cuadros_postre[counter_postres] = Entry(panel_postres,
                                    font='Dosis',
                                    bd=1,
                                    width=4,
                                    state=DISABLED,
                                    textvariable=texto_postre[counter_postres])
    cuadros_postre[counter_postres].grid(row=counter_postres,column=2) 
    counter_postres+=1          
#etiqueta de costo y campos de entrada
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_costo_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


etiqueta_costo_comida = Label(panel_costos, text="Costo comida",
                            bg='azure4',
                            font=('Dosis',12),
                            foreground='white')
etiqueta_costo_comida.grid(row=0,column=0)
texto_costo_comida = Entry(panel_costos,
                        bg='azure4',
                        width=10,
                        font=('Dosis'),
                        state='readonly',
                        textvariable=var_costo_comida)
                        
texto_costo_comida.grid(row=0, column=1,padx=41)

etiqueta_costo_bebida = Label(panel_costos, text="Costo bebidas",
                            bg='azure4',
                            font=('Dosis',12),
                            foreground='white')
etiqueta_costo_bebida.grid(row=1,column=0)
texto_costo_bebida = Entry(panel_costos,
                        bg='azure4',
                        width=10,
                        font=('Dosis'),
                        state='readonly',
                        textvariable=var_costo_bebida,
                        )
                        
texto_costo_bebida.grid(row=1, column=1,padx=41)

etiqueta_costo_postre = Label(panel_costos, text="Costo postre",
                            bg='azure4',
                            font=('Dosis',12),
                            foreground='white')
etiqueta_costo_postre.grid(row=2,column=0)
texto_costo_postre = Entry(panel_costos,
                        bg='azure4',
                        width=10,
                        font=('Dosis'),
                        state='readonly',
                        textvariable=var_costo_postre)
                        
texto_costo_postre.grid(row=2, column=1,padx=41)

etiqueta_costo_subtotal = Label(panel_costos, text="Subtotal",
                            bg='azure4',
                            font=('Dosis',12),
                            foreground='white')
etiqueta_costo_subtotal.grid(row=0,column=2)
texto_costo_subtotal = Entry(panel_costos,
                        bg='azure4',
                        width=10,
                        font=('Dosis'),
                        state='readonly',
                        textvariable=var_costo_subtotal)
                        
texto_costo_subtotal.grid(row=0, column=3)

etiqueta_impuesto = Label(panel_costos, text="Impuestos",
                            bg='azure4',
                            font=('Dosis',12),
                            foreground='white')
etiqueta_impuesto.grid(row=1,column=2)
texto_impuesto= Entry(panel_costos,
                        bg='azure4',
                        width=10,
                        font=('Dosis'),
                        state='readonly',
                        textvariable=var_impuesto)
                        
texto_impuesto.grid(row=1, column=3,padx=41)

etiqueta_costo_total = Label(panel_costos, text="Total",
                            bg='azure4',
                            font=('Dosis',12),
                            foreground='white')
etiqueta_costo_total.grid(row=2,column=2,padx=41)
texto_costo_total = Entry(panel_costos,
                        bg='azure4',
                        width=10,
                        font=('Dosis'),
                        state='readonly',
                        textvariable=var_total)
                        
texto_costo_total.grid(row=2, column=3,padx=41)

#action buttons
botones = ['total','recibo','guardar','resetear']
botones_creados = []
columnas = 0
for buton in botones:
    boton = Button(panel_botones,
                text=buton.title(),
                font=('Dosis',14,'bold'),
                foreground='white',
                bg='azure4',
                bd=1,
                width=9)
    boton.grid(row=0,column=columnas)
    botones_creados.append(boton)
    columnas+=1

botones_creados[0].config(command= lambda:calcular_totales())
botones_creados[1].config(command= lambda:generar_recibo())
botones_creados[2].config(command= lambda:guardar())
botones_creados[3].config(command= lambda:reset())



#area de recibo
texto_recibo = Text(panel_RECIBO,
                    font=('Dosis',12,'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,column=0)

#calculadora

visor_calculadora = Entry(panel_calculadora, font=('Dosis',16),width=33, bd=1)
visor_calculadora.grid(row=0,column=0,columnspan = 4)

buttons_calculadora = ['7','8','9','+',
                        '4','5','6','-',
                        '1','2','3','x',
                        '=','Borrar','0','/']

botones_guardados = []                        
position_boton_calc_row = 1
position_boton_calc_col = 0

for boton_calc in buttons_calculadora:
    boton = Button(panel_calculadora,
                text=boton_calc.title(),
                font=('Dosis',14,'bold'),
                foreground='white',
                bg='azure4',
                bd=1,
                width=9)
    botones_guardados.append(boton)
    if(position_boton_calc_col == 4):
        position_boton_calc_row += 1
        position_boton_calc_col = 0
    
    position_boton_calc_col+=1
    boton.grid(row=position_boton_calc_row,column=position_boton_calc_col)
    

botones_guardados[0].config(command= lambda:click_boton('7'))
botones_guardados[1].config(command= lambda:click_boton('8'))
botones_guardados[2].config(command= lambda:click_boton('9'))
botones_guardados[3].config(command= lambda:click_boton('+'))
botones_guardados[4].config(command= lambda:click_boton('4'))
botones_guardados[5].config(command= lambda:click_boton('5'))
botones_guardados[6].config(command= lambda:click_boton('6'))
botones_guardados[7].config(command= lambda:click_boton('-'))
botones_guardados[8].config(command= lambda:click_boton('1'))
botones_guardados[9].config(command= lambda:click_boton('2'))
botones_guardados[10].config(command= lambda:click_boton('3'))
botones_guardados[11].config(command= lambda:click_boton('*'))
botones_guardados[12].config(command= lambda:obtener_resultado())

botones_guardados[13].config(command= lambda:borrar())

botones_guardados[14].config(command= lambda:click_boton('0'))
botones_guardados[15].config(command= lambda:click_boton('/'))





#avoid window closure
application.mainloop()