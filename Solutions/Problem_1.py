'''
Name:			Multiples of 3 and 5

Description:	If we list all the natural numbers below 10 that are multiples of 3 or 5, 
 				we get 3, 5, 6 and 9. The sum of these multiples is 23.
				Find the sum of all the multiples of 3 or 5 below 1000.

Answer:			233168
'''

def sumMultiplesThreeAndFive(num_below):
	return sum(i for i in range(num_below) if i % 3 == 0 or i % 5 == 0)

print("Sum: {}".format(sumMultiplesThreeAndFive(1000)))