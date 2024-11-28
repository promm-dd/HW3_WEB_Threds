import time
from multiprocessing import Pool, cpu_count
def factorize_single(number):#вычисл делители для числа 
    return [i for i in range(1, number+1) if number % i ==0]#возвр список чисел на которые заданное число делится без остатка 
def factorize_sync(*numbers): #синхро версия 
    return [factorize_single(number) for number in numbers]# перебир числа из numbers
def factorize_parallel (*numbers): #созд пул процессов с числом воркеров равным кол-ву ядер процессора cpu_count
    with Pool(cpu_count()) as pool: 
       results= pool.map(factorize_single, numbers) #вызывает функцию / это метод пула процесов котор применяет функцию ко всем элементам 
    return results
   
if __name__ == '__main__':
    #синхрон
    numbers= (128, 255, 99999, 10651060)
    start_time = time.time()
    result_sync = factorize_sync(*numbers)
    end_time= time.time() 
    #параллельн 
    start_parall = time.time()
    result_parall = factorize_parallel(*numbers)
    end_parall= time.time() 
    
    
    
    a, b, c, d  = result_sync
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


    print("Синхронная версия:")
    print(f"Время выполнения: {end_time - start_time:.4f} секунд")
    print(f"Результаты: {result_sync}")

    print("\nПараллельная версия:")
    print(f"Время выполнения: {end_parall - end_parall:.4f} секунд")
    print(f"Результаты: {result_parall}")


#     results=[]
#     for number in numbers:
#         fact= [i for i in range(1, number+1) if number % i ==0]#
#         results.append(fact)
#     return results