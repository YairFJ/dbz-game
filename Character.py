class Character:
    def __init__(self, nombre, fuerza, velocidad, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__velocidad = velocidad
        self.__vida = vida

    @property          #Property es un decorador que nos permite llamar a un método como atributo
    def nombre(self):
        return self.__nombre


    @nombre.setter      # Este seria un setter(para modificar el atributo)
    def nombre(self, new_value):        #Las propiedades están puestas privadas sólo para modo de práctica
        self.__nombre = new_value

    
    @property
    def fuerza(self):
        return self.__fuerza


    @fuerza.setter
    def fuerza(self, new_value):
        self.__fuerza = new_value


    @property
    def velocidad(self):
        return self.__velocidad


    @velocidad.setter
    def velocidad(self, new_value):
        self.__velocidad = new_value


    @property       
    def vida(self):
        return self.__vida


    @vida.setter
    def vida(self, new_value):
        self.__vida = new_value
       

    def __repr__(self):  # Método especial que nos da una representació del objeto como String
        return f"Nombre: {self.nombre}, Fuerza: {self.fuerza}, Velocidad: {self.velocidad}, Vida: {self.vida}"

    
    def __add__(self, otro):    # Método especial que nos indica que hacer al sumar dos objetos de esta clase.
        new_f = round(((self.fuerza + otro.fuerza)/2)**2)
        new_v = round(((self.velocidad + otro.velocidad)/2)**2)
        new_h = round(((self.vida + otro.vida)/2)**2)
        return Character(self.nombre +'-'+ otro.nombre, new_f, new_v, new_h)


