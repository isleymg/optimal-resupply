
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
gpx = gpxpy.parse(file)

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
