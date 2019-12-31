import math
import timeit
import numpy as np
import scipy.integrate

def decaying_sinx(x):
    return (math.sin(x) * math.exp(-x))


# commented out function runtime timings since I use timeit later

def mc_integration(func,a,b,depth):
    ''' Takes in a function, and an interval
    starting from a and ending at b'''
    #start = time.time()
    # func is a function
    inner,total = 0, 0
    length = b-a
    # need to find max value of function func
    # avoiding zero division error, max
    max = 1
    # (max amplitude is 1)
    for i in range(depth):
        x = np.random.uniform(0, length)
        y = np.random.uniform(0,max)
        if y < func(x):
            inner = inner + 1
        #dont need total, it's just depth
    ratio = inner/depth
    #end = time.time()
    #print("Total elapsed time for monte carlo: " + str(end-start) + " seconds")
    return ratio * max * length

def scipy_integrate(func,a,b):
    #start = time.time()
    solution, error = scipy.integrate.quad(func,a,b)
    #end = time.time()
    #print("Total elapsed time for scipy quadrature: " + str(end-start) +" seconds")
    return solution

print(mc_integration(decaying_sinx,0,5,10000))
print(scipy_integrate(decaying_sinx,0,5))

# Testing the timings between the code

def monte_carlo_time():
    setupcode = '''
from __main__ import mc_integration
from __main__ import decaying_sinx
from random import randint
    '''
    testcode = """
depth = 10000
a = 0
b = 5
mc_integration(decaying_sinx,0,5,10000)

    """
    times = timeit.repeat(setup = setupcode, stmt = testcode, repeat = 3, number = 3)
    avg = np.average(times)
    print("monte carlo timing is: " + str(avg))
def scipy_timing():
    setupcode = '''
from __main__ import scipy_integrate
from __main__ import decaying_sinx
from random import randint
    '''
    testcode = """
depth = 10000
a = 0
b = 5
scipy_integrate(decaying_sinx,a,b)
"""
    times = timeit.repeat(setup = setupcode, stmt = testcode, repeat = 3, number = 3)
    avg = np.average(times)
    print("average scipy timing : " + str(avg))
# FROM THIS WE CONCLUDE THAT MY METHOD IS ABSOLUTELY DESTROYED BY SCIPY's LIBRARY
if __name__ == "__main__":
    monte_carlo_time()
    scipy_timing()
    print("Therefore scipy's quadrature implementation beats mine vastly for" \
    " 1 dimensional integration for a decaying sine wave," \
    " which is what our project dealt with")