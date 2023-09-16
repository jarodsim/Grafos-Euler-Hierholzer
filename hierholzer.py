from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.IN = [0] * vertices

    def addEdge(self, v, u):
        self.graph[v].append(u)
        self.IN[u] += 1

    def DFSUtil(self, v, visited):
        visited[v] = True
        for node in self.graph[v]:
            if visited[node] == False:
                self.DFSUtil(node, visited)

    def getTranspose(self):
        gr = Graph(self.V)

        for node in range(self.V):
            for child in self.graph[node]:
                gr.addEdge(child, node)

        return gr

    def isSC(self):
        visited = [False] * self.V

        v = 0
        for v in range(self.V):
            if len(self.graph[v]) > 0:
                break

        self.DFSUtil(v, visited)

        for i in range(self.V):
            if visited[i] == False:
                return False

        gr = self.getTranspose()

        visited = [False] * self.V
        gr.DFSUtil(v, visited)

        for i in range(self.V):
            if visited[i] == False:
                return False

        return True

    def isEulerianCycle(self):
        if self.isSC() == False:
            return False

        for v in range(self.V):
            if len(self.graph[v]) != self.IN[v]:
                return False

        return True


graps = [
    [[0, 1], [1, 2], [2, 3], [3, 0], [1, 3], [3, 4], [4, 0], [4, 2]],
    [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 0],
    ],
]


def get_number_of_vertices_from_edges(edges):
    num_vertices = 0
    for edge in edges:
        num_vertices = max(num_vertices, edge[0], edge[1])
    return num_vertices + 1


def stringfy_edges(edges):
    string = ""

    for i, edge in enumerate(edges):
        if edges[i - 1][1] is not None and edge[0] != edges[i - 1][1] or i == 0:
            string += f"{edge[0]} -> {edge[1]}"
        else:
            string += f" -> {edge[1]}"

    return string


for graph in graps:
    print(f"para o grafo: {stringfy_edges(graph)}")
    g = Graph(get_number_of_vertices_from_edges(graph))
    for edge in graph:
        g.addEdge(edge[0], edge[1])

    if g.isEulerianCycle():
        print("O grafo direcionado é euleriano")
    else:
        print("O grafo direcionado não é euleriano")
