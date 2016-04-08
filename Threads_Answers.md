#### Name: Sravani Dyawara
#### Date:04/08/2016
#### M20227855

## 1. Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.
Answer: In Thread1.py we are creating two independent threads and made them run independently .They are allowed to access the shared resources without allowing other to control over it.  
In Threads2.py in run(), we are incrementing the sharedcounter to one i.e.,sharedCounter += 1. The interrupter that occured first will have the current value and calculates new value and assigns that value to variable.In this process if one thread gets control on other then there is a chance of change of value.

## 2. After running Thread3.py does it fix the problems that occured in Threads2.py? What's the down-side?
Answer: yes, it does fix the problem. In Threads2.py their is no synchronization between the threads whereas in Threadspy.3 we have fixed the problem of synchronization using Lock().A lock can be held by a single thread at a time or no thread.Sharedcounter in Threads3.py is being blocked by each thread using lock.acquire() and lock.release().the down-side is the run time of the program, Using locks() in Threads3.py causes the more overhead that means it increases the program runtime.

## 3. Comment out the join statements at the bottom of the program and describe what happens.
Answer: When we comment out the join statements in Threads3.py the statements below gets executed and doesn,t wait for any other process to complete. Whereas if we don't comment the join statements in Threads3.py then it will wait for a process to complete after that the statements gets executed.

## 4. What happens if you try to Ctrl-C out of the program before it terminates?
Answer: If we try to ctrl-c out of the program it throws a keyboardInterrupt and terminates the main program but the threads that are created will run until its given range. 

## 5. Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.
Answer: 
            
            sharedNumber = 1
            
            if sharedNumber != 1:
            
                print ("A: that was weird")

The lock has been called on both resources and as program executes sharedNumber will never be 1.Same things happen for thread B.It always prints "A:that was weird" and B:that was weird.

## 6. Does uncommenting the lock operations clear up the problem in question 5?
Answer: Yes, it clear up the problem by locking the resource for each thread. And then it should check the codition that sharedNumber is =1 and sharednumber=2 for thread A&B without having control on each other.These does not cause any bizarre behavior and does not create any race conditions. 
