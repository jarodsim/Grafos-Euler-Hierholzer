from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def find_eulerian_cycle(self, node):
        cycle = []

        def dfs(u):
            while self.graph[u]:
                v = self.graph[u].pop()
                dfs(v)
            cycle.append(u)

        dfs(node)

        return cycle[::-1]

    def is_eulerian_cycle(self):
        for node in self.graph:
            if len(self.graph[node]) % 2 != 0:
                return False

        start_node = next(iter(self.graph))
        cycle = self.find_eulerian_cycle(start_node)

        return len(cycle) == sum(len(self.graph[node]) for node in self.graph)


# Exemplo de uso
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)
g.add_edge(4, 0)

if g.is_eulerian_cycle():
    print("O grafo direcionado é Euleriano.")
else:
    print("O grafo direcionado NÃO é Euleriano.")
