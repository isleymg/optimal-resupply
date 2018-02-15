def find_all_paths(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return [path]
  if start not in graph.keys():
    return []
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
      for newpath in newpaths:
        paths.append(newpath)
  return paths



graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
         
print (find_all_paths(graph, "A", "D"))

def find_shortest_path(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return path
  if start not in graph.keys():
    return None
  shortest = None
  for node in graph[start]:
    if node not in path:
      newpath = find_shortest_path(graph, node, end, path)
      if newpath:
        if not shortest or (len(newpath) < len(shortest)):
          shortest = newpath
  return shortest

print (find_shortest_path(graph, "A", "D"))


from graphs import Graph 

g = { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
    }


graph = Graph(g)

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())


print('The path from vertex "a" to vertex "b":')
path = graph.find_path("a", "b")
print(path)

print('The path from vertex "a" to vertex "f":')
path = graph.find_path("a", "f")
print(path)

print('The path from vertex "c" to vertex "c":')
path = graph.find_path("c", "c")
print(path)

print("----------------------------------------")

g = { "a" : ["d", "f"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["d"]
    }


graph = Graph(g)

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())

print('All paths from vertex "a" to vertex "b":')
path = graph.find_all_paths("a", "b")
print(path)

print('All paths from vertex "a" to vertex "f":')
path = graph.find_all_paths("a", "f")
print(path)

print('All paths from vertex "c" to vertex "c":')
path = graph.find_all_paths("c", "c")
print(path)
