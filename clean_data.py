'''
John Muir Trail: 211 miles from Yosemite Valley to Mt Whitney

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


A lot points in between: https://80d2853cc4def76b377d-54344bc01a8b066c84096a8e7a3499ac.ssl.cf1.rackcdn.com/original/538195.jpg
Each point is a node. 
Distance and elevation gain/loss is the weight of each node

'''
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
file = open('jmt-detailed.gpx')
jmt_gpx = gpxpy.parse(file)
gpxObj = gpxpy.gpx.GPX()



# A GPXTrack consists of GPXTrackSegments that are made up of GPXTrackPoints

# Add elevation to gpx xml
for track in jmt_gpx.tracks:
  gpx_track = gpxpy.gpx.GPXTrack(name=track.name)
  gpxObj.tracks.append(gpx_track) 
  for segment in track.segments:
    for point in segment.points:
      try:
        # elevation = getElevation(str(point.latitude), str(point.longitude))
        #Added methods into gpx.py to allow for adding elevation
        elevation = 4000
        point.set_elevation(elevation)
        gpx_segment = gpxpy.gpx.GPXTrackSegment()
        gpx_track.segments.append(gpx_segment)
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(point.latitude, point.longitude, elevation=elevation, name=point.name ))
      except Exception as e:
        print(e)


# Add routes to gpx xml
for route in jmt_gpx.routes:
  gpx_route = gpxpy.gpx.GPXRoute(name=route.name)
  gpxObj.routes.append(gpx_route)
  for point in route.points:
    # TODO: get elevation for route points
    gpx_route.points.append(gpxpy.gpx.GPXRoutePoint(point.latitude, point.longitude, elevation=point.elevation))

# Add waypoints to gpx xml
for waypoint in jmt_gpx.waypoints:
  gpxObj.waypoints.append(waypoint)

# Uncomment to view XML string
# print ('Created GPX:' +  gpxObj.to_xml())

with open("cleaned_data.txt", "w") as f:
  f.write(gpxObj.to_xml())

print("finished cleaning.")
