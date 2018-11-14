from paquete_academico.modelado import *

est1 = EstDistancia()    					# Instanciamos el objecto est1
p = Pais("Ecuador", "Quito")				# Instanciamos un objeto p de la clase Pais

# Agregamos algunos atributos
est1.agregar_nombre("Jose")					
est1.agregar_apellido("Diaz")
est1.agregar_codigo("11012")
est1.agregar_num_materias(5)
est1.agregar_modulo("Noveno")

est1.agregar_pais(p)						# Agregamos el objeto "p" como atributos del objeto "est1"

print(est1.presentar_informacion())			# Presentamos los datos

