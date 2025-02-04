
from cv2 import cv2
import face_recognition as fr

#cargar imagenes
foto_control = fr.load_image_file('FOTOBASE.jpg')
foto_prueba = fr.load_image_file('FotoB.jpg')
#Pasar imagenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

#mostrar imagenes
cv2.imshow('foto', foto_control)
