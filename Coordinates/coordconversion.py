import utm
lat, lon = 36.4, -28.9
var = utm.from_latlon(lat, lon)
print(var)
print(utm.to_latlon(*var))
print (var[0])
