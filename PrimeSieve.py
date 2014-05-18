#PrimeSieve.py
#@author: Baron Daugherty
#uses a sieve method to find the primes between 2 and a specified n
#includes stats to track how long the sieve ran

#imports for stats
import cProfile, pstats, io

#main asks us for a number n and builds a list of all numbers 2 to n, inclusive, and passes it to our sieve
def main():
	#create the stat profile and prime list
    pr = cProfile.Profile();
    primes = []
	
	#get n
    num = int(input("Find all primes between 2 and: "))
	
	#fill the list
    for i in range(2, num+1):
        primes.append(i)

	#begin tracking and call sieve on the list, end tracking when done
    pr.enable()
    primes = sieve(primes)
    pr.disable()
	
	#organize and create the stat output
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
	
	#output the new primes list and stats
    print(primes)
    print("Stats:", s.getvalue())

#sieve takes the list and iterates through its members, removing non-primes
def sieve(primes):
    count = 0;  #iterator
	
	#loop through only the part of the list from the last found prime to the end, removing multiples of the current prime
    while count < len(primes):
        mult = primes[count]
        for i in primes[count+1:]:
            if i % mult == 0:
                primes.remove(i)
        count+=1

    return primes

#start the program
main();
