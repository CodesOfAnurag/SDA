#The objective of this program is to check if there's an obstacle between two points and return where 
import coord_conversion
import math 
  
avoidance_data = []

def checker(a, b, c, x, y, radius): 
    dist = ((abs(a * x + b * y + c)) / math.sqrt(a * a + b * b))
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
    a = y1 - y2
    b = x2 - x1
    c = (x1 * y2) - (x2 * y1)
    for i in coord_conversion.cartesian_obstacles:
        x = i[0]
        y = i[1]
        r = i[2]
        if (checker(a, b, c, x, y, r) == 1):
            avoidance_data.append([x1, y1, x2, y2, x, y, r])

print(avoidance_data)   