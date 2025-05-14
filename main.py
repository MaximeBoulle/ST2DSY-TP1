#!/usr/bin/env python3
"""
ST2DSY - TP Synchronization with Shared Memory
"""

import threading

class Semaphores:
    """
    Exercise 2: Synchronizing access using semaphores
    """
    def __init__(self):
        self.i = 65
        self.semaphore = threading.Semaphore(1)

    def increment(self):
        """
        This method increments the value of i while ensuring thread safety.
        It uses a semaphore to control access to the shared resource.
        """
        self.semaphore.acquire()
        self.i += 1
        self.semaphore.release()
        
    def decrement(self):
        """
        This method decrements the value of i while ensuring thread safety.
        It uses a semaphore to control access to the shared resource.
        """
        self.semaphore.acquire()
        self.i -= 1
        self.semaphore.release()

    def runQ1(self):
        threads = []
        
        T1 = threading.Thread(target=self.increment)
        T2 = threading.Thread(target=self.decrement)
        
        threads.append(T1)
        threads.append(T2)
        
        # Start the threads
        for thread in threads:
            thread.start()
            
        # Wait for all threads to finish
        for thread in threads:
            thread.join()
            
        # Print the final value of i
        print(f"Final value of i: {self.i}")
        
    def runQ2(self):
        """
        Creates a deadlock situation using three semaphores and three threads.
        Each thread holds one semaphore and tries to acquire another, forming a circular wait pattern.
        """
        semA = threading.Semaphore(1)
        semB = threading.Semaphore(1)
        semC = threading.Semaphore(1)
        
        def process1():
            semA.acquire()
            print("Process 1: Acquired semaphore A")
            threading.Event().wait(0.5)
            print("Process 1: Trying to acquire semaphore B")
            semB.acquire()
            print("Process 1: Acquired semaphore B")
            semB.release()
            semA.release()
            
        def process2():
            semB.acquire()
            print("Process 2: Acquired semaphore B")
            threading.Event().wait(0.5)
            print("Process 2: Trying to acquire semaphore C")
            semC.acquire() 
            print("Process 2: Acquired semaphore C")
            semC.release()
            semB.release()
            
        def process3():
            semC.acquire()
            print("Process 3: Acquired semaphore C")
            threading.Event().wait(0.5)
            print("Process 3: Trying to acquire semaphore A")
            semA.acquire()  
            print("Process 3: Acquired semaphore A")
            semA.release()
            semC.release()
        
        # Create three threads
        t1 = threading.Thread(target=process1)
        t2 = threading.Thread(target=process2)
        t3 = threading.Thread(target=process3)
        
        # Start the threads
        print("Starting threads that will create a deadlock...")
        t1.start()
        t2.start()
        t3.start()
        
    def runQ3(self):
        """
        Use semaphores to run 3 different applications (firefox, emacs, vi) in a predefined sequence 
        no matter in which order they are launched.        
        """
        
        
        
def main():
    """
    Main function to run the exercises.
    """
    choice = input("Choose an exercise to run (1-5) or 'all': ")
    
    if choice == '1' or choice == 'all':
        print("\n----- Running Race Problems Part 1 -----")
        # pc = RaceProblems()
        # pc.run()
        
        print("\n----- Running Race Problems Part 2 (with race condition) -----")
        # pc = RaceProblems2()
        # pc.run()

    if choice == '2' or choice == 'all':
        semaphores = Semaphores()

        print("\n----- Running Semaphores Question 1 -----")
        semaphores.runQ1()
        
        print("\n----- Running Semaphores Question 2 -----")
        semaphores.runQ2()
        
        print("\n----- Running Semaphores Question 3 -----")
        semaphores.runQ3()
    
if __name__ == "__main__":
    main()


