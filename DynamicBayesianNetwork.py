import configparser
from pyvis.network import Network
import ast
import Graph

class DynamicBayesianNetwork(object):
    def __init__(self):
        pass

    def getGraphDetails(self, filePath):
        config = configparser.ConfigParser()
        config.read(filePath)
        try:
            graph = config.get('Details', 'graph2')
            graphpath = config.get('Details', 'graphNetwork.txt')
            nodecount = config.get('GraphDetails', 'nodecount')
            timeslice = config.get('GraphDetails', 'timeslice')
            query = config.get('Algorithm', 'query')
            applyPF = config.get('Algorithm', 'ParticleFilter')
        except configparser.Error as e:
            print(f"Error: {e}")
        print(graphpath)
        print(graph)
        print(nodecount)
        print(timeslice)
        print(query)
        print(applyPF)
        return graph, nodecount, timeslice, query, applyPF

    def testNet(self, graph):
        print(graph.items)

    def createDynamicGraph(self, graphpath):
        g = Graph()
        nodes, edges = input().split()
        for _ in range(int(edges)):
            node1, node2, cost = input().split()
            g.addEdge(node1, node2, cost)

        g.printGraph()

        '''
        graph = Graph()
        net = Network()
        graph = ast.literal_eval(graphip)
        print(graph)
        for parent, connections in graph.items():
            for connection in connections:
                child, weight = connection
                net.add_node(parent, label=parent)
                net.add_node(child, label=child)
                net.add_edge(parent, child, value=weight)
        '''

