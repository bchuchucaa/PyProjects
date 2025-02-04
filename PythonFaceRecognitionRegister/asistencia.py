from cv2 import cv2, imshow
import face_recognition as fr
import os
import  numpy
from datetime import datetime

#CREAR BASE DE DATOS
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []

lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}\\{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

#CODIFICAR IMAGENES
def codificar(imagenes):
    #CREAR UNA LISTA NUEVA
    lista_codificada = []
    #PASAR TODAS LAS IMAGENES A RGB
    for image in imagenes:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        #CODIFICAR
        codificado = fr.face_encodings(image)[0]
        #AGREGAR A LA LISTA
        lista_codificada.append(codificado)
    return lista_codificada

#REGISTRAR INGRESOS
def registrar_ingresos(persona):
    file = open('registro.csv','r+')
    lista_datos = file.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append((ingreso[0]))

        if persona not in nombres_registro:
            ahora = datetime.now()
            string_ahora = ahora.strftime('%H:%M:%S')
            file.writelines(f'\n{persona},{string_ahora}')

lista_empleados_codificada = codificar(mis_imagenes)

#TOMAR UNA IMAGEN DE CAMARA WEB
captura = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#LEER LA IMAGEN DE LA CAMARA
exito, imagen = captura.read()

if not exito:
    print("NO SE A PODIDO TOMAR LA CAPTURA")
else:
    #RECONOCER CARA EN CAPTURA
    cara_captura = fr.face_locations(imagen)
    # imshow("foto prueba",cara_captura)

    #CODIFICAR CARA CAPTURADA
    cara_captura_codificada = fr.face_encodings(imagen,cara_captura)
    #BUSCAR COINCIDENCIAS

    for caracodif, caraubic in zip(cara_captura_codificada,cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada,caracodif)
        distancias = fr.face_distance(lista_empleados_codificada,caracodif)

        print(distancias)
        indice_coincidencia = numpy.argmin(distancias)

        #MOSTRAR COINCIDENCIAS SI EXISTEN
        if distancias[indice_coincidencia] > 0.65:
            print("NO SE ENCONTRARON COINCIDENCIAS")
        else:
            #BUSCAR EL NOMBRE DEL EMPLEADO
            nombre = nombres_empleados[indice_coincidencia]
            y1,x2,y2,x1 = caraubic
            #RESALATAR ROSTRO
            cv2.rectangle(imagen,(x1,y1),(x2,y2), (255, 255,0),2)
            cv2.rectangle(imagen,(x1,y2-35),(x2,y2),cv2.FILLED)
            cv2.putText(imagen,nombre,(x1+6,y2-13),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
            registrar_ingresos(nombre)
            #MOSTRAR LA IMAGEN OBTENIDA
            cv2.imshow('Imagen web',imagen)

            #MANTENER VENTANA ABIERTA
            cv2.waitKey(0)

