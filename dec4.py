# # December 4
import numpy as np
puzzle_input = '272091-815432'

lower_limit,upper_limit = puzzle_input.split('-')

pw_counter = 0
pw_counter2 = 0

for k1 in range(int(lower_limit[0]),int(upper_limit[0])+1):
    for k2 in range(k1,10):
        for k3 in range(k2,10):
            for k4 in range(k3,10):
                for k5 in range(k4,10):
                    for k6 in range(k5,10):
                        num = k1*1e5+k2*1e4+k3*1e3+k4*1e2+k5*1e1+k6
                        num_diff = np.diff([k1,k2,k3,k4,k5,k6])
                        if num>=int(upper_limit):
                            continue 
                        elif num>int(lower_limit) and 0 in num_diff:
                            pw_counter+=1
                            
#                             # Diff the positions of the equal adjacent entries, 1 correponds to more than two adjacent entries
#                             position_diff = np.diff(np.where(num_diff==0)[0])
#                             
#                             if position_diff.size == 0 or len(position_diff) == len(np.where(position_diff==1)[0])+1:
#                                 pw_counter2+=1
#                                 print(num)
                            diff_string=''.join([str(x) for x in num_diff])
                            zeros = diff_string.count('0')
                            
                            if zeros < 5 and zeros > diff_string.count('000')*3 and zeros > diff_string.count('00')*2:
                                print(num)
                                pw_counter2+=1

print(pw_counter)       
print(pw_counter2)     