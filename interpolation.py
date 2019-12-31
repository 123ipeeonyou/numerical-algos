# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:34:38 2019

@author: hs8769
"""
import sympy
import numpy as np
import math
import random



class Interpolation:
    def __init__(self, data_set):
        self.data_set = data_set
        
    #Implementing the Vandermonde matrix to interpolate a data set 
    
    def build_vandermonde_matrix(self):
        '''
        assumes that the data set is in the form of a 
        nested list or np array such as :
        [[1,-1], [3,2], [5,2]]
        '''
        #need to augment the matrix by making the last column 
        #all the y values 
        x_values, y_values = [],[]
        #Isolating all x and y values into their own arrays 
        for i in range(len(self.data_set)):
            x_values = x_values + [self.data_set[i][0]]
            y_values = y_values + [self.data_set[i][1]]
        vander_matrix = []
        #polynomial property of matrix
        for i in x_values:
            vander_matrix.append([i**n for n in range(len(x_values))])
          
        #now we need to append the y values as the last column in this matrix
        #to setup an augmented matrix 
        for i in range(len(y_values)):
            vander_matrix[i].append(y_values[i])
            
        #now we can reduce the matrix
        matrix_length = len(vander_matrix)
        vander_matrix = sympy.Matrix(vander_matrix)
        #returns 2 tuples
        reduced, pivots= vander_matrix.rref()
        if len(pivots)!= matrix_length:
            raise ValueError("The inputted points do not correspond to a function")
        return reduced, matrix_length
        


#Testing vandermonde properties

m = sympy.Matrix([[1,0,0,1],[1,1,1,0], [1,.5,.25,.5]])
x = [[1,0,0,1],[1,1,1,0], [1,.5,.25,.5]]
a = [[0,0],[1,0],[1.5,2],[2,4]]
inter = Interpolation(a)
reduced, s = (inter.build_vandermonde_matrix())
l = list(m.row(0))


def interpolation_function(matrix,x_value):
    # Takes in reduced vandermonde matrix
    # and builds it into a more readable polynomial as a dictionary
    new_dict = {}
    polynomial = 0
    i = 0
    # TO DO
    # ITERATE THROUGH MATRIX AND STORE DATA INTO DICTIONARY
    for i in range(4):
        row = matrix.row(i)
        # visit the last element in each row
        polynomial = row[i] * x_value**i
        i += 1
    return polynomial

print("The interpolation function predicts that the value of " + str(1.5) + " in our function is: " + str(interpolation_function(reduced,1.5)))

#fiddling
'''
a = [[0,0],[1,0],[1.5,2],[2,4]]
x,y = [],[]
c,d = [],[]

for i in range(len(a)):
    x= x + [a[i][0]]
    y = y + [a[i][1]]
for i in x:
    c.append([i**n for n in range(len(x))])
for z in range(len(y)):
    c[z].append(y[z])
print(sympy.Matrix(c).rref())
'''




