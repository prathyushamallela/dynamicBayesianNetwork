import configparser
from pyvis.network import Network
import ast





if __name__ == "__main__":
    print("The Dynamic Bayesian Network is:")
    g1 = DynamicBayesianNetwork
    filePath="ConfigurationFile.ini"
    graph, nodecount, timeslice, query, applyPF=g1.getGraphDetails(g1,filePath)
    print (graph, nodecount, timeslice, query, applyPF)
    g1.testNet(g1,graph)
    #g1.createDynamicGraph(g1,graph)
    #g1.createDynamicGraph()