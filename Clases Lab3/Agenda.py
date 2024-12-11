from Clases.Usuario import *

class Agenda():
    def __init__(self, registro, no_reg):
        self.__registro = []
        self.__no_reg = 0
        
    def buscar(id): #Método buscar, recibe como parametros el id del usuario
        id_buscado = id #Variable que almacena el id que queremos comparar
        for ids in range(__no_reg): #Ciclo que recorre el arreglo hasta los objetos que hayamos decidido meter en el
            if __registro[ids].id == id_buscado: #Comparamos cada id de los objetos con el id presentado
                return ids #Si la comparación es verdadera entonces retornamos el indice de dicho objeto
        else: #En caso de no haberse encontrado comparación similar
            return -1 #Retornamos menos uno

    def agregar(Usuario u):
        if buscar(u.getId()) != -1: #Tomamos el id del usuario y se lo pasamos al método buscar, si este obtiene un valor diferente de menos 1 retornara False
            return False #Retorna False pues el objeto ya pertenece al arreglo
        else:
            __registro.append(u) #Si el valor retornado fue menos uno, entonces se agrega el nuevo objeto al arreglo
            __no_reg += 1 #Aumenta el tamaño del arreglo
            return True #Retorna True porque el nuevo objeto fue agregado con exito
    
    def eliminar(id): #Método que elimina objetos
        if buscar(id) == -1: #Usando el método buscar se fija si el objeto esta en el arreglo, si no esta retorna Falso
            return False #Retorna Falso porque no se encontraba el objeto
        else: #En caso de que el objeto este
            indice_eliminado = buscar(id)
            for i in range(indice_eliminado, __no_reg-2): #Se empieza a iterar desde el indice del objeto eliminado
                __registro[i] = __registro[i+1] #Se mueven los objetos hacia la ¿izquierda?
            __registro[no_reg-1] = None #El ultimo valor del arreglo ya no esta pues todo fue ocupado por los demas valores
            __no_reg -= 1 #Disminuimos el tamaño del arreglo
            return True #Devolvemos Verdadero tras haberse completado todo el proceso
        
    def toFile(Usuario u):
        fichero = open("agenda.txt", "w")
        for i in range(Agenda.__no_reg):
            Agenda.__registro[i]
            
                

    
