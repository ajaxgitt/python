

import networkx as nx  # Importar la librería NetworkX con el alias nx
import matplotlib.pyplot as plt  # Importar matplotlib para visualización

# Crear un grafo vacío utilizando nx.Graph()
g = nx.Graph()

# Añadir un nodo al grafo con identificador 1
g.add_node(1)

# Añadir varios nodos al grafo utilizando una lista
g.add_nodes_from([2, 3])

# Añadir una arista (edge) entre los nodos 1 y 2
g.add_edge(1, 2)

# Añadir múltiples aristas al grafo utilizando una lista de tuplas
g.add_edges_from([(1, 3), (2, 3)])

# Imprimir los nodos del grafo
print("Nodos del grafo:", g.nodes())

# Imprimir las aristas del grafo
print("Aristas del grafo:", g.edges())

# Dibujar el grafo utilizando nx.draw()
# with_labels=True muestra etiquetas en los nodos
# node_color establece el color de los nodos en 'lightblue'
# edge_color establece el color de las aristas en 'grey'
nx.draw(g, with_labels=True, node_color='lightblue', edge_color='grey')

# Mostrar el gráfico utilizando plt.show() de matplotlib
plt.show()
