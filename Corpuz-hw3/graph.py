from collections import deque
class Vertex:
    def __init__(self, name):
        self.name = name
        self.visited = False

        # this is where edges will go
        self.neighbors = []

    def add_neighbor(self, nName, weight):
        self.neighbors.append((nName,weight))

        self.neighbors.sort(key=lambda edge: edge[1])

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_edge(self,start,end,weight):
        if (start not in self.vertices):
            self.vertices[start] = Vertex(start)

        if (end not in self.vertices):
            self.vertices[end] = Vertex(end)

        self.vertices[start].add_neighbor(end,weight)
        self.vertices[end].add_neighbor(start,weight)

    #the different nodes in the graph
    def add_vertex(self, vName):
        if vName not in self.vertices:
            self.vertices[vName] = Vertex(vName)


    #Queue
    #referenced from GeeksforGeeks on Queues for Python
    def bfs(self,start):

        q = start

        for vertex in self.vertices:
            q.append(vertex)




    #List
    # def dfs(self):