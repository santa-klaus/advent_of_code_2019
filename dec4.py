# # December 4
import time
T1 = time.time()

import numpy as np

# Import input
with open('dec4_input.txt','r') as fin:
    lower_limit,upper_limit = fin.read().split('-')

# Initialise password counters to 0
pw_counter = 0
pw_counter2 = 0

# Loop through all numbers which  fulfill the "no decreasing digits" rule
for k1 in range(int(lower_limit[0]),int(upper_limit[0])+1):
    for k2 in range(k1,10):
        for k3 in range(k2,10):
            for k4 in range(k3,10):
                for k5 in range(k4,10):
                    for k6 in range(k5,10):
                        # compute the number and the diff of its digits
                        num = k1*1e5+k2*1e4+k3*1e3+k4*1e2+k5*1e1+k6
                        num_diff = np.diff([k1,k2,k3,k4,k5,k6])
                        # stop the loop if the upper limit is reached
                        if num>=int(upper_limit):
                            continue 
                        # If the number is above the lower limit and contains at least a double digit
                        elif num>int(lower_limit) and 0 in num_diff:
                            # increment pw counter part 1
                            pw_counter+=1
                            
                            # Convert the diff result to a string and count the zeros (adjacent equal numbers)
                            diff_string=''.join([str(x) for x in num_diff])
                            zeros = diff_string.count('0')
                            
                            # Check if there is any pair of equal numbers that is not adjacent to one more and increment pw counter part 2
                            if zeros < 5 and zeros > diff_string.count('000')*3 and zeros > diff_string.count('00')*2:
                                pw_counter2+=1

print('Possible passwords part 1:')
print(pw_counter) 
print('Possible passwords part 2:')      
print(pw_counter2)     

print('Execution time:')
print(time.time()-T1)
