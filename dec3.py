# # December 3
import numpy as np
# Read input
with open('dec3_input.txt','r') as fin:
    data = fin.read().splitlines()

# Separate the two cables
cable1 = [x.strip() for x in data[0].split(',')]
cable2 = [x.strip() for x in data[1].split(',')]

for k in range(len(cable1)):
    if 'R' in cable1[k]:
        cable1[k] = np.complex(int(cable1[k][1:]),0)
    elif 'L' in cable1[k]:
        cable1[k] = np.complex(-int(cable1[k][1:]),0)
    elif 'U' in cable1[k]:
        cable1[k] = np.complex(0,int(cable1[k][1:]))
    elif 'D' in cable1[k]:
        cable1[k] = np.complex(0,-int(cable1[k][1:]))
    else:
        print('Unknown direction:')
        print(cable1[k])

        