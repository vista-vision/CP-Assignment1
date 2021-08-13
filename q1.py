#                                                              Sum of 1st N natural numbers and N odd numbers.

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
            print(n)

            #Sum of first N odd natural numbers.
            i=1
            m=1
            j=1
            while j!=p:
                i+=2
                m+=i
                j+=1
            print(m)

            #To iterate for 5 values of N.
            repeat+=1

    except ValueError:
        print("Enter a natural number!")