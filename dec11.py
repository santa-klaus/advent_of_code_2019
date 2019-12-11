# December 11
import numpy as np
from operator import mul
from functools import reduce
from matplotlib import pyplot as plt

# Define robot
def robot(instruction,init_pos,init_direction):
    # Initialise empty painted & white panels
    painted_panels = []
    white_panels = []
    # Initialise position and direction
    robot_pos = [init_pos]
    robot_dir = init_direction
    # Check if current output is painting or turning
    paint = True
    
    # Define parameter getter
    def get_param(instruction,param_mode,pos,rel_base):
        param = []
        
        for k in range(min(2,len(param_mode))):
            if param_mode[k]==0: # Position mode
                param.append(instruction.get(instruction.get(pos+1+k,0),0))
            elif param_mode[k]==1: # Absolute mode
                param.append(instruction.get(pos+1+k,0))
            elif param_mode[k]==2: # Relative mode
                param.append(instruction.get(instruction.get(pos+1+k,0)+rel_base,0))
            else:
                print('Unknown parameter mode!')
                print(param_mode[k])

        return param    
                
    # Start at first instruction           
    pos = 0
    # Initialize relative base
    rel_base=0
    # Initialize with first opcode
    opcode = str(instruction[pos])
    # Count executed instructions
    exec_instr = 0
    
    # loop through instructions
    while opcode != '99':
                
        # parse opcode
        if len(opcode)<=2:
            param_mode = [0,0,0]
            opcode = int(opcode)
            
        elif len(opcode) == 3:
            param_mode = [int(opcode[0]),0,0]
            opcode = int(opcode[-2:])
            
        elif len(opcode) == 4:
            param_mode = [int(opcode[1]),int(opcode[0]),0]
            opcode = int(opcode[-2:])
        elif len(opcode) == 5:
            param_mode = [int(opcode[2]),int(opcode[1]),int(opcode[0])]
            opcode = int(opcode[-2:])
        else:
            print('Undefined opcode length')
            print(len(opcode))
        
        
        # do opcode
        if opcode == 1: # Addition
            instruction[instruction[pos+3]+rel_base if param_mode[2]==2 else instruction[pos+3]] = sum(get_param(instruction,param_mode,pos,rel_base))
            pos+=4 # Move instruction pointer
        elif opcode == 2: # Multiplication
            instruction[instruction[pos+3]+rel_base if param_mode[2]==2 else instruction[pos+3]] = reduce(mul,get_param(instruction,param_mode,pos,rel_base))
            
            pos+=4 # Move instruction pointer
        elif opcode == 3: # Input
            instruction[instruction[pos+1]+rel_base if param_mode[0]==2 else instruction[pos+1]] = [1 if robot_pos[-1] in white_panels else 0] # Take input from current input position
            pos+=2 # Move instruction pointer
        elif opcode == 4: # Output
            if paint: # Paint
                painted_panels.append(robot_pos[-1])
                if get_param(instruction,[param_mode[0]],pos,rel_base)[0]==1: # Paint if output 1
                    white_panels.append(robot_pos[-1])
                elif get_param(instruction,[param_mode[0]],pos,rel_base)[0]!=0:
                    print('Weird output')
                    print(get_param(instruction,[param_mode[0]],pos,rel_base)[0])
                    
                paint=False # Next output is turning
            else: # Turn
                robot_dir+=[1 if get_param(instruction,[param_mode[0]],pos,rel_base)[0]==1 else -1][0] # +1 for turn right, -1 for turn left
                # Move:
                if robot_dir%4==0: #Up
                    robot_pos.append((robot_pos[-1][0],robot_pos[-1][1]+1))
                elif robot_dir%4==1: # Right
                    robot_pos.append((robot_pos[-1][0]+1,robot_pos[-1][1]))
                elif robot_dir%4==2: #Down
                    robot_pos.append((robot_pos[-1][0],robot_pos[-1][1]-1))
                elif robot_dir%4==3: # Left
                    robot_pos.append((robot_pos[-1][0]-1,robot_pos[-1][1]))
                paint=True # Next output is painting                    
                
            pos+=2 # Move instruction pointer
        elif opcode == 5 or opcode == 6: # Jump if true/false  
            params = get_param(instruction,param_mode,pos,rel_base)
            if (opcode==5 and params[0]) or (opcode==6 and not params[0]):
                pos = params[1] # Jump instruction pointer
            else:
                pos+=3 # Move instruction pointer
        elif opcode == 7: # Less than
            instruction[instruction[pos+3]+rel_base if param_mode[2]==2 else instruction[pos+3]] = int(np.diff(get_param(instruction,param_mode,pos,rel_base))>0)
            pos+=4 # Move instruction pointer
        elif opcode == 8: # Equals
            instruction[instruction[pos+3]+rel_base if param_mode[2]==2 else instruction[pos+3]] = int(np.diff(get_param(instruction,param_mode,pos,rel_base))==0)
            pos+=4 # Move instruction pointer
        elif opcode == 9: # Adjust relative base
            rel_base += get_param(instruction,[param_mode[0]],pos,rel_base)[0]
            pos+=2
        else:
            print("Invalid opcode: ")
            print(opcode,pos)
            input()
            return []
           
        exec_instr+=1
        opcode = str(instruction[pos])
            
        
    return [white_panels,painted_panels,robot_pos]
# Read input
with open('dec11_input.txt','r') as fin:
# with open('example.txt','r') as fin:
    data = [int(y) for x in fin.read().splitlines() for y in x.split(',')]

# Cast data to dictionary
data_dict = dict(zip(range(len(data)),data))

# Runt part 1
[white_panel,painted_panels,robot_pos] = robot(data_dict.copy(),(0,0),0)

x_coords = [x[0] for x in robot_pos]
y_coords = [x[1] for x in robot_pos]

plt.plot(x_coords,y_coords)
plt.show()

print(len(set(painted_panels)))

