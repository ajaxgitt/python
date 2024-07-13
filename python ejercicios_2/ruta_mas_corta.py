import libreria.grafo as gr
import osmnx as ox
from shapely.geometry import Polygon
import networkx as nx

coordenadas = [
    (-63.181817,-17.766709),
    (-63.162407,-17.780224),
    (-63.172425,-17.799699),
    (-63.196322,-17.793340),
    (-63.197992,-17.778833)
]





polygon = Polygon(coordenadas)
G_recortado = ox.graph_from_polygon(polygon, network_type='drive')
nodos = G_recortado.nodes(data=True)
enlaces = list(G_recortado.edges(data=True))


Grafo = gr.GrafoDirigido()

for i in nodos:
    mi_nodo = gr.Nodo(i[0],i[1])
    Grafo.agregar_nodo(mi_nodo)
    
for i in enlaces:
    Grafo.conectar_nodos(i[0],i[1],round(i[2]['length'],2))
    



Grafo.dibujar_grafo(coordenadas)


Grafo.imprimir_nodos()



