import time
import matplotlib.pyplot as plt


terms = []
timer = []


def recursion1(n):
	
   if n <= 1:
       return n
   else:
       return(recursion1(n-1) + recursion1(n-2))

rterms1 = 10
terms.append(rterms1)

tStart1 = time.time()

for i in range(rterms1):
       print(recursion1(i))

tEnd1 = time.time()

runTime1 = tEnd1 - tStart1
print(runTime1)

timer.append(runTime1)

def recursion2(n):
	
   if n <= 1:
       return n
   else:
       return(recursion2(n-1) + recursion2(n-2))

rterms2 = 20
terms.append(rterms2)

tStart2 = time.time()

for i in range(rterms2):
       print(recursion2(i))

tEnd2 = time.time()

runTime2 = tEnd2 - tStart2
print(runTime2)

timer.append(runTime2)


def recursion3(n):
	
   if n <= 1:
       return n
   else:
       return(recursion3(n-1) + recursion3(n-2))

rterms3 = 30
terms.append(rterms3)

tStart3 = time.time()

for i in range(rterms3):
       print(recursion3(i))

tEnd3 = time.time()

runTime3 = tEnd3 - tStart3
print(runTime3)

timer.append(runTime3)




plt.plot(terms,timer, 'bo')
plt.xlabel('Terms')
plt.ylabel('Runtime')
plt.axis([0, 35, 0, 2.5])
plt.title("Fibonacci Recursion")
plt.show()
