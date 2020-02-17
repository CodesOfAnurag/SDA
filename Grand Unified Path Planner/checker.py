#The objective of this program is to check if there's an obstacle between two points and return where 
import coord_conversion
  
avoidance_data = []

def distance(x1, y1, x2, y2, x3, y3):
    px = x2 - x1
    py = y2 - y2
    norm = px * px + py * py
    u = ((x3 - x1) * px + (y3 - y1) * py) / norm
    if u > 1:
        u = 1
    elif u < 0:
        u = 0
    x = x1 + u * px
    y = y1 + u * py
    dx = x - x3
    dy = y - y3
    dist = (dx * dx + dy * dy) ** 0.5
    return dist

def checker(x1, y1, x2, y2, x3, y3, radius): 
    dist = distance(x1, y1, x2, y2, x3, y3)
    if (radius >= dist):
        return 1
    else:
        return 0

l = len(coord_conversion.cartesian_waypoints)

for i in range(l-1):
    x1 = coord_conversion.cartesian_waypoints[i][0]
    y1 = coord_conversion.cartesian_waypoints[i][1]
    x2 = coord_conversion.cartesian_waypoints[i+1][0]
    y2 = coord_conversion.cartesian_waypoints[i+1][1]
    for i in coord_conversion.cartesian_obstacles:
        x3 = i[0]
        y3 = i[1]
        r = i[2]
        if (checker(x1, y1, x2, y2, x3, y3, r)):
            avoidance_data.append([x1, y1, x2, y2, x3, y3, r])

print(avoidance_data)   
