'''
Creates a graph representation of the points from cleaned_data.gpx 
'''

from graphs import Digraph, Node
import gpxpy

file = open('test2.gpx')
jmt_gpx = gpxpy.parse(file)
gpxObj = gpxpy.gpx.GPX()


digraph = Digraph()

'''get starting track point'''
for track in jmt_gpx.tracks:
  for segment in track.segments:
    for point in segment.points:
        from_node = digraph.add_node(Node((point.latitude, point.longitude, point.elevation)))
        break


'''add edge and weight (elevation difference) between each track point'''
to_node = None
for track in jmt_gpx.tracks:
  for segment in track.segments:
    for point in segment.points:
        to_node = Node((point.latitude, point.longitude, point.elevation))
        digraph.add_edge(from_node, to_node)
        from_node = to_node

## POR QUE NODE CONNECTIONS RETURNING EMPTY?!
for node in digraph.node_list:
    print(node.connected_to)
# digraph.show()


# TODO: 
# 1) modify Digraph class to print visual of nodes
