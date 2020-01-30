#This program's purpose is to just obtain the relevant coordinates from mission.json
#   mission.json will be obtained from interop
import json

#Obtain the dictionary from the JSON file
with open('mission.json', 'r') as f:
    data = f.read()

mission_obj = json.loads(data)
origin = [38.146614, -76.426927]

#Obtain the geofence coordinates from the dictionary
geofence = mission_obj["flyZones"][0]["boundaryPoints"]

#Obtain the waypoints from the dictionary
waypoints = mission_obj["waypoints"]

#Obtain the search polygon
search_polygon = mission_obj["searchGridPoints"]

#Emergent target
emergent = mission_obj["emergentLastKnownPos"]

#UGV geofence
ugv_geofence = mission_obj["airDropBoundaryPoints"]

#UGV waypoints
ugv_waypoints = mission_obj["ugvDrivePos"]

#UGV target
drop_target = mission_obj["airDropPos"]

#Obstacles
obstacles = mission_obj["stationaryObstacles"]
