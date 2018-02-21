'''
Creates a graph representation of the points from cleaned_data.gpx 
'''

from graphs import Digraph 
import gpxpy

file = open('cleaned_data.gpx')
jmt_gpx = gpxpy.parse(file)
gpxObj = gpxpy.gpx.GPX()


digraph = Digraph()

for track in jmt_gpx.tracks:
  for segment in track.segments:
    for point in segment.points:
      digraph.add_node(point)

digraph.get_stats()

# TODO: 
# 1) modify Digraph class to print visual of nodes
# 2) modify node data structure to allow for name/lat-long/elevation
