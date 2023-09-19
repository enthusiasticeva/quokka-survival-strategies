from graph import QuokkaMaze
from vertex import Vertex

maze = QuokkaMaze()

a = Vertex(False)
a.name = "a"
b = Vertex(False)
b.name = "b"
c = Vertex(True)
c.name = "c"
d = Vertex(False)
d.name = "d"
e = Vertex(True)
e.name = "e"
f = Vertex(True)
f.name = "f"
g = Vertex(False)
g.name = "g"
h = Vertex(True)
h.name = "h"
i = Vertex(False)
i.name = "i"
j = Vertex(True)
j.name = "j"
k = Vertex(False)
k.name = "k"
l = Vertex(False)
l.name = "l"

maze.add_vertex(a)
maze.add_vertex(b)
maze.add_vertex(c)
maze.add_vertex(d)
maze.add_vertex(e)
maze.add_vertex(f)
maze.add_vertex(g)
maze.add_vertex(h)
maze.add_vertex(i)
maze.add_vertex(j)
maze.add_vertex(k)
maze.add_vertex(l)

maze.fix_edge(a,b)
maze.fix_edge(a,c)
maze.fix_edge(a,d)
maze.fix_edge(b,e)
maze.fix_edge(b,f)
maze.fix_edge(c,g)
maze.fix_edge(d,h)
maze.fix_edge(d,i)
maze.fix_edge(d,j)
maze.fix_edge(i,k)
maze.fix_edge(j,l)

maze.find_all_paths(a,l)
