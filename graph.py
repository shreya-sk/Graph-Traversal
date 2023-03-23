
from typing import List, Union
from vertex import Vertex

class QuokkaMaze:

    def __init__(self) -> None:
        """
        Initialises an empty graph with a list of empty vertices.
        """
        self.vertices = []

    def food_list(self) -> List:
        food_list = []
        for i in self.vertices:
            if i.has_food == True:
                food_list.append(i)
        return food_list

    def trial(self, start, end, k, temp, count):
        temp = temp + [start]

        if start == end:
            return temp

        if count < k:
            for i in start.edges:
                if i not in temp:
                    if i == end:
                        temp.append(i)
                        return temp
                    else:
                        if i in self.food_list():
                            count = - 1
                        newPath = self.trial(i, end, k, temp, count+1)

                    if newPath:
                        return newPath

            return None

    def possible_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        ways = []
        for v in start.edges:
            if v not in path:
                temp_paths = self.possible_paths(v, end, path)
                for poss_path in temp_paths:
                    ways.append(poss_path)

        return ways

    def add_vertex(self, v: Vertex) -> bool:

        if v != None and self != None and v not in self.vertices:
            self.vertices.append(v);
            return True

        return False

    def fix_edge(self, u: Vertex, v: Vertex) -> bool:

        if u != None and v != None and self != None:
            if u in self.vertices and v in self.vertices:
                if u in v.edges and v in u.edges:
                    return False
                else:
                    u.add_edge(v)
                    v.add_edge(u)
                    return True
            else:
                return False
        else:
            return False

    def block_edge(self, u: Vertex, v: Vertex) -> bool:

        if u != None and v != None and self != None:
            if u in self.vertices and v in self.vertices:
                if u not in v.edges and v not in u.edges:
                    return False
                else:
                    u.rm_edge(v)
                    v.rm_edge(u)
                    return True
            else:
                return False
        else:
            return False


    def find_path(
            self,
            s: Vertex,
            t: Vertex,
            k: int
    ) -> Union[List[Vertex], None]:

        if k >=0 and s != None and t != None and self != None and s in self.vertices and t in self.vertices and s!=t:
            return(self.trial(s, t, k, [], 0))

        else:
            return None

    def find_vertexes(self, s : 'Vertex', t : 'Vertex',ls : list )->list:

        ls = ls + [s]

        if s == t:
            return [ls]

        paths = []
        for i in s.edges:
            if i not in ls:
                path = self.find_vertexes(i,t,ls)

                if path:
                    for p in path:
                        paths.append(p)

        return paths

    # def exists_path_with_extra_food(
    #     self,
    #     s: Vertex,
    #     t: Vertex,
    #     k: int,
    #     x: int
    # ) -> bool:
    #
    #     def choose_way(start, end, energy, extra):
    #
    #         temp = self.possible_paths(s, t, [])
    #
    #         for way in temp:
    #             temp_k = energy
    #             temp_x = extra
    #
    #             i = 0
    #             while i < len(way):
    #
    #                 if way[i] == end:
    #                     return True
    #
    #                 if way[i] in food_list:
    #                     temp_k = energy - 1
    #
    #                 else:
    #                     if temp_k > 0:
    #                         temp_k = temp_k - 1
    #
    #                     elif temp_x > 0:
    #                         temp_x = temp_x - 1
    #                         temp_k = energy - 1
    #
    #                     else:
    #                         break
    #                 i = i + 1
    #
    #         return False
    #
    #     food_list = self.food_list()
    #     food_list.append(s)
    #     ls = []
    #
    #     if k > 0 and x >= 0 and s!= None and t != None and self != None and s in self.vertices and t in self.vertices:
    #         return choose_way(s, t, k, x)
    #
    #     else:
    #         return False

    def exists_path_with_extra_food(
        self,
        s: Vertex,
        t: Vertex,
        k: int,
        x: int
    ) -> bool:

            if s != None and t != None and self != None and k >= 0 and x >= 0:
                if s in self.vertices and t in self.vertices:
                    if s != t:
                        temp = []
                        final = self.find_vertexes(s,t,temp)

                        if final != None or final != []:

                            for path in final:
                                print(len(path))
                                temp = k
                                extra = x

                                if path != None or path != []:
                                    for p in path:
                                        m = len(path) -1

                                        if p == m:
                                            print("p==t")
                                            return True

                                        if p.has_food == True:
                                            print("p has food")
                                            temp = k -1

                                        else:
                                            if k > 0:
                                                print("k>0")
                                                temp -= 1
                                            elif extra > 0:
                                                print("extra > 0")
                                                extra -= 1
                                                temp = k -1
                                            else:
                                                break

                        #return self.find_extra_food_path(t, k, x, final)
                            print("false oops")
                            return False

A = Vertex(True) #0x7f02d01cdfa0
B = Vertex(False) #0x7f02d029b970
C = Vertex(False) #0x7f02d029b9a0
D = Vertex(False) #0x7f02d01f37c0
E = Vertex(False) #0x7f02d01f36a0
G = Vertex(False) #0x7f1a8e8ac640
F = Vertex(False)

m = QuokkaMaze()

m.add_vertex(A)
m.add_vertex(B)
m.add_vertex(C)
m.add_vertex(D)
m.add_vertex(E)
m.add_vertex(G)
m.add_vertex(F)

m.fix_edge(A, B)
m.fix_edge(B, C)
m.fix_edge(C, D)
m.fix_edge(D, E)
m.fix_edge(D, G)
m.fix_edge(C, F)
m.fix_edge(A, F)
m.fix_edge(F ,G)

print(m.find_path(A,D,4))
print(m.exists_path_with_extra_food(A, D, 1, 1))
