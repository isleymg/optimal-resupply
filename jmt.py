'''
John Muir Trail: 211 miles from Yosemite Valley to Mt Whitney
9 passes:
- Donohue Pass
- Island Pass
- Silver Pass
- Selden Pass
- Muir Pass
- Mather Pass
- Pinchot Pass
- Glen Pass
- Forester Pass

A lot points in between: https://80d2853cc4def76b377d-54344bc01a8b066c84096a8e7a3499ac.ssl.cf1.rackcdn.com/original/538195.jpg
Each point is a node. 
Distance and elevation gain/loss is the weight of each node

'''


from graphs import Graph 
import gpxpy

file = open('jmt.gpx')

gpx = gpxpy.parse(file)

for track in gpx.tracks:
  for segment in track.segments:
    for point in segment.points:
      print ('Point at ({0:7f},{1:7f}) -> Elevation: {2}'.format(point.latitude, point.longitude, point.elevation))






