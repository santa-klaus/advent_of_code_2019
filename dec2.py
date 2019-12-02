# # December 2
# Read input
with open('dec2_input.txt','r') as fin:
    data = [int(y) for x in fin.read().splitlines() for y in x.split(',')]

# Define intcode program
def intcode(instruction,noun,verb):
    instruction[1:3] = [noun,verb]
    pos = 0
    opcode = instruction[pos]
    
    while opcode != 99:
        if opcode == 1: # Addition
            instruction[instruction[pos+3]] = instruction[instruction[pos+1]] + instruction[instruction[pos+2]]
            pos = pos + 4 # Move instruction pointer
        elif opcode == 2: # Multiplication
            instruction[instruction[pos+3]] = instruction[instruction[pos+1]] * instruction[instruction[pos+2]]
            pos = pos + 4 # Move instruction pointer
        else:
            print("Invalid opcode: ")
            print(opcode,noun,verb,pos)
            input()
            return []
             
        opcode = instruction[pos]
        
    return instruction[0]

# Part 1
# Permute program input following instructions
noun,verb = 12,2

result = intcode(data.copy(),noun,verb)
print(result)


# Part 2
print("Part 2")
des_out = 19690720
# Brute force approach
for x in range(len(data)):
    for y in range(len(data)):
        result = intcode(data.copy(),x,y)
        if result == des_out:
            print(x*100+y)
            quit()       
        
print(data)




## Running backward approach (not working)
# print("Input desired program output:")
# data[0] = int(input())
# data[0] = 19690720
# 
# # find position of all 99 and determine if they are in an opcode position (assuming always steps of 4)
# eop_pos = [i for i,x in enumerate(data) if x==99]
# eop_pos = [x for x in eop_pos if (x)%4==0]
# 
# # Start program 4 positions before the first opcode 99 in an opcode position
# pos = eop_pos[0] - 4
# 
# 
# while pos!=0:
#     opcode = data[pos]
#     if opcode == 1: # Addition
#         data[data[pos+3]] = data[data[pos+1]] + data[data[pos+2]]
#         pos = pos - 4 # Move instruction pointer
#     elif opcode == 2: # Multiplication
#         data[data[pos+3]] = data[data[pos+1]] * data[data[pos+2]]
#         pos = pos - 4 # Move instruction pointer
#     else:
#         print("Invalid opcode: ")
#         print(opcode)
#          
#     opcode = data[pos]
#     
# print(data)


