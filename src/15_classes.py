# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat=1, lon=1):
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name='Waypoint', lat=2, lon=2):
        super().__init__(lat, lon)
        self.name = name
    
    def __str__(self):
        return f"Name: \t{self.name}\nLat: \t{self.lat}\nLon: \t{self.lon}"


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name='Geocache', difficulty=1, size=1, lat=2, lon=2):
        super().__init__(name=name, lat=lat, lon=lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        attrs_str = f"\nDiff: \t{self.difficulty}\nSize: \t{self.size}"
        return super().__str__() + attrs_str


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint.name, waypoint.lat, waypoint.lon)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
#print(geocache)
