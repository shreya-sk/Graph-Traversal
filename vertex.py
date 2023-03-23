
class Vertex:

    def __init__(self,  has_food: bool) -> None:
        self.has_food = has_food
        self.edges = []


    def add_edge(self, v: 'Vertex') -> None:

        if v != None and self != None and v not in self.edges and v != self:
            self.edges.append(v)


    def rm_edge(self, v: 'Vertex') -> None:

        if v != None and self != None and v in self.edges and v != self:
            self.edges.remove(v)
