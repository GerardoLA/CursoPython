# 1. Introducción a las Clases en Python
# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase.
# Nos permiten agrupar datos (atributos o propiedades) y funciones (metodos) en un solo lugar.

# Ejemplo básico de una clase
class Coche:
# atributo de clase(comparte todas las instancias)
    tipo = "vehiculo de cuatro ruedas"
# Método especial que es el que construye el objeto
# Se llama automáticamente este método cuando creas la instancia

    def __init__(self, marca, modelo, color):
        #atributos de la instancia
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} ha arrancado!")

mi_coche = Coche("volskwagen", "Golf", "rojo" )
mi_coche.arrancar()
print(mi_coche.tipo)

coche_de_Igor =Coche("Seat", "Ronda", "Rosa")
coche_de_Igor.arrancar()
print(coche_de_Igor.modelo)

# Encapsulación: es ocultar los detalles internos de una clase y exponer solo la interfaz pública

# Crear una clase para llamar a la IA  de OpenAI, Deepseek o lo que sea https://www.twitch.tv/videos/2397854000?filter=archives&sort=time

