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
from_node = None
for track in jmt_gpx.tracks:
  for segment in track.segments:
    for point in segment.points:
        from_node = Node((point.latitude, point.longitude, point.elevation))
        start_node = from_node
        break


'''add edge and weight (elevation difference) between each track point'''
to_node = None
for track in jmt_gpx.tracks:
  for segment in track.segments:
    for point in segment.points:
        to_node = Node((point.latitude, point.longitude, point.elevation))

        if to_node.id == from_node.id:
            pass
        else:
            digraph.add_edge(from_node, to_node)
            from_node = to_node
            print(digraph.node_list[from_node].connected_to.keys())
        # print(digraph.show())

digraph.show()
