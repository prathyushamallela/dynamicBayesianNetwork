from pyvis import network as net
if __name__ == "__main__":
    graph_data = {'A1': [('A2', 0.5), ('B1', 0.3)],
          'A2': [('A3', 0.5), ('B2', 0.2)],
          'B1': [('C1', 0.8), ('B2', 0.7)],
          'B2': [('B3', 0.6), ('C2', 0.4)],
          'C1': [('C2', 0.2)],
          'C2': [('C3', 0.1)],
          'A3': [('B3', 0.5)],
          'B3': [('C3', 0.6)]}
    net = net.Network
    for node, connections in graph_data.items():
        for connection in connections:
            child, weight = connection
            net.add_node(node, label=node)
            net.add_node(child, label=child)
            net.add_edge(node, child, value=weight)

# Visualize the network
    net.show("weighted_graph.html")