import sympy as s
import math as m
from sympy import *
'''
Resources
https://www.youtube.com/watch?v=Wr9VOum9Co0&t=431s
https://www.youtube.com/watch?v=yCuVBd4N4nY

'''


'''
SLOPE_FIELDS
The Slope Fields method is qutie picky in its func parameter. No y' because we can assume that is what the function is equal to in the first place and will result in error. "=" are also forbidden
x and y are the only variables you can put in the func. NO CAPS
WARNING- THIS METHOD USES EVAL giving it a high chance to error if the func parameter is entered wrong. The error messages do NOT directly tell you if you entered in something wrong and will rather explode your console with error messages.
This method uses synmpy to represent the numbers in the matrice. This is convenient to code and saves space. As the basic math module would generate large numbers(space wise) and be a pain to look at(it's also inaccurate).
Fraction must be put in parenthesis and divided DUH
To distribute to go from 2(x + y) you must put a * in between them 2 * (x + Y) Coefficients can't be right next to numbers
Spaces do not matter     Origin is highlighted Green for convenience. 
Sorry about the spacing but I am mad lazy
There may be more functions you can get away with. Read sympy documentation to see what is possible

Ex func prompts
x
x ** 2
sqrt(x) + y
tan(x) + 2 * (sin(y))
E * 2x
cos ** 2(x)
(x - y) * (x + y)
x ** x ** x

Have Fun
'''
def slope_field(x_min, x_max, y_min, y_max, func):
    '''Plots y' at integer values. Prints matrice'''
    x_min -= 1
    y_min -= 1
    s.expand(func)
   
    graph = [[0 for x in range(x_max - x_min)] for y in range(y_max - y_min)] 
   
    y = y_max
    x = x_min
    for i in range (y_max - y_min):
        x = x_min
        
        for j in range (x_max - x_min):
            x = x + 1
           
            try:
               graph[i][j] = eval(func)
            except ZeroDivisionError:
                graph[i][j] = s.oo
            
           
            if(x == 0 or y == 0):
                print("\u001b[32m[", graph[i][j], end="]\u001b[37m  ")
            else:
                print("[", graph[i][j], end="] ")

        print("\n")
        y = y - 1
    






#------------------------------------------------------------------------------------------------------------------- NOT PART OF MODULE ONLY TEST
print("\033[2J\033[H")
slope_field(-4, 4, -4, 4, "x + y")
#print(left_rsum(-4, 4, 30, "4*x + 2"))
   
    
