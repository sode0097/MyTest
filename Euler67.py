'''
From http://projecteuler.net/problem=67

Problem Statement: By starting at the top of the triangle below 
and moving to adjacent numbers on the row below, the maximum 
total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt 
(right click and 'Save Link/Target As...'), a 15K text file 
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. 
It is not possible to try every route to solve this problem, 
as there are 299 altogether! If you could check one trillion 
(1012) routes every second it would take over twenty billion 
years to check them all. There is an efficient algorithm to 
solve it. ;o)

EXAMPLE: >>> get_max_sum('triangle.txt')



Author: Erin Soderberg
Date: March 23, 2014
'''

def get_max_sum(filename = '../../small_triangle.txt', num_rows = 15, num_entries = 105):
    '''
    SUMMARY: get_max_sum() takes a txt file containing 
    integers as input and finds the path from top to bottom
    through the triangle with the maximum sum
	
    INPUT: a .txt file containing integers
	
    OUTPUT: an integer, the value of the maximum path
    through the triangle
    '''

    f = open(filename, 'r')
    input_string = f.read()
    string_list = input_string.split()
    f.close()
    print(string_list)
    print(len(string_list))

    triangle = []
    counter = 0
    for n in range(num_rows):
        row_list = []
        for j in range(n+1):
            row_list.append(int(string_list[counter]))
            counter += 1
        triangle.append(row_list)

    for i in reversed(range(num_rows-1)):
        for j in range(len(triangle[i])):
            val_to_change = triangle[i][j]
            val1 = triangle[i+1][j]
            val2 = triangle[i+1][j+1]
            triangle[i][j] = (val_to_change + val1) if (val1 > val2) else (val_to_change + val2)
			
    return triangle[0][0]
		






    
