class Graph:
    def __init__(self):
        self.graph = dict()

    def addEdge(self, node1, node2, cost):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append((node2, int(cost)))

        # in case of undirected graph
        # self.graph[node2].append((node1, int(cost)))

    def printGraph(self):
        for source, destination in self.graph.items():
            print(f"{source}-->{destination}")


def main():
    g = Graph()
    nodes, edges = input().split()

    for _ in range(int(edges)):
        node1, node2, cost = input().split()
        g.addEdge(node1, node2, cost)

    g.printGraph()