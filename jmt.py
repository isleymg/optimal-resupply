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
import requests


API_KEY = "AIzaSyC_-MMk0HNHowTT8FPsxNFrZYnPVGuMFr8"

# TODO: Too slow-->store somewhere 
def getElevation(lat, lon):
  '''gets elevation from a given lat and lon string using Google Maps API'''
  r = requests.get("https://maps.googleapis.com/maps/api/elevation/json?locations="+lat+","+lon+"&key="+API_KEY)
  r = r.json()
  print(r)
  return r['results'][0]['elevation']


# file = open('jmt-map.gpx')
file = open('writegpx.gpx')

jmt_gpx = gpxpy.parse(file)

'''
print("TRACKS")
print("------------------------------------------")
trackpt_count = 0
for track in gpx.tracks:
  for segment in track.segments:
    for point in segment.points:
      trackpt_count += 1
      elevation = getElevation(str(point.latitude), str(point.longitude))
      #Added methods into gpx.py to allow for adding elevation
      point.set_elevation(elevation)
      print ('Trackpoint at ({0:7f},{1:7f}) -> Elevation: {2}'.format(point.latitude, point.longitude, point.elevation))


print("WAYPOINTS")
print("------------------------------------------")
waypt_count = 0
for waypoint in gpx.waypoints:
  waypt_count += 1
  print ('Waypoint at {0:25s} -> ({1:7f},{2:7f})'.format(waypoint.name, waypoint.latitude, waypoint.longitude))


for route in gpx.routes:
    print ('Route:')
    for point in route.points:
      print ('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))


print ("\nSTATISTICS")
print("------------------------------------------")
print("Trackpoints: " + str(trackpt_count))
print("Waypoints: " + str(waypt_count))
'''

# Creating a new file:
# --------------------
'''
Goal: Single GPX file with the following--
***Waypoints of main JMT markers***
- Mount Whitney Trail
- Donohue Pass
- Island Pass
- Silver Pass
- Selden Pass
- Muir Pass
- Mather Pass
- Pinchot Pass
- Glen Pass
- Forester Pass
- Purple Lake
- Reds Meadow
- Tuolomne Meadows Trail
- Cathedral Pass
- Sunrise Camp
- Lyell Fork Base Trail
- Wallace Creek
- Woods Creek
- Taboose Pass Trail
- Palisade Creek
- Blaney Meadows Trail
- Bear Creek Trail
- Bear Ridge
- Mono Creek Bridge
- Johnson Meadow
- Rosalie Lake
- Garnet Lake
- Thousand Island Lake
- Tuolomne Meadows Trail
- Halfdome Trail
- Happy Isle
- Whitney Summit

***Exit Routes to leave the trail and/or resupply***
- Exit - Bear Ridge Trail
- Exit - Bishop Pass Trail
- Exit - Bullfrog Lake Trail
- Exit - Horseshoe Lake Trail
- Exit - Kearsarge Trail
- Exit - Mammoth Pass Trail
- Exit - Reds Meadow Trail
- Exit - Muir Ranch Trail
- Exit - VVR Trail
- Exit - Tuolumne Spur
- Exit - Tuolumne Spur 2
- 

***Alternate Routes***
- Alt - Devils Postpile Alternate
- Alt - Evolution Creek Alternate
- Alt - Muir Ranch Alternate
- Alt - Whitney Portal Trail

***Main Trail Routes***
- 05 - Tuolumne CG Trail
- 03 - Whitney Trail
- 06 - Yosemite Valley Spur Trail
- 07 - Yosemite Valley Trail
- 01 - Whitney Portal Trail
- 04 - JMT - Main
- 02 - Mountaineers Route

***Segments between each waypoint***



'''

gpx = gpxpy.gpx.GPX()

# Add elevation to track points
for track in jmt_gpx.tracks:
  for segment in track.segments:
    for point in segment.points:
      try:
        # elevation = getElevation(str(point.latitude), str(point.longitude))
        #Added methods into gpx.py to allow for adding elevation
        elevation = 4000
        point.set_elevation(elevation)
      except Exception as e:
        print(e)
        print ('Trackpoint at ({0:7f},{1:7f}) -> Elevation: {2}'.format(point.latitude, point.longitude, point.elevation))
  gpx_track = gpxpy.gpx.GPXTrack()
  gpx.tracks.append(gpx_track)

print('done')



# Create first segment in our GPX track:

for route in gpx.routes:
  print ('Route:')
  for point in route.points:
    print ('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))
  gpx_segment = gpxpy.gpx.GPXTrackSegment()
  gpx_track.segments.append(gpx_segment)

# Create points:
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1234, 5.1234, elevation=1234))
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1235, 5.1235, elevation=1235))
gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(2.1236, 5.1236, elevation=1236))

# You can add routes and waypoints, too...

print ('Created GPX:' +  gpx.to_xml())


