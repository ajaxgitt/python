Dibujar Grafos

#Grafico aleatorio
        # nx.draw(grafico, with_labels=True, node_color='skyblue', node_size=1500, edge_color='green', arrows=True)
        # plt.show()
        
        #grafico Circular
        # pos = nx.circular_layout(grafico)
        # nx.draw(grafico,pos,with_labels=True, node_color='skyblue',node_size=1500,edge_color='gray')
        # plt.show()
        
        G = grafico
        # Layout Spring
        
        # En este diseño, los nodos estan dispuestos utilizando un algoritmo 
        # de resorte, lo que coloca nodos conectados ms cerca uno del otro y nodos no conectados mas lejos.
        # pos = nx.spring_layout(G)
        # nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
        # plt.title('Grafo Spring')
        # plt.show()

        # Layout Spectral
        #Este diseño utiliza la descomposición espectral del grafo para colocar los nodos. 
        # Es útil para visualizar patrones y estructuras en el grafo
        
        #pos = nx.spectral_layout(G)
        #nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
        #plt.title('Grafo Spectral')
        #plt.show()
        
        # Layout Kamada-Kawai
        #Este método posiciona los nodos basándose en el algoritmo Kamada-Kawai,
        # que intenta minimizar la energía total del grafo considerando las longitudes de los enlaces.
        # pos = nx.kamada_kawai_layout(G)
        # nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
        # plt.title('Grafo Kamada-Kawai')
        # plt.show()
