import mission_coordinates
import utm

#Sample on how to use utm library
#u = utm.from_latlon(47.9941214, 7.8509671)
#print u
#(414278, 5316285, 32, 'T')
#
#print utm.to_latlon(*u)
#(47.994157948891505, 7.850963967574302)

#This makes a list called "cartesian_waypoints" which stores all the waypoints in cartesian form
cartesian_waypoints = []
cartesian_geofence = []
cartesian_searchgrid = []
cartesian_obstacles = []

origin = utm.from_latlon(mission_coordinates.origin[0], mission_coordinates.origin[1])


def shift_origin(h, k):
    h = h - origin[0]
    k = k - origin[1]
    return [h,k]

#zone 18 S

for i in mission_coordinates.waypoints:
    cartesian_waypoints.append(utm.from_latlon(i['latitude'], i['longitude']))

for i in mission_coordinates.geofence:
    cartesian_geofence.append(utm.from_latlon(i['latitude'], i['longitude']))

for i in mission_coordinates.search_polygon:
    cartesian_searchgrid.append(utm.from_latlon(i['latitude'], i['longitude']))

for i in mission_coordinates.obstacles:
    b = []
    a = utm.from_latlon(i['latitude'], i['longitude'])
    b.append(a[0])
    b.append(a[1])
    b.append(i['radius'])
    cartesian_obstacles.append(b)

    
#print(cartesian_waypoints[0][0:1])
#SHifting the origin

for i in range(len(cartesian_waypoints)):
    cartesian_waypoints[i] = shift_origin(cartesian_waypoints[i][0], cartesian_waypoints[i][1])

for i in range(len(cartesian_obstacles)):
    a = shift_origin(cartesian_obstacles[i][0], cartesian_obstacles[i][1])
    a.append(cartesian_obstacles[i][2])
    cartesian_obstacles[i] = a

for i in range(len(cartesian_searchgrid)):
    cartesian_searchgrid[i] = shift_origin(cartesian_searchgrid[i][0], cartesian_searchgrid[i][1])

for i in range(len(cartesian_geofence)):
    cartesian_geofence[i] = shift_origin(cartesian_geofence[i][0], cartesian_geofence[i][1])

print(cartesian_obstacles)
print(cartesian_waypoints)
#at this point all variables are in local cartesian