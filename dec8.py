## Dec 8
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import patches as patches

# Reshape the input into a 3-dim matrix
def reshape_input(data,width,height):
    return np.reshape(data,(int(len(data)/(height*width)),height,width))
                      
# Read data input
with open('dec8_input.txt','r') as fin:
    data = [int(m) for k in fin.read().splitlines() for m in k]
    

# Define dimensions (from puzzle instructions):
width = 25
height = 6

# Reshape data
data = reshape_input(data, width, height)

# Part 1: find layer with fewest 0
zeros = [np.count_nonzero(data[k,:,:]==0) for k in range(data.shape[0])]
min_zero_layer = zeros.index(min(zeros)) # assume there is only one layer with that number
# Print number of 1's times number of 2's
print(np.count_nonzero(data[min_zero_layer,:,:]==1)*np.count_nonzero(data[min_zero_layer,:,:]==2))

## Part 2: Final picture:
picture = np.ones(data.shape[1:])*2 # Initialize transparent picture

layer=0
while np.count_nonzero(picture==2)!=0:
    # As long as there are still transparen pixels
    for k in range(width):
        for m in range(height):
            if picture[m,k]==2 and data[layer,m,k]!=2:
                picture[m,k]=data[layer,m,k]
    layer+=1

x_coords = [x for x in range(width) for y in range(height) if picture[y,x]==0]
y_coords = [height-y for x in range(width) for y in range(height) if picture[y,x]==0]
    
# Get axes
ax = plt.gca()
# Draw black rectangles      
for k in range(len(x_coords)):
    # Create a rectangle patch and add it to the axes
    ax.add_patch(patches.Rectangle((x_coords[k]-0.5,y_coords[k]-0.5),1,1,linewidth=0.1,edgecolor='c',facecolor='k'))

ax.set_xlim([0,25])
ax.set_ylim([0,6])
plt.show() 
          