# December 9
import numpy as np
from operator import mul
from functools import reduce

# Define intcode program
# Accept noun and verb
# Take input as list
# Give output as list
# Take instructions as directory
def intcode(instruction,noun,verb,inp):
    # Permute instructions according to noun and verb
    instruction[1] = noun
    instruction[2] = verb
    # Count the number of inputs queried
    inp_counter = 0
    # Initialise empty outputs
    outputs = []
    
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
#             print('Enter input:')
#             print(inp[inp_counter])
            instruction[instruction[pos+1]+rel_base if param_mode[0]==2 else instruction[pos+1]] = inp[inp_counter] # Take input from current input position
            inp_counter+=1 # Move input counter
            pos+=2 # Move instruction pointer
        elif opcode == 4: # Output
#             print('Output:')
#             print([instruction[instruction[pos+1]] if param_mode[0]==0 else instruction[pos+1]][0])
            outputs.append(get_param(instruction,[param_mode[0]],pos,rel_base)[0])
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
            print(opcode,noun,verb,pos)
            input()
            return []
           
        exec_instr+=1
        opcode = str(instruction[pos])
            
        
#     outputs.append(instruction[0])
    return outputs
# Read input
with open('dec9_input.txt','r') as fin:
# with open('example.txt','r') as fin:
    data = [int(y) for x in fin.read().splitlines() for y in x.split(',')]

# Cast data to dictionary
data_dict = dict(zip(range(len(data)),data))

# Runt part 1, diagnostics
out = intcode(data_dict.copy(),data_dict[1],data_dict[2],[1])

print(out)


# Run part 2 
out = intcode(data_dict.copy(),data_dict[1],data_dict[2],[2])

print(out)