# # December 3
import numpy as np
# Read input
with open('dec3_input.txt','r') as fin:
    data = fin.read().splitlines()

# data = ['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83']
# Separate the two cables
cable1_direc = [x.strip() for x in data[0].split(',')]
cable2_direc = [x.strip() for x in data[1].split(',')]

# Define cable directions function
def cable_direction(cable_coords,cable_direc):
    for k in range(len(cable_direc)):
        if 'R' in cable_direc[k]:
            cable_coords.extend([(cable_coords[-1][0]+x+1,cable_coords[-1][1]) for x in range(int(cable_direc[k][1:]))])
        elif 'L' in cable_direc[k]:
            cable_coords.extend([(cable_coords[-1][0]-x-1,cable_coords[-1][1]) for x in range(int(cable_direc[k][1:]))])
        elif 'U' in cable_direc[k]:
            cable_coords.extend([(cable_coords[-1][0],cable_coords[-1][1]+x+1) for x in range(int(cable_direc[k][1:]))])
        elif 'D' in cable_direc[k]:
            cable_coords.extend([(cable_coords[-1][0],cable_coords[-1][1]-x-1) for x in range(int(cable_direc[k][1:]))])
        else:
            print('Unknown direction:')
            print(cable1[k])


cable1 = [(0,0)]
cable2 = [(0,0)]

cable_direction(cable1, cable1_direc)
cable_direction(cable2, cable2_direc)

crossings = list(set(cable1).intersection(set(cable2)).symmetric_difference([(0,0)]))
distance = [abs(x)+abs(y) for (x,y) in crossings]

print('Closest intersection:')
print(crossings[distance.index(min(distance))])
print('Distance of closest intersection:')
print((min(distance)))

