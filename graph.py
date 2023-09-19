"""
Quokka Maze
===========
 
This file represents the quokka maze, a graph of locations where a quokka is
trying to find a new home.

Please help the quokkas find a path from their current home to their
destination such that they have sufficient food along the way!

*** Assignment Notes ***

This is the main file that will be interacted with during testing.
All functions to implement are marked with a `TODO` comment.

Please implement these methods to help the quokkas find their new home!
"""

from typing import List, Union

from vertex import Vertex

import copy


class QuokkaMaze:
    """
    Quokka Maze
    -----------

    This class is the undirected graph class that will contain all the
    information about the locations between the Quokka colony's current home
    and their final destination.

    We _will_ be performing some minor adversarial testing this time, so make
    sure you're performing checks and ensuring that the graph is a valid simple
    graph!

    ===== Functions =====

        * block_edge(u, v) - removes the edge between vertex `u` and vertex `v`
        * fix_edge(u, v) - fixes the edge between vertex `u` and `v`. or adds an
            edge if non-existent
        * find_path(s, t, k) - find a SIMPLE path from veretx `s` to vertex `t`
            such that from any location with food along this simple path we
            reach the next location with food in at most `k` steps
        * exists_path_with_extra_food(s, t, k, x) - returns whether it’s
            possible for the quokkas to make it from s to t along a simple path
            where from any location with food we reach the next location with
            food in at most k steps, by placing food at at most x new locations

    ===== Notes ======

    * We _will_ be adversarially testing, so make sure you check your params!
    * The ordering of vertices in the `vertex.edges` does not matter.
    * You MUST check that `k>=0` and `x>=0` for the respective functions
        * find_path (k must be greater than or equal to 0)
        * exists_path_with_extra_food (k and x must be greater than or equal to
            0)
    * This is an undirected graph, so you don't need to worry about the
        direction of traversing during your path finding.
    * This is a SIMPLE GRAPH, your functions should ensure that it stays that
        way.
    * All vertices in the graph SHOULD BE UNIQUE! IT SHOULD NOT BE POSSIBLE
        TO ADD DUPLICATE VERTICES! (i.e the same vertex instance)
    """

    def __init__(self) -> None:
        """
        Initialises an empty graph with a list of empty vertices.
        """
        self.vertices = []
        self.currentPath = []
        self.simplePaths = []

    def add_vertex(self, v: Vertex) -> bool:
        """
        Adds a vertex to the graph.
        Returns whether the operation was successful or not.

        :param v - The vertex to add to the graph.
        :return true if the vertex was correctly added, else false
        """
        # TODO implement me, please?
        if v in self.vertices or type(v) != Vertex:
          return False
        
        self.vertices.append(v)
        return True

    def fix_edge(self, u: Vertex, v: Vertex) -> bool:
        """
        Fixes the edge between two vertices, u and v.
        If an edge already exists, then this operation should return False.

        :param u - A vertex
        :param v - Another vertex
        :return true if the edge was successfully fixed, else false.
        """

        # TODO implement me please.
        if v not in self.vertices or u not in self.vertices:
          return False

        if type(v) != Vertex or type(u) != Vertex:
          return False

        if v in u.edges or u in v.edges:
          return False

        u.add_edge(v)
        v.add_edge(u)
        return True

    def block_edge(self, u: Vertex, v: Vertex) -> bool:
        """
        Blocks the edge between two vertices, u and v.
        Removes the edge if it exists.
        If not, it should be unsuccessful.

        :param u - A vertex
        :param v - Another vertex.
        :return true if the edge was successfully removed, else false.
        """

        # TODO implement me, please!
        if v not in self.vertices or u not in self.vertices:
          return False

        if type(v) != Vertex or type(u) != Vertex:
          return False

        if v not in u.edges or u not in v.edges:
          return False

        u.rm_edge(v)
        v.rm_edge(u)
        return True

    def find_path(
            self,
            s: Vertex,
            t: Vertex,
            k: int
    ) -> Union[List[Vertex], None]:
        """
        find_path returns a SIMPLE path between `s` and `t` such that from any
        location with food along this path we reach the next location with food
        in at most `k` steps

        :param s - The start vertex for the quokka colony
        :param t - The destination for the quokka colony
        :param k - The maximum number of hops between locations with food, so
        that the colony can survive!
        :returns
            * The list of vertices to form the simple path from `s` to `t`
            satisfying the conditions.
            OR
            * None if no simple path exists that can satisfy the conditions, or
            is invalid.

        Example:
        (* means the vertex has food)
                    *       *
            A---B---C---D---E

            1/ find_path(s=A, t=E, k=2) -> returns: [A, B, C, D, E]

            2/ find_path(s=A, t=E, k=1) -> returns: None
            (because there isn't enough food!)

            3/ find_path(s=A, t=C, k=4) -> returns: [A, B, C]

        """
        
        if s == None or t == None or k == 0:
          return None
        
        for vertex in self.vertices:
          vertex.parent = None
          vertex.visited = False
          
        path = self.DFS_visit(s, s, t, k, k)
        #self.print_path(path)
        if path == []:
          return None
        
        return path
        
    def print_path(self, path):
      if path == []:
        print("No path found")
        return
      for v in path:
        print(v.name, end = "")
      print()


    def DFS_visit(self, v, s, t, k, food_left):
      v.visited = True
      #print(v.name)
      
      if v == t:
        cursor = v
        path = []
        while cursor != s:
          path.append(cursor)
          cursor = cursor.parent
    
        path.append(s)
        path.reverse()
        return path
      
      food_left -= 1
      
      # print(v.name, ": ", end = "")
      # self.print_path(v.edges)
      results = []
      for neighbour in v.edges:
        # print(v.name, ": ", neighbour.name)
        if neighbour.visited == False:
          neighbour.parent = v
          if neighbour.has_food:
            food_left = k
          if food_left == 0:
            continue
          results += self.DFS_visit(neighbour, s, t, k, food_left)
      return results
        
    

    def exists_path_with_extra_food(
        self,
        s: Vertex,
        t: Vertex,
        k: int,
        x: int
    ) -> bool:
        """
        Determines whether it is possible for the quokkas to make it from s to
        t along a SIMPLE path where from any location with food we reach the
        next location with food in at most k steps, by placing food at at most
        x new locations.

        :param s - The start vertex for the quokka colony
        :param t - The destination for the quokka colony
        :param k - The maximum number of hops between locations with food, so
        that the colony can survive!
        :param x - The number of extra foods to add.
        :returns
            * True if with x added food we can complete the simple path
            * False otherwise.

        Example:
        (* means the vertex has food)
                            *
            A---B---C---D---E

            1/ exists_with_extra_food(A, E, 2, 0) -> returns: False
                (because we can't get from A to E with k=2 and 0 extra food)

            2/ exists_with_extra_food(A, E, 2, 1) -> returns: True
                (Yes, if we put food on `C` then we can get to E with k=2)

            3/ exists_with_extra_food(A, E, 1, 6) -> returns: True
                (Yes, if we put food on `B`, `C`, `D` then we reach E!)

        """

        # TODO implement me please
        if s == None or t == None or k == 0:
          return False
        
        paths = self.find_all_paths(s,t)
        
        
        for path in paths:
          valid = True
          food_left = k
          extra_left = x
          
          for step in path[1:]:
            food_left -= 1
            
            if step.has_food:
              food_left = k
              
            if food_left == 0:
              if extra_left < 1:
                valid = False
                break
              extra_left -= 1
              food_left = k
              
          if not valid:
            continue
          else:
            return True
        
        return False


    def find_all_paths(self, s, t):
        if s == None or t == None:
            return False
          
        for vertex in self.vertices:
          vertex.parent = None
          vertex.visited = False
        
          
        self.currentPath = []
        self.simplePaths = []
        self.DFS_all(s,t)
        
        # for p in self.simplePaths:
        #   self.print_path(p)
          
        return self.simplePaths
      
    def DFS_all(self, u, t):
      if u.visited == True:
        return
      
      u.visited = True
      self.currentPath.append(u)
      
      if u == t:
        self.simplePaths.append(list(self.currentPath))
        u.visited = False
        self.currentPath.pop()
        
        return
        
      for neighbour in u.edges:
        self.DFS_all(neighbour, t)
        
      self.currentPath.pop()
      u.visited = False
    