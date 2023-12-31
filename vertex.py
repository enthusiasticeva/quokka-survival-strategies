"""
Vertex
=======
 
Represents a vertex in the maze, holds the information about other
connected vertices, and checks whether this vertex has food.
"""


class Vertex:
    """
    Vertex represents a location in the quokka's quest to find food.
    It contains the relevant information surrounding the location.

    Attributes:
        * self.has_food (bool) - indicates whether this location has food.
        * self.edges (List[Vertex]) - list of connected vertices.

    Functions:
        * add_edge(self, v) - connects 'v' to this vertex by adding an edge.
        * rm_edge(self, v) - removes the vertex 'v' from this vertex's edges,
            breaking the connection between this vertex and 'v'.
    """

    def __init__(self, has_food: bool) -> None:
        """
        Initialises this vertex, by setting the attribute whether it has food.

        :param has_food - boolean indicating whether this location has food.
        """

        self.has_food = has_food
        self.edges = []
        self.parent = None
        self.visited = False
        self.name = ""

    def add_edge(self, v: 'Vertex') -> None:
        """
        Add an edge between this vertex and vertex 'v'.

        :param v - The vertex to add an edge between.
        """
        # TODO implement me please!
        if v in self.edges or v == None or v == self:
          return
        
        self.edges.append(v)

    def rm_edge(self, v: 'Vertex') -> None:
        """
        Removes the edge between this vertex and 'v'.

        :param v - The vertex to remove from edges.
        """
        # TODO implement me please!
        if v not in self.edges or v == None:
          return

        self.edges.remove(v)

    def set_parent(self, v: 'Vertex') -> None:
      self.parent = v