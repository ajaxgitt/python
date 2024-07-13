

class GrafoDirigido:
    def __init__(self) -> None:
        self.diccionario_grafo = {}
        
    def insertar(self, dato):
        if dato in self.diccionario_grafo:
            return 'el vértice ya existe en el grafo'
        self.diccionario_grafo[dato]=[]
        
    def agregar_enlace(self, enlace):
        origen = enlace.obtener_origen()
        destino = enlace.obtener_destino()
        if origen not in self.diccionario_grafo:
            raise ValueError(f'El nodo {origen} no existe en el grafo')
        if destino not in self.diccionario_grafo:
            raise ValueError(f'El nodo {destino} no existe en el grafo')
        
        self.diccionario_grafo[origen].append(destino)
        
    def esta_el_nodo_en(self, nodo):
        return nodo in self.diccionario_grafo
        
    def obtener_nodo(self, nombre_nodo):
        for i in self.diccionario_grafo:
            if nombre_nodo == i.obtener_nombre():
                return i
        print('El nodo no existe')
        
        
    def obtener_nodos_conectados(self,nodo):
        return self.diccionario_grafo[nodo]
    
    def __str__(self) -> str:
        enlaces = ''
        for i in self.diccionario_grafo:
            for j in self.diccionario_grafo[i]:
                enlaces += i.obtener_nombre()+' -----> '+ j.obtener_nombre()+ '\n'
        return enlaces
    


class Enlace:
    def __init__(self,origen,destino) -> None:
        self.origen = origen
        self.destino = destino
    
    def obtener_origen(self):
        return self.origen
    
    def obtener_destino(self):
        return self.destino
    
    def __str__(self) -> str:
        return self.origen.obtener_nombre()+' ----> '+self.destino.obtener_nombre()
    
    
class Nodo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        
    def obtener_nombre(self):
        return self.nombre
    
    def __str__(self) -> str:
        return self.nombre
    
class GrafoNoDirigido(GrafoDirigido):
    
    def agregar_enlace(self, enlace):
        GrafoDirigido.agregar_enlace(self, enlace)
        enlace_inverso = Enlace(enlace.obtener_origen(),enlace.obtener_destino())
        GrafoDirigido.agregar_enlace(self, enlace_inverso)

def construir_grafo(grafo):
    g = grafo()
    for i in ('s','a','b','c','d','e','f','g','h','i','j','k'):
        g.insertar(Nodo(i))
    
    g.agregar_enlace(Enlace(g.obtener_nodo('s'),g.obtener_nodo('a')))
    return g

G1 = construir_grafo(GrafoDirigido)
print(G1)