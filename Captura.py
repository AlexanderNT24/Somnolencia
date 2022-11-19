import cv2 #Opencv

class Captura:

    tipoEntrada=""
    captura=None
    tipo="mp4"
    url=""

    def __init__(self,tipoEntrada,url="https://www.youtube.com/watch?v=j6eGHROLKP8&t=17s&ab_channel=RingaTech"):   
        self.tipoEntrada=tipoEntrada
        self.url=url

    def getCaptura(self):
        if self.tipoEntrada=="webcam":        
            #Capturo el streaming de la webcam de el puerto de la webcam (0 para la nativa y 1,2.. para externas)
            self.captura=cv2.VideoCapture('rtsp://192.168.1.40:5540/ch0')
        else:
            print("NO VALIDA")
            self.captura = None
        return self.captura    

