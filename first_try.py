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

        # TODO implement me please

        cursor = s
        nodes_since_food = 0
        visited = []

        path = self.DFS_visit(s,visited, nodes_since_food, k, t,s)
        print(path)


    def DFS_visit(self, v: "Vertex", visited, nodes_since_food,k,t,s):
      