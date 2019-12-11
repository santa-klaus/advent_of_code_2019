# December 7
import numpy as np

# Define intcode program
# Accept noun and verb
# Take input as list
# Give output as list
def intcode(instruction,noun,verb,inp):
    # Permute instructions according to noun and verb
    instruction[1:3] = [noun,verb]
    # Count the number of inputs queried
    inp_counter = 0
    # Initialise empty outputs
    outputs = []
    
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
#             print('Enter input:')
#             print(inp[inp_counter])
            instruction[instruction[pos+1]] = inp[inp_counter] # Take input from current input position
            inp_counter+=1 # Move input counter
            pos+=2 # Move instruction pointer
        elif opcode == 4: # Output
#             print('Output:')
#             print([instruction[instruction[pos+1]] if param_mode[0]==0 else instruction[pos+1]][0])
            outputs.append([instruction[instruction[pos+1]] if param_mode[0]==0 else instruction[pos+1]][0])
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
        
#     outputs.append(instruction[0])
    return outputs




num_of_amplifiers = 5 # For loops don't scale!
# Read input
with open('dec7_input.txt','r') as fin:
    data = [int(y) for x in fin.read().splitlines() for y in x.split(',')]
orig_data = data.copy()

# Part1
# phase settings
phase_list = list(range(num_of_amplifiers))
phasors = [0]*num_of_amplifiers
results = []
combis = []
out = [0]*num_of_amplifiers

# UUUUUUUUUUUgly. Rewrite for recursive calls
for k1 in range(len(phase_list)):
    phase_list1 = phase_list.copy()
    phasors[0] = phase_list1.pop(k1)
    out[0] = intcode(data.copy(),data[1],data[2],[phasors[0],0])
    
    for k2 in range(len(phase_list1)):
        phase_list2 = phase_list1.copy()
        phasors[1] = phase_list2.pop(k2)
        out[1] = intcode(data.copy(),data[1],data[2],[phasors[1],out[0][-1]])
        
        for k3 in range(len(phase_list2)):
            phase_list3 = phase_list2.copy()
            phasors[2] = phase_list3.pop(k3)
            out[2] = intcode(data.copy(),data[1],data[2],[phasors[2],out[1][-1]])
            
            for k4 in range(len(phase_list3)):
                phase_list4 = phase_list3.copy()
                phasors[3] = phase_list4.pop(k4)
                out[3] = intcode(data.copy(),data[1],data[2],[phasors[3],out[2][-1]])
                
                for k5 in range(len(phase_list4)):
                    phase_list5 = phase_list4.copy()
                    phasors[4] = phase_list5.pop(k5)
                    out[4] = intcode(data.copy(),data[1],data[2],[phasors[4],out[3][-1]])
                
                    results.append(out[4])
                    combis.append(phasors.copy())
    

print(max(results))


# Part 2
