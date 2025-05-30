import random
import time
import multiprocessing
import threading
import math

class lab:
    def __init__(self):
        #self.imitation()
        self.paralel()

        

    def imitation(self):
        start = time.time()
        for i in range(50):
            a = random.randint(1, 2)
            time.sleep(a)
            print(f'обработанно элементов:', i,'/50', 'времени затрачено:')
        print('обработка завершена')
    

    def paralel(self):
        numbers = list(range(1, 100))  
        with multiprocessing.Pool(processes = 2) as pool:  
            results = pool.map(math.factorial, numbers)
            print(results)

    def __del__(self):

        
        pass

if __name__ == "__main__":
    name = lab()
