import cv2 #Opencv
import mediapipe as mp #Google
import time
import matplotlib.pyplot as plt

from Captura import Captura
from MallaFacial import MallaFacial
from AnalisisFacial import AnalisisFacial


fuente = cv2.FONT_ITALIC
def main():
    #tipoEntrada=input("Entrada video:")
    tipoEntrada="webcam"
    objetoCaptura=Captura(tipoEntrada)
    captura=objetoCaptura.getCaptura()
    objetoMallaFacial=MallaFacial()
    mediapMallaFacial,mallaFacial=objetoMallaFacial.getMallaFacial()
    mediapDibujoPuntos,dibujoPuntos=objetoMallaFacial.getPuntosMallaFacial()   
    analisisVideo(captura,mediapDibujoPuntos,dibujoPuntos,mediapMallaFacial,mallaFacial) 
    
def analisisVideo(captura,mediapDibujoPuntos,dibujoPuntos,mediapMallaFacial,mallaFacial):
    global mensaje,hilo
    vectorEstado=[]
    verMalla=False
    rotacion=0

    anteriorTiempoFrame = 0
    capturaTiempoFrame = 0
    while True:
        #Lectura de frame y el estado (En Python puedo asignar datos a variables de la siguiente forma var1,var2=1,2) 
        estado,frame=captura.read()
        #Efecto espejo
        frame=cv2.flip(frame,rotacion)
        #Procesa el fotograma para entreganos la malla facial
        resultados=mallaFacial.process(frame)
        listaPuntosFaciales=[]
        capturaTiempoFrame = time.time()
 
        #Si encuentra un rostro        
        if resultados.multi_face_landmarks:
            #Para todos los rostros detectados
            for rostros in resultados.multi_face_landmarks:
                #Dibujamos las conecciones de la malla
                if verMalla:
                    mediapDibujoPuntos.draw_landmarks(frame,rostros,mediapMallaFacial.FACEMESH_CONTOURS,dibujoPuntos,dibujoPuntos)
                #Puntos rostro detectado
                for puntoID,puntos in enumerate (rostros.landmark):
                    #Alto y ancho de la ventana
                    altoVentana, anchoVentana,variable=frame.shape
                    posx=int(puntos.x*anchoVentana)
                    posy=int(puntos.y*altoVentana)
                    #print(f"alto{altoVentana} ancho {anchoVentana}")
                    #Apilamos los puntos faciales en una lista con sus coordenadas
                    listaPuntosFaciales.append([puntoID,posx,posy])
                    if len(listaPuntosFaciales)==468:
                        
                        objetoAnalisisFacial=AnalisisFacial(listaPuntosFaciales)
                        mensaje=str(objetoAnalisisFacial.getLongitudes())
                        if mensaje=='yes':
                            cv2.putText(frame, text='Abre los ojos!', org=(0, 30), fontFace=fuente,
                            fontScale=1, color=(0, 0, 255), thickness=2, lineType=cv2.LINE_8)
                        else:
                            cv2.putText(frame, text='Ojos abiertos', org=(0, 30), fontFace=fuente,
                            fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_8)                       
                        mostrarEjesRotacion(listaPuntosFaciales,frame,altoVentana)
                        vectorEstado.append(str(objetoAnalisisFacial.getLongitudes()).replace("emocion_","").replace("yes","cerrado").replace("no","abierto"))  
                         
        fps = 1/(capturaTiempoFrame-anteriorTiempoFrame)
        anteriorTiempoFrame = capturaTiempoFrame
        fps = str(int(fps))
        cv2.putText(frame, text='FPS:'+fps, org=(500, 30), fontFace=fuente,
                            fontScale=1, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_8)                  
        cv2.imshow("Analisis Facial Python",frame)
        tecla = cv2.waitKey(1) & 0xFF
        if tecla==ord('e'):
            if rotacion==1:
                rotacion=rotacion-1
            elif rotacion==-1:  
                rotacion=rotacion+1
            else:
                rotacion=rotacion+1
        if tecla==ord('q'):
            verMalla=True
        elif tecla==ord('w'):  
            verMalla=False
        #Codigo Ascii ESC es 27 para cerrar frame
        elif tecla==27:
            hilo=True
            break
    #Destruimos cada ventana creada por opencv 
    cv2.destroyAllWindows() 
    analizarDatos(vectorEstado)


def analizarDatos(vectorEstado):
    plt.plot(vectorEstado)
    plt.title('ANALISIS')
    plt.xlabel('TIEMPO')
    plt.ylabel('OJO')
    plt.show()

def mostrarEjesRotacion(listaPuntosFaciales,frame,altoVentana):
    coordenadaCentralX,coordenadaCentralY=listaPuntosFaciales[9][1:]
    coordenadaQuijadaX,coordenadaQuijadaY=listaPuntosFaciales[152][1:]
    cv2.line(frame,pt1=(coordenadaCentralX,coordenadaCentralY),pt2=(coordenadaCentralX,altoVentana),color=(0,0,255))
    cv2.line(frame,pt1=(coordenadaCentralX,coordenadaCentralY),pt2=(coordenadaQuijadaX,coordenadaQuijadaY),color=(0,0,255))

#Buena practica de programacion en python (Python ejecuta todos los modulos cargados en orden descendente y declara variables internas __name__ se le declara como main al modulo que se encarga de "correr", al trabajar con esta condicional )
if __name__ == "__main__":
    main()
