#Recursive solution for N-Queens problem in Python
from math import *
import sys
import time
"""
This program is used to calculate the solutions to the n queen problem where n can be changed.

count: Counts the number of solutions
x : An array that will hold the placements of queens
n: The number of queens to place on the board. Also acts as the board's side length
first: A boolean to check the first time a solution is found
first_time: the CPU time to find the first solution
"""
count = 0
x = {}
n = 9
first = "true"
first_time = 0;

"""
This function is used to build the matrix of zeros and one and prints it out to the console
Takes an input of board size and where to place the queen.
"""
def matrix_build(val, n):
    zeros = 0
    while zeros < (val-1):
        print '{:4}'.format(0),
        zeros += 1
    print '{:4}'.format(1),
    while zeros < (n-1):
        print '{:4}'.format(0),
        zeros += 1
    print

"""
This function is used to place a queen. It checks if the current is position is vaild,
and if so places the queen.

"""
def place(k, i):
    if (i in x.values()):
        return False
    j = 1
    while(j < k):
        if abs(x[j]-i) == abs(j-k):
            return False
        j+=1
    return True
"""
This function is used to clean out all the placed queens if the previous path
would not of resulted in a solution. Takes the number of vaildly placed queens
as input.

"""
def clear_future_blocks(k):
    for i in range(k,n+1):
       x[i]=None

"""
This function is used to calculate the solution when n queens are placed.
It also tracks the time until the first queen is placed.
"""
def NQueens(k):
    for i in range(1, n + 1):
        clear_future_blocks(k)
        if place(k, i):
            x[k] = i
            if (k==n):
                global count
                global first
                global first_time
                if first:
                    first = "false"
                    first_time = time.clock()
                count += 1
                for j in x:
                    a = x.__getitem__(j)
                    matrix_build(a, n)
                print '---------'

            else:
                NQueens(k+1)



start_time = time.clock()
NQueens(1)
print count, "solutions."

print "Time till first solution: ", first_time - start_time, "seconds."
print "Total CPU Time:", time.clock() - start_time, "seconds."

