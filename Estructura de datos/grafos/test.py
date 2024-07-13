import osmnx as ox
from shapely.geometry import Polygon
import grafos.graph as gr




grafo = gr.Grafo()

coordenadas = [
    (-63.181817, -17.766709),
    (-63.162407, -17.780224),
    (-63.172425, -17.799699),
    (-63.196322, -17.793340),
    (-63.197992, -17.778833)
]


polygon = Polygon(coordenadas)
G_recortado = ox.graph_from_polygon(polygon, network_type='drive')
nodos = G_recortado.nodes(data=True)
enlaces = list(G_recortado.edges(data=True))

for i in nodos:
    mi_nodo = gr.Nodo(i[0], i[1])
    grafo.insertar_nodo(mi_nodo)

for i in enlaces:
    grafo.conectar_nodos(i[0], i[1], round(i[2]['length'], 2))

grafo.buscar_ruta_mas_corta(-17.7884664, -63.1878028,-17.7705527, -63.1789193)

