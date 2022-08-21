'''This script is used to give product of two integers using the Karatsuba Algorithm
   Nishu Choudhary'''


#Import Required Packages
import math

#Ask user for inputting two integers
def user_input():
    try:
        a, b = input("Enter two integers, x and y: ").split()
        a ,b = int(a), int(b)
        return a, b
    except ValueError:
        print("Entered inputs aren't integers")
        return(user_input())

def karatsuba(g,h):
    #Base case for recursion call
    if len(str(g)) == 1 or len(str(h))== 1:
        return g*h
    else:
        n_g = len(str(g))
        n_h = len(str(h))
        t = max(n_g, n_h) // 2

        k, l = g // pow(10, t), g % pow(10, t)
        m, n = h // pow(10, t), h % pow(10, t)

        term_1 = karatsuba(k,m)
        term_3 = karatsuba(l,n)
        #This step reduces the number of recursive calls from 4 to 3
        term_2_0 = karatsuba(k+l,m+n)
        term_2 = term_2_0 - term_1 - term_3

        return pow(10,2*t)*term_1 + pow(10,t)*term_2 + term_3

x,y = user_input()
print(karatsuba(x,y))
