import time
import matplotlib.pyplot as plt


terms = []
timer = []


def iterate1():

	tStart1 = time.time()

	iterms1 = 10
	terms.append(iterms1)
	
	x = 0
	y = 1
	print(x)
	while(iterms1-2):
		z = x + y
		x,y = y,z
		print(z)
		iterms1 = iterms1 - 1

	tEnd1 = time.time()
	runTime1 = tEnd1 - tStart1
	print(runTime1)

	timer.append(runTime1)


iterate1()


def iterate2():

	tStart2 = time.time()

	iterms2 = 20
	terms.append(iterms2)
	
	x = 0
	y = 1
	print(x)
	while(iterms2-2):
		z = x + y
		x,y = y,z
		print(z)
		iterms2 = iterms2 - 1

	tEnd2 = time.time()
	runTime2 = tEnd2 - tStart2
	print(runTime2)

	timer.append(runTime2)


iterate2()


def iterate3():

	tStart3 = time.time()

	iterms3 = 30
	terms.append(iterms3)
	
	x = 0
	y = 1
	print(x)
	while(iterms3-2):
		z = x + y
		x,y = y,z
		print(z)
		iterms3 = iterms3 - 1

	tEnd3 = time.time()
	runTime3 = tEnd3 - tStart3
	print(runTime3)

	timer.append(runTime3)


iterate3()



plt.plot(terms,timer, 'yo')
plt.xlabel('Terms')
plt.ylabel('Runtime')
plt.axis([0, 35, 0, 0.1])
plt.title("Fibonacci Iteration")
plt.show()