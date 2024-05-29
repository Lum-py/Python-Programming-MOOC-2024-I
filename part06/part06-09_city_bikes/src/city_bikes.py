# Write your solution here
def get_station_data(filename: str):
    station = {}
    with open(filename) as file:        
        for line in file:            
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            station[parts[3]] = (float(parts[0]), float(parts[1]))
    return station

def distance(stations: dict, station1: str, station2: str):
    import math
    x1, y1 = stations[station1]
    x2, y2 = stations[station2]
    x_km = (x1 - x2) * 55.26
    y_km = (y1 - y2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km
    
def greatest_distance(stations: dict):
    max_distance = 0

    for i in stations:
        for j in stations:
            dist = distance(stations, i, j)
            if dist > max_distance:
                max_distance = dist
                station1 = i
                station2 = j
    return station1, station2, max_distance 


if __name__ == "__main__":
    # stations = get_station_data('stations1.csv')
    # d = distance(stations, "Designmuseo", "Hietalahdentori")
    # print(d)
    # d = distance(stations, "Viiskulma", "Kaivopuisto")
    # print(d)
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)