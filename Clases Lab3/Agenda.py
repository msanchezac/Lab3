from Clases.Usuario import *

class Agenda():
    def __init__(self, registro, no_reg):
        self.__registro = []
        self.__no_reg = 0

def agregar(Usuario u):
        if buscar(u.getId()) != -1:
            return False
        else:
            __registro.append(u)
            no_reg += 1
            return True

    def buscar(id): #Método buscar, recibe como parametros el id del usuario
        id_buscado = id #Variable que almacena el id que queremos comparar
        for ids in range(no_reg): #Ciclo que recorre el arreglo hasta los objetos que hayamos decidido meter en el
            if __registro[ids].id == id_buscado: #Comparamos cada id de los objetos con el id presentado
                return ids #Si la comparación es verdadera entonces retornamos el indice de dicho objeto
        else: #En caso de no haberse encontrado comparación similar
            return -1 #Retornamos menos uno