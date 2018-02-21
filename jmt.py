'''
Creates a graph representation of the points from cleaned_data.gpx 
'''

from graphs import Digraph 
import gpxpy

file = open('test_data.gpx')
jmt_gpx = gpxpy.parse(file)
gpxObj = gpxpy.gpx.GPX()


digraph = Digraph()

'''add each track point to digraph'''

for track in jmt_gpx.tracks:
  for segment in track.segments:
    for point in segment.points:
      start_node = point
      digraph.add_node(start_node)
      break

print(start_node)


'''add edge and weight (elevation difference) between each track point'''
prev_node = start_node
for track in jmt_gpx.tracks:
  for segment in track.segments:
    for point in segment.points:
      digraph.add_edge(prev_node, point, 2)
      prev_node = point

print(prev_node)


digraph.get_stats()
# digraph.get_nodes()

# TODO: 
# 1) modify Digraph class to print visual of nodes
# 2) modify node data structure to allow for name/lat-long/elevation
