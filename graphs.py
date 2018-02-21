

class Graph(object):
    '''
    Python class to represent a Graph object
    '''

    def __init__(self, graph_dict=None):
        '''Initializes a dictionary, or empty dict if nothing specified'''
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        '''If a vertex doesn't already exist, add it as a key with empty dict as value'''
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        '''Edge is of type set, tuple or list'''
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ Generates the edges of the 
            graph. Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_path(self, start, end, path=None):
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath
        return None

    def find_all_paths(self, start, end, path=[]):
        graph = self.__graph_dict
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for p in newpaths:
                    paths.append(p)
        return paths

    def vertex_degree(self, vertex):
        '''Returns the number of edges connecting it (loops counted as double)'''
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree


class Digraph:
    '''
    Implements a directed, weighted graph'''
    def __init__(self):
        self.nodes = set()
        self.children = dict()
        self.parents = dict()
        self.edges = 0

    def add_node(self, node):
        if node in self.nodes:
            return
        self.nodes.add(node)
        self.children[node] = dict()
        self.parents[node] = dict()

    def add_arc(self, tail, head, weight):
        '''creates directed arc from tail to head and assigns a weight'''
        if tail not in self.nodes:
            self.add_node(tail)
        if head not in self.nodes:
            self.add_node(head)

        self.children[tail][head] = weight
        self.parents[head][tail] = weight
        self.edges += 1

    def has_arc(self, tail, head):
        return tail in self.nodes and head in self.children[tail]

    def get_arc_weight(self, tail, head):
        if tail not in self.nodes:
            raise Exception("The tail node is not present in this digraph.")

        if head not in self.nodes:
            raise Exception("The head node is not present in this digraph.")

        if head not in self.children[tail].keys():
            raise ValueError("The edge ({}, {}) is not in this digraph.".format(tail, head))

        return self.children[tail][head]

    def remove_arc(self, tail, head):
        '''removes directed arc from tail to head'''
        if tail not in self.nodes:
            return

        if head not in self.nodes:
            return

        del self.children[tail][head]
        del self.parents[head][tail]
        self.edges -= 1

    def remove_node(self, node):
        '''removes node from digraph and removes all arcs incident on input node'''
        if node not in self.nodes:
            return

        self.edges -= len(self.children[node]) + len(self.parents[node])

        #Unlink children:
        for child in self.children[node]:
            del self.parents[child][node]

        #Unlink parents"
        for parents in self.parents[node]:
            del self.children[parents][node]

        del self.children[node]
        del self.parents[node]
        self.nodes.remove(node)

    def __len__(self):
        return len(self.nodes)

    def number_of_arcs(self):
        return self.edges

    def get_parents_of(self, node):
        '''returns all parents of node'''
        if node not in self.nodes:
            return []
        return self.parents[node].keys()

    def get_children_of(self, node):
        '''returns all children of node'''
        if node not in self.nodes:
            return []
        return self.children[node].keys()

    def get_stats(self):
        print("Number of nodes: {}\nNumber of children: {}\nNumber of parents: {}\nNumber of edges: {}"
              .format(len(self.nodes), len(self.children), len(self.parents), self.edges))

    def clear(self):
        del self.nodes[:]
        self.children.clear()
        self.parents.clear()
        self.edges=0

