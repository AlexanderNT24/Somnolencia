# Detector de somnolencia Usando MediaPipe y Arduino.
El proyecto se basa en un detector de somnolencia controlado con inteligencia artificial y gestionado en arduino, esto con la ayuda de la librería mediapipe, la cual reconoce y brinda puntos especiales en un rostro.
Nuestro proyecto crea una comunicación entre python y arduino, con la finalidad de que si python detecta que los ojos del usario se cierran, este se lo comunicará a arduino que a su vez iniciará un protocolo, como encender focos led y una alarma.
## Sobre El Proyecto
Para el desarrollo de nuestro proyecto usamos una placa Arduino UNO, el IDE de Arduino y Visual Studio Code para la programación del detector de somnolencia.
### El proyecto hace uso de las siguentes tecnologías.
#### Para Arduino UNO:
```
C++
```
#### Para el detector de somnolencia:
```
Python 
Mediapipe
OpenCV
```
#### Para la comunicación entre Python y Arduino:
```
Threading
Pyserial
```
### Uso
https://user-images.githubusercontent.com/89727568/151181256-ad33e71b-ce66-44e1-a59a-3f42e1a2ef1b.mp4

