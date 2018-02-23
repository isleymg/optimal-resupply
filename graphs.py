
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


'''
Implementation of a directed graph as an adjacency list
'''


class Node:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight
        print(str(self.id) + " connected to " + str(self.connected_to))

    def get_connections(self):
        return self.connected_to

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]



class Digraph:
    '''
    Implements a directed, weighted graph'''
    def __init__(self):
        self.node_list = dict()
        self.num_nodes = 0

    def add_node(self, key):
        if key in self.node_list:
            return
        self.num_nodes += 1
        new_node = Node(key)
        self.node_list[key] = new_node
        return new_node

    def add_edge(self, from_node, to_node, cost=0):
        '''creates directed edge from tail to head and assigns a weight'''
        if from_node not in self.node_list:
            nv = self.add_node(from_node)
        if to_node not in self.node_list:
            nv = self.add_node(to_node)

        self.node_list[from_node].add_neighbor(self.node_list[to_node], cost)


    def get_nodes(self):
        return self.node_list.keys()

    def __iter__(self):
        return iter(self.node_list.values())

    def show(self):
        for node in self.node_list:
            print(node.id)
            print(node.get_connections())
            # for conn in node.get_connections():
            #     print("( %s , %s )" % (node.getId(), conn.getId()))

"""
    def has_edge(self, tail, head):
        return tail in self.nodes and head in self.children[tail]

    def get_edge_weight(self, tail, head):
        if tail not in self.nodes:
            raise Exception("The tail node is not present in this digraph.")

        if head not in self.nodes:
            raise Exception("The head node is not present in this digraph.")

        if head not in self.children[tail].keys():
            raise ValueError("The edge ({}, {}) is not in this digraph.".format(tail, head))

        return self.children[tail][head]

    def remove_edge(self, tail, head):
        '''removes directed edge from tail to head'''
        if tail not in self.nodes:
            return

        if head not in self.nodes:
            return

        del self.children[tail][head]
        del self.parents[head][tail]
        self.edges -= 1

    def remove_node(self, node):
        '''removes node from digraph and removes all edges incident on input node'''
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

    def number_of_edges(self):
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

    def print_nodes(self):
        formatted_node = '''
        Name: {} \n
        Long: {}, Lat: {}
        Elevation: {} \n
        Next: {}
        '''

        for node in self.nodes:
            print(type(node))
            # print(formatted_node.format(node.name, 
            #                             node.longitude,
            #                             node.latitude,
            #                             node.elevation,
            #                             node.next))
 """       
