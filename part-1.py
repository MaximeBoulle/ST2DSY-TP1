"""
TP1 - ST2DSY
Synchornization - Shared Memory Model

Part 1 - Concurrent Access To Shared Memory : Race Problems
"""

import threading
import time
from typing import List


class TP1:
    def __init__(self, i: int = 65) -> None:
        self.i = i  # Shared variable

    @staticmethod
    def threading_operations(funcs: List[callable]) -> None:
        """
        Test the threading function
        """
        threads = [threading.Thread(target=func) for func in funcs]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    def op_direct_increment(self) -> None:
        """
        Operation increment
        """
        self.i = self.i + 1

    def op_direct_decrement(self) -> None:
        """
        Operation decrement
        """
        self.i = self.i - 1

    def op_indirect_increment(self) -> None:
        """
        Operation indirect increment
        """
        reg = self.i
        time.sleep(0.1)
        reg += 1
        self.i = reg

    def op_indirect_decrement(self) -> None:
        """
        Operation indirect decrement
        """
        reg = self.i
        time.sleep(0.1)
        reg -= 1
        self.i = reg


class TP1Exercices(TP1):
    def exo_1(self) -> None:
        """
        Exercice 1

        Create a shared variable 'i' and initialize it to 65;
        Create two tasks T1 and T2;
        T1 increments i (i++) and T2 decrements it (i--);

        Run these two tasks and check whenther the final value is incorrect.

        Pseudocode:
        i = 65 # Shared variable
        T1:
            i = i + 1
        T2:
            i = i - 1
        Parallel execution of T1 and T2

        There, the race condition is not really problematic, because operations (increment & decrement) give the correct result.
        """
        self.threading_operations(
            funcs=[self.op_direct_increment, self.op_direct_decrement]
        )

        print(f"Exercice 1.1 - Final value of i: {self.i}")

    def exo_2(self) -> None:
        """
        Change the previous code (i++ and i--) of the two tasks into the following:

        Reg = i
        sleep(for_some_time)
        Reg++ (or Reg--, depending on the task)
        i = Reg

        Pseudocode:
        i = 65 # Shared variable
        T1:
            reg = i
            sleep(0.1)
            reg = reg + 1
            i = reg
        T2:
            reg = i
            sleep(0.1)
            reg = reg - 1
            i = reg
        Parallel execution of T1 and T2

        In this situation, there will be a problem -> the final value of i will be incorrect.
        Race condition occurs because the value of i is read and written in two different tasks.
        Compared to the previous example, the operation is based on a dirty read of the variable i.
        """
        self.threading_operations(
            funcs=[self.op_indirect_increment, self.op_indirect_decrement]
        )

        print(f"Exercice 1.2 - Final value of i: {self.i}")


if __name__ == "__main__":
    # TP1 - Exo 1.1
    tp1 = TP1Exercices()
    tp1.exo_1()

    # TP1 - Exo 1.2
    tp1 = TP1Exercices()
    tp1.exo_2()
