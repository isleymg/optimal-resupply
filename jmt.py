'''
Creates a graph representation of the points from cleaned_data.gpx 
'''

from graphs import Digraph, Node
import gpxpy

# use 'jmt.gpx' for actual JMT coordinate points and waypoints
file = open('test3.gpx')
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
            if (from_node.id[2] == None) or (to_node.id[2] == None):
                weight = 0
            else:
                weight = to_node.id[2]-from_node.id[2]
            digraph.add_edge(from_node, to_node, weight)
            from_node = to_node

digraph.show()


'''
TODO: 
1) Determine function for weight:
    - elevation gain/loss
    - water sources
2) Add/modify nodes for Waypoints
    - resupply locations
    - non-resupply locations
3) Add tracks for alternate trails to resupply locations
'''