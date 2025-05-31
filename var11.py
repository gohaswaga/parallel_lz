import random
import time
import multiprocessing
import math
import asyncio

class Lab:
    def imitation(self):
        start = time.time()
        for i in range(50):
            a = random.randint(1, 2)
            time.sleep(a)
            finish = time.time() 
            difference = finish - start
            print(f'Обработано элементов: {i}/50, времени затрачено:', difference)
        print('Обработка завершена')

    def paralel(self):
        numbers = list(range(1, 500))
        with multiprocessing.Pool(processes=50) as pool:
            results = pool.map(math.factorial, numbers)
            print(f"Результаты факториалов:", results)

    async def problemo(self, numb, timer):
        await asyncio.sleep(timer)
        result = numb - 3
        print(f"Результат: {result}")
        if result == 0:
            raise ZeroDivisionError("Ошибка: результат равен нулю!")
        return result

    async def main(self):
        try:
            await asyncio.gather(self.problemo(3, 2),self.problemo(4, 1))
        except ZeroDivisionError as e:
            print(f'Ошибка:', e)

    def __init__(self):
        self.imitation()
        self.paralel()
        asyncio.run(self.main())

    def __del__(self):

        
        pass
