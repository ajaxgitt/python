import matplotlib.pyplot as plt
import osmnx as ox
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import osmnx as ox
from shapely.geometry import Polygon
import networkx as nx


class Nodo:
    def __init__(self, id , atributos=None) -> None:
        self.id = id
        self.atributos = atributos if atributos is not None else {}
        
    def obtener_latitud(self):
        return self.atributos['y']
    
    def obtener_longitud(self):
        return self.atributos['x']
        

    def __repr__(self) -> str:
        return f'Nodo: ({self.id}, {self.atributos})'
    

class Enlace:
    def __init__(self, origen, destino, peso=1) -> None:
        self.origen = origen
        self.destino = destino
        self.peso = peso
        
    def __repr__(self) -> str:
        return f'Enlace origen:({self.origen.id} -> {self.destino.id},peso={self.peso}) '
        


class GrafoDirigido:
    
    def __init__(self) -> None:
        self.nodos = {}
        self.enlaces = []
        
    #11209278543

        
        
        
    def _verificar_coordenadas(self,y,x):
        for id , nodo in self.nodos.items():
            if nodo.obtener_latitud() == y and nodo.obtener_longitud()==x:
                return id
    
    def buscar_ruta_mas_corta(self, origen_latitud, origen_longitud,destino_latitud,destino_longitud):
        
        id_origen = self._verificar_coordenadas(origen_latitud,origen_longitud)
        id_destino = self._verificar_coordenadas(destino_latitud,destino_longitud)
        
        if (id_origen is not None and id_destino is not None)and(id_origen != id_destino):
            print('funciono')
            print(f'origen: {id_origen}')
            print(f'destino: {id_destino}')
            
        else:
            if id_origen is None or id_destino is None:
                print('Error: Una o ambas coordenadas no corresponden a nodos validos.')
            elif id_origen == id_destino:
                print('Error: Las coordenadas de origen y destino son iguales.')
            else:
                print('Error desconocido: No se pudo encontrar una ruta valida.')
        
            
            
        
        
    def obtener_numero_nodos(self):
        print(f'{len(self.nodos.keys())} nodos')
        return 
        
    def obtener_numero_enlaces(self):
        print(f'{len(self.enlaces)} enlaces')
        return
    
    def agregar_nodo(self, nodo):
        if nodo.id not in  self.nodos:
            self.nodos[nodo.id]= nodo
        else:
            print(f'El nodo con el id {nodo.id} ya existe en el grafo.!')
    
    def conectar_nodos(self, id_origen,id_destino, peso=1):
        if id_origen in self.nodos and id_destino in self.nodos:
            origen = self.nodos[id_origen]
            destino = self.nodos[id_destino]
            enlace = Enlace(origen,destino, peso)
            self.enlaces.append(enlace)
        else:
            print(f"Error: No se pueden conectar los nodos {id_origen} y {id_destino}. Al menos uno no existe.")
            
    def imprimir_enlaces(self):
        for i in self.enlaces:
            print(f'origen:{i.origen.id}-> destino {i.destino.id}' )
            
    def imprimir_nodos(self):
        for _, valor in self.nodos.items():
            print(f'{valor}')
    
    
    def dibujar_grafo(self, coordenadas):
        polygon = Polygon(coordenadas)
        G_recortado = ox.graph_from_polygon(polygon, network_type='drive')
        ox.plot_graph(G_recortado, 
                                figsize=(10, 10), 
                                bgcolor='w', 
                                node_color='lightblue',  
                                node_size=30, 
                                node_alpha=0.8, 
                                edge_color='gray', 
                                edge_linewidth=1.5)
        plt.show()
        
        
    
