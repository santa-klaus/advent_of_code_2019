# December 1
# Read input for part 1
with open('dec1_input.txt','r') as fin:
    data = list(map(int, fin.read().splitlines()))


# Calculate part 1
fuel_need = list(x//3-2 for x in data)
total_fuel_need = sum(fuel_need)

print("Answer part 1:")
print(total_fuel_need)


# Part 2
additional_fuel = list(x//3-2 for x in fuel_need)
fuel_need = [sum(pair) for pair in zip([max(x,0) for x in additional_fuel],fuel_need)]

while any(x > 0 for x in additional_fuel):
    additional_fuel =  list(x//3-2 for x in additional_fuel)
    fuel_need = [sum(pair) for pair in zip([max(x,0) for x in additional_fuel],fuel_need)]

total_fuel_need = sum(fuel_need)
print("Answer part 2:")
print(total_fuel_need)