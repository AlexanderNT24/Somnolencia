class Conexion:

    objetoArchivo=None
    datos=None

    def __init__(self,datos=None):
        self.datos=datos

    def enviarDatos(self):
        try:
           objetoArchivo=open(".\Datos\DatosLongitudes.txt", "w")
           objetoArchivo.write(self.datos)
           objetoArchivo.close()
        except:
            print("Error")



