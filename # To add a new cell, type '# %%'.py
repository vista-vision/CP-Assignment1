# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#                                       Q1. Sum of 1st N natural numbers and N odd numbers.

repeat=1

while repeat!=6:    #For 5 different values of N.
    N=input("What natural number would you like to sum up to?")

    try:
        p=int(N)

        if p<=0:
            print("Enter a natural number!")

        else:
            #Sum of first N natural numbers.
            n=1
            i=1
            while i!=p:
                i+=1
                n+=i
            print("The sum of the first "+N+" natural numbers is "+str(n)+".")

            #Sum of first N odd natural numbers.
            i=1
            m=1
            j=1
            while j!=p:
                i+=2
                m+=i
                j+=1
            print("The sum of the first "+str(N)+" odd natural numbers is "+str(m)+".")

            #To iterate for 5 values of N.
            repeat+=1

    except ValueError:
        print("Enter a natural number!")


# %%
#                                                Q2. Sum of N terms of an AP, GP, HP

cd=1.5
cr=0.5

a=input('Please enter the 1st term for the different sequences (AP, GP, HP).')
n=input('How many terms do you want to sum up to?')

try:
    b=float(a)
    p=int(n)

    if p<0:
        print("Please enter a non-negative integer for number of terms.")
    else:
        #A.P.
        total=b
        print(b,end='')
        for i in range(p-1):
            print(' + %s' %(b+cd),end='')
            b=b+cd
            total=total+b
        print(' = %s' %total)

        #G.P.
        b=float(a)
        total=b
        print(a,end='')
        for j in range(p-1):
            print(' + %s' %(b*cr),end='')
            b=b*cr
            total=total+b
        print(' = %s' %total)

        #H.P.
        b=float(a)
        d=float(a)
        total=1/b
        print('1/%s' %d,end='')
        for i in range(p-1):
            print(' + 1/%s' %(d+cd),end='')
            d=d+cd
            b=1/d
            total=total+b
        print(' = %s' %total)

except ValueError:
    print('Enter a real number for the first term and a natural number for the number of terms.')




# %%
#                                                   Q3. Calculate n!

def fact(N):
    fact.var=N
    p=0
    while p!=1:
        try:
            n=int(N)
            if n<0:
                print('Enter a natural number.')
            elif n==0:               
                return 0
            else:
                f=n
                while n-1!=0:
                    f=f*(n-1)
                    n=n-1
                p=1
                return f
        except ValueError:
            print('Enter a natural number.')

q=fact(input('What NATURAL number do you want to find the factorial of?'))

if q==0:
    print('0!=0')
else:
    print('%s! = %s' %(fact.var,q))


# %%
#                                               Q4. sinx and exp x upto 4 accurate decimal places

import math
from matplotlib import pyplot as plot

#Creating Taylor Series
def sin(x,n):
    sine=0
    for e in range(1,n+1):
        sign=((-1)**e)
        #Find the factorial and sum the series:
        sine=sine+((sign)*((x**((2*e)+1))/(fact((2*e)+1))))
    return sine

def exp(x,n):
    exp=0
    for e in range(n):
        #Convert degree input to radian:
        pi=math.pi
        #Find the factorial and sum the series:
        exp=exp+((x**e)/fact(e))
    return exp

#Using python functions for accurate values
def accurate_sine(x):
    asin=math.sin(x)
    return asin
def accurate_exp(x):
    aexp=math.exp(x)
    return aexp

#Errors
def error_sine(x,n):
    error=abs(accurate_sine(x)-sin(x,n))
    return error
def error_exp(x,n):
    error=abs(accurate_exp(x)-exp(x,n))
    return error

#Plot
def plot_sin(x,precision):

    Error_Modulus=[]
    Num_Terms=[]

    #Convert degree input to radian.
    pi=math.pi
    r=x*(pi/180)

    k=1
    while error_sine(r,k)>precision:
        Num_Terms.append(k)
        Error_Modulus.append(error_sine(x,k))     
        k+=1
    
    plot.plot(Num_Terms,Error_Modulus, 'bo')
    plot.grid(color='r',ls='--',lw=0.5)
    plot.xlabel('Number of terms')
    plot.ylabel('Modulus of error')
    plot.axis([0,20,0,x/2])
    plot.title('Sine function - Modulus of error vs. number of terms considered from Taylor series expansion')
    plot.show()

plot_sin(0.2,10**(-1))

'''
def plot_exp(x,precision):

    Err_Mod=[]
    Terms_Num=[]

    #Convert degree input to radian.
    pi=math.pi
    r=x*(pi/180)

    k=1
    while error_exp(x,k)>precision:
        Err_Mod.append(error_exp(x,k))
        Terms_Num.append(k)
        k+=1
'''














# %%





# %%
