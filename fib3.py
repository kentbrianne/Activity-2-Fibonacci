import time
import matplotlib.pyplot as plt


terms = []
timer = []


def for_better1():

	tStart1 = time.time()

	term1 = 10
	terms.append(term1)
	x = 0
	y = 1
	counter = 0

	while counter < term1:
		print(x)
		z = x + y
		x = y
		y = z
		counter = counter + 1


	tEnd1 = time.time()
	runTime1 = tEnd1 - tStart1
	print(runTime1)

	timer.append(runTime1)


for_better1()

def for_better2():

	tStart2 = time.time()

	term2 = 20
	terms.append(term2)
	x = 0
	y = 1
	counter = 0

	while counter < term2:
		print(x)
		z = x + y
		x = y
		y = z
		counter = counter + 1


	tEnd2 = time.time()
	runTime2 = tEnd2 - tStart2
	print(runTime2)

	timer.append(runTime2)


for_better2()

def for_better3():

	tStart3 = time.time()

	term3 = 30
	terms.append(term3)
	x = 0
	y = 1
	counter = 0

	while counter < term3:
		print(x)
		z = x + y
		x = y
		y = z
		counter = counter + 1


	tEnd3 = time.time()
	runTime3 = tEnd3 - tStart3
	print(runTime3)

	timer.append(runTime3)


for_better3()

plt.plot(terms,timer, 'yo')
plt.xlabel('Terms')
plt.ylabel('Runtime')
plt.axis([0, 35, 0, 0.1])
plt.title("Fibonacci Iteration")
plt.show()