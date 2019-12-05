# December 5
import numpy as np
# Define intcode program
def intcode(instruction,noun,verb):
    # Permute instructions according to noun and verb
    instruction[1:3] = [noun,verb]
    
    # Start at first instruction           
    pos = 0
    # Initialize with first opcode
    opcode = str(instruction[pos])
    
    # loop through instructions
    while opcode != '99':
        
        # parse opcode
        if len(opcode)<=2:
            param_mode = [0,0]
            opcode = int(opcode)
            
        elif len(opcode) == 3:
            param_mode = [int(opcode[0]),0]
            opcode = int(opcode[-2:])
            
        elif len(opcode) == 4:
            param_mode = [int(opcode[1]),int(opcode[0])]
            opcode = int(opcode[-2:])
        else:
            print('Undefined opcode length')
            print(len(opcode))
        
        
        if opcode == 1: # Addition
            instruction[instruction[pos+3]] = sum([instruction[instruction[pos+1+x]] if param_mode[x]==0 else instruction[pos+1+x] for x in range(2)])
            pos+=4 # Move instruction pointer
        elif opcode == 2: # Multiplication
            instruction[instruction[pos+3]] = np.prod([instruction[instruction[pos+1+x]] if param_mode[x]==0 else instruction[pos+1+x] for x in range(2)])
            pos+=4 # Move instruction pointer
        elif opcode == 3: # Input
            print('Enter input:')
            instruction[instruction[pos+1]] = int(input())
            pos+=2 # Move instruction pointer
        elif opcode == 4: # Output
            print('Output:')
            print([instruction[instruction[pos+1]] if param_mode[0]==0 else instruction[pos+1]][0])
            pos+=2 # Move instruction pointer
        elif opcode == 5 or opcode == 6: # Jump if true/false
            if (opcode==5 and [instruction[instruction[pos+1]] if param_mode[0]==0 else instruction[pos+1]][0]) or (opcode==6 and not [instruction[instruction[pos+1]] if param_mode[0]==0 else instruction[pos+1]][0]):
                pos = [instruction[instruction[pos+2]] if param_mode[1]==0 else instruction[pos+2]][0] # Jump instruction pointer
            else:
                pos+=3 # Move instruction pointer
        elif opcode == 7: # Less than
            instruction[instruction[pos+3]] = int([instruction[instruction[pos+1]] if param_mode[0]==0 else instruction[pos+1]][0] < [instruction[instruction[pos+2]] if param_mode[1]==0 else instruction[pos+2]][0])
            pos+=4 # Move instruction pointer
        elif opcode == 8: # Equals
            instruction[instruction[pos+3]] = int([instruction[instruction[pos+1]] if param_mode[0]==0 else instruction[pos+1]][0] == [instruction[instruction[pos+2]] if param_mode[1]==0 else instruction[pos+2]][0])
            pos+=4 # Move instruction pointer
        else:
            print("Invalid opcode: ")
            print(opcode,noun,verb,pos)
            input()
            return []
           
        opcode = str(instruction[pos])
        
    return instruction[0]

# Read input
with open('dec5_input.txt','r') as fin:
    data = [int(y) for x in fin.read().splitlines() for y in x.split(',')]

intcode(data,data[1],data[2])
