from graph import Graph
from graph import Vertex

gp = Graph()

def buildGraph():
    gp.add_vertex("Cardassian Union")
    gp.add_vertex("Romulan Empire")
    gp.add_vertex("Borg")
    gp.add_vertex("United Federation of Planets")
    gp.add_vertex("Bajoran")
    gp.add_vertex("Klingon Empire")
    gp.add_vertex("Tholian Assembly")

    gp.add_edge("Cardassian Union", "Romulan Empire", 42)
    gp.add_edge("Cardassian Union", "Bajoran", 14)
    gp.add_edge("Bajoran", "Tholian Assembly", 80)
    gp.add_edge("Tholian Assembly", "Borg", 10)
    gp.add_edge("Borg", "Romulan Empire", 33)
    gp.add_edge("Romulan Empire","United Federation of Planets", 53)
    gp.add_edge("United Federation of Planets","Bajoran", 22)
    gp.add_edge("United Federation of Planets", "Klingon Empire", 87)
    gp.add_edge("Klingon Empire","Borg", 41)

def bfs(start):
    gp.bfs(start)


if __name__ == '__main__':
    buildGraph()
    for vertex in gp.vertices.values():
        print(f"Vertex: {vertex.name}")

    vStart = input(str("Starting Vertex: "))
    while vStart not in gp.vertices:
        vStart = input(str("Starting Vertex: "))
    bfs(vStart)
