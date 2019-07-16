import random
import statistics
import math
try:    
    a=int(input("Enter first number : "))
    b=int(

    input("Enter second number : "))
    if (a<b):    
        c=int(random.randrange(a, b, 1))
        print(c)
        if(c%2==0):
                print("heads")

        else:
                print("tails")
    else:
        print ("The first number needs to be larger than the second number")
            
            
            #THIS IS THE STATISITICS SECTION
    l=[]
    m=[5,5,1,1,2,2,5] 
    for j in range(c):
        l.append(random.randrange(a, b, 1))
    print('Randomised list is: ',l)
    print ("Average of all the values in the list is: ", statistics.mean(l))
    print ("Rounded off to the nearest full number:", math.ceil(statistics.mean(l)))
    print ("Median value is: ", statistics.median(l)) 
    print ("Modal value is: ", statistics.mode(m)) 
except:
    print("radu nakos baala")   

