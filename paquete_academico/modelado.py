# Creamos la clase padre
class Persona(object):

    # Constructor
    def __init__(self):
        super(Persona, self).__init__()

    # Métodos set
    def agregar_nombre(self, nombre):
        self.nombre = nombre

    def agregar_apellido(self, apellido):
        self.apellido = apellido

    def agregar_pais(self, pais):
        self.pais = pais

    # Métodos get
    def obtener_nombre(self):
        return self.nombre

    def obtener_apellido(self):
        return self.apellido

    def obtener_pais(self):
        return self.pais


# Clase hija en primer orden
class Estudiante(Persona):

    # Constructor
    def __init__(self):
        super(Estudiante, self).__init__()

    # Método set
    def agregar_codigo(self, codigo):
        self.codigo = codigo

    # Método get
    def obtener_codigo(self):
        return self.codigo


# Clase hija en segundo orden
class EstPresencial(Estudiante):

    # Constructor
    def __init__(self):
        super(EstPresencial, self).__init__()
      
    # Métodos set
    def agregar_num_creditos(self, m):
        self.num_creditos = m

    def agregar_ciclo(self, ciclo):
        self.ciclo = ciclo.upper()

    def obtener_num_creditos(self):
        return self.num_creditos

    def obtener_ciclo(self):
        return self.ciclo

    def presentar_informacion(self):
        cadena = ("\nInformacion:\n\tNombres Completos: %s %s\n\tCodigo: %s\n\tProcedencia: pais-%s capital-%s\n\tCiclo: %s\n\tNúmero Créditos: %s\n"%(self.obtener_nombre(), self.obtener_apellido(), self.obtener_codigo(), self.obtener_pais().obtener_nombre_pais(), self.obtener_pais().obtener_capital(), self.obtener_ciclo(), self.obtener_num_creditos()                 ))
        return cadena


# Clase hija en segundo orden
class EstDistancia(Estudiante):

    # Constructor
    def __init__(self):
        super(EstDistancia, self).__init__()

    # Métodos set
    def agregar_num_materias(self, m):
        self.num_materias = m

    def agregar_modulo(self, modulo):
        self.modulo = modulo.upper()

    def obtener_num_materias(self):
        return self.num_materias

    def obtener_modulo(self):
        return self.modulo

    def presentar_informacion(self):
        cadena = ("\nInformacion:\n\tNombres Completos: %s %s\n\tCodigo: %s\n\tProcedencia: pais-%s capital-%s\n\tModulo: %s\n\tNúmero de Materias: %s\n"%(self.obtener_nombre(), self.obtener_apellido(), self.obtener_codigo(), self.obtener_pais().obtener_nombre_pais(), self.obtener_pais().obtener_capital(), self.obtener_modulo(), self.obtener_num_materias()))
        return cadena

      
# Clase Pais
class Pais(object):

    # Constructor
    def __init__(self, nombre, capital):
        self.nombre = nombre
        self.capital = capital

    # Métodos set
    def agregar_nombre_pais(self,nombre):
        self.nombre=nombre

    def agregar_capital(self,capital):
        self.capital=capital

    # Métodos get
    def obtener_nombre_pais(self):
        return  self.nombre

    def obtener_capital(self):
        return  self.capital
