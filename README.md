	                                                            Code Logic

	                                                            PART-A

1. The number of combinations possible is calculated by multiplying the number of sides of one dice by the number of sides in another dice, i.e, 6*6 = 36

2. The distribution of all possible combinations when both dice are rolled together is calculated by taking number of dots in a face of each dice and taking the same in the other dice as pairs. For, 1 dot in Dice A and 2 dots in Dice B is taken as (1,2) is appended to the combinations = [] array for all values in both arrays.

3. Now since we have the dice dots pair in combinations = [] array, we can take the sum of each pair and keep a track of the frequency of each sum using the dictionary probability_distribution = {} and then the probability for each sum is calculated by dividing the frequency of each sum value by 36 and keeping track of probabilities for each sum in the distribution dictionary. (Check the function def probability())

                                                              PART-B

The base logic of the problem that the probabilites of getting the sum (or frequencies of the sum values between two new arrays) between the two new dice should be the same as the probabilites for the regular six-faced dice. This is achieved using the generate_arrays() function which takes the frequency of sums between our old dice, maximum value that is allowed for array A (max_value_A) and the number of sides of dice (array_length).

The function initiates two arrays for checking the condition for the new_dice array_A and array_B. Since any die (Die A and Die B in this case) will contain only 6 faces and not beyond that, we run a for loop 6 times for inserting random values in the arrays representing the two dice, dice A and dice B.

Now using the condition while len(array_A) < array_length, we append random value to the array_A in each iteration using random_value = random.randint(1, max_value_A) within the maximum permissible value max_value_A.

For array B also, we follow same method but random value is defined as random_value = random.randint(1, 12-max_value_A) (or 12 – max(array_A)), since the maximum sum possible between two dice is 12. We also check if a value is not present in array_B to make sure that repetition does not occur.

Now since we have array values for both dice, we take another dictionary for the sum between the values of each array in frequency_calculated. Next step is to compare frequency_calculated with frequencies with frequencies, which is the sum of the values in the old arrays.

If frequency_calculated == frequency, our condition is satisfied and we return the arrays and these can be the values of the new dice.

Else, a new pair of array values for the dice is generate using the recursion function generate_arrays(frequency, max_value_A, array_length) to see if the condition is satisfied for the new array pairs.
  
