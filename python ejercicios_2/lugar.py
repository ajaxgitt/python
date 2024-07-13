import osmnx as ox
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

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

for i in enlaces[:1]:
    print(f'origen: {i[0]}, destino:{i[1]}, peso = {i[2]['length']}')




fig, ax = ox.plot_graph(G_recortado, 
                        figsize=(10, 10), 
                        bgcolor='w', 
                        node_color='lightblue',  
                        node_size=30, 
                        node_alpha=0.8, 
                        edge_color='gray', 
                        edge_linewidth=1.5)
plt.show()

