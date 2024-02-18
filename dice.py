import random
import sys

sys.setrecursionlimit(10000)

A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3, 4, 5, 6]
combinations = []
probability_distribution = {}
distribution = {}
new_combinations = []
New_Die_A=[]
New_Die_B=[]

for i in A:
    for j in B:
        combinations.append([i,j])
        
print("")
print("Distribution of combination:")
print(combinations) #answer for Part-A Q2

def total_combinations():
    num_outcomes_per_die = 6
     
    total_combinations = num_outcomes_per_die ** 2
    
    #Since two dies are rolled, each die has 6 sides, all 6 sides of a die is in a
    #combination with all 6 sides of the other die, 6 is multiplied by 6 (i.e, 6 multiplied by  the number of dice
    print("")
    print("Number of possible combinations:")
    print(total_combinations) #answer for Part-A Q1

def probability():
    for i in combinations:
        total = 0
        for j in i:
            total += j
        if total in probability_distribution:
            probability_distribution[total] += 1
        else:
            probability_distribution[total] = 1
    for key,value in probability_distribution.items():
        distribution[key]=value/36
    print("")
    print("Probability of possible sums from combinations:")
    print(distribution) #answer for Part-A Q3

def generate_arrays(frequency, max_value_A, array_length):
    array_A = []

    while len(array_A) < array_length:
        random_value = random.randint(1, max_value_A) #change in case of error
        array_A.append(random_value)

    array_B = []

    while len(array_B) < array_length:
        random_value = random.randint(1, 12-max_value_A)
        if random_value not in array_B:
            array_B.append(random_value)

    if max(array_A) + max(array_B) > 12: #change in case of error
        return generate_arrays(frequency, max_value_A, array_length)

    frequency_calculated = {}
    for i in array_A:
        for j in array_B:
            total = i+j
            if total in frequency_calculated:
                frequency_calculated[total] += 1
            else:
                frequency_calculated[total] = 1
                
    if frequency_calculated == frequency:
        return array_A,array_B
    else:
        return generate_arrays(frequency, max_value_A, array_length)
                
def undoom_dice(C,D):
    max_value_A = 4

    max_sides = 6

    New_Die_A, New_Die_B = generate_arrays(probability_distribution, max_value_A, max_sides)

    print("")
    print("New_Die_A:", New_Die_A)
    print("New_Die_B:", New_Die_B)
                    
total_combinations()
probability()
undoom_dice(A,B)
