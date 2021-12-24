class Vehiculo():
  def __init__(self,color,marca,velocidad_maxima) :
      self.color= color
      self.marca= marca
      self.velocidad_maxima= velocidad_maxima
      self.velocidad_actual= 0
      self.encendido= False
  def encender_vehiculo(self):
      self.encendido= True
      print("vehiculo encendido")
  def apagar_vehiculo(self):
      self.encendido= False
      print("vehiculo apagado")
  def mostrar_velocimetro(self):
        print ("La velocidad actual es "+ str(self.velocidad_actual)+ " de "+ str(self.velocidad_maxima))

  
  def acelerar(self,velocidad):
      if (self.encendido== True):
        if self.velocidad_actual+velocidad > self.velocidad_maxima:
            self.velocidad_actual= self.velocidad_maxima
        else:
            self.velocidad_actual= self.velocidad_actual+velocidad
      else:
          print("Para acelerar primero encender vehiculo")
      self.mostrar_velocimetro()

  def frenar(self, velocidad):
      if self.velocidad_actual-velocidad < 0:
         self.velocidad_actual= 0
         self.mostrar_velocimetro()
      else:
         self.velocidad_actual= self.velocidad_actual-velocidad
         self.mostrar_velocimetro()

class Automovil(Vehiculo):
    def __init__(self,puertas,color,marca,velocidad_maxima):
        self.puertas=puertas
        Vehiculo.__init__(self,color,marca,velocidad_maxima)
    def abrir_puertas(self,nro_puertas):
        print("Se abren las puertas")
   

class Camion(Vehiculo):
    def __init__(self,carga_maxima,color, marca, velocidad_maxima):
        self.carga_maxima=carga_maxima
        self.carga_actual=0
        Vehiculo.__init__(self,color, marca, velocidad_maxima)
    def cargar(self,cantidad):
        self.carga_actual= self.carga_actual+cantidad
    def mostrar_velocimetro(self):
      print ("La velocidad actual es "+ str(self.velocidad_actual)+ " de "+ str(self.velocidad_maxima)+ " y la carga actual es de "+ str(self.carga_actual))



mi_auto= Automovil(4,"Azul","Fiat",180,)
print(mi_auto.color)
print(mi_auto.marca)
mi_auto.abrir_puertas(5)
mi_auto.encender_vehiculo()
mi_auto.acelerar(150)
mi_auto.acelerar(20)
mi_auto.frenar(160)
mi_auto.apagar_vehiculo()

mi_camion= Camion(300,"rojo","Skania",150)
print(mi_camion.marca)
print(mi_camion.color)
mi_camion.encender_vehiculo()
mi_camion.cargar(100)
mi_camion.acelerar(100)
mi_camion.acelerar(60)
mi_camion.frenar(120)
mi_camion.apagar_vehiculo()












