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
f = Vertex(False)
f.name = "f"
g = Vertex(True)
g.name = "g"
h = Vertex(False)
h.name = "h"
i = Vertex(False)
i.name = "i"
j = Vertex(False)
j.name = "j"
k = Vertex(True)
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
maze.fix_edge(b,c)
maze.fix_edge(c,d)
maze.fix_edge(d,e)

maze.fix_edge(a,l)
maze.fix_edge(l,i)
maze.fix_edge(b,i)
maze.fix_edge(i,j)
maze.fix_edge(j,k)

maze.fix_edge(c,f)
maze.fix_edge(f,g)
maze.fix_edge(g,h)
maze.fix_edge(h,e)

# maze.find_path(a,e,2)
# print(maze.exists_path_with_extra_food(a,e,1,1))
# print(maze.exists_path_with_extra_food(a,e,1,3))
maze.find_all_paths(i,g)

print(maze.exists_path_with_extra_food(a,e,1,3))