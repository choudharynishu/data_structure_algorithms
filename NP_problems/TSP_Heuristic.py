'''
   Nearest Neighbor heuristic-based solution of the Traveling Salesman Problem
   Running Time:
'''

#Import Required Packages
import math

def squared_distance(source,destination, geo_data):
    '''
    Returns Squared Euclidean distance between the given source and destination pair
    :param source: index of the source node
    :param destination: index of the destination node
    :param geo_data: dictionary containing location info (x,y) with index as key,
                     Here x and y represent coordinates in cartesian space
    :return: Squared Euclidean distance
    '''
    x1, y1 = geo_data[source]
    x2, y2 = geo_data[destination]
    return ((x1-x2)**2+(y1-y2)**2)

#Read the input file
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/TSP_heuristic.txt", "r")
data = file.readlines()

geo_data = {}

for index, item in enumerate(data):
    if index == 0:
        n_cities = int(data[index])
    else:
        geo_data[index] = tuple(map(float, data[index].split()[1:]))

visited = set() #set representing cities visited so far
source_index = 1 #Index of the city from which distances of unvisited cities is calculated
visited.add(source_index)
tsp_tour = []

while len(visited) < n_cities:
    #List of Tuples that store the (distance, index) from the source index for the unvisited cities
    unvisited_cities_dist = [(squared_distance(source_index, x, geo_data), x) for x in range(1, n_cities+1) if x not in visited]
    nearest_city_sq_dist, nearest_city_index = min(unvisited_cities_dist, key=lambda t: t[0])
    tsp_tour.append((nearest_city_sq_dist))
    source_index = nearest_city_index
    visited.add(nearest_city_index)

tsp_tour.append(squared_distance(source_index, 1, geo_data))
tsp_tour_length = sum(list(map(math.sqrt, tsp_tour)))
print(math.floor(tsp_tour_length))




