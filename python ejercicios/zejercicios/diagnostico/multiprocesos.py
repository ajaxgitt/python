from multiprocessing import Process, cpu_count
import time

def contador(num):
    count = 0
    while count < num:
        count += 1
        
        
def main():
    
    iniciar = time.perf_counter()
    
    a = Process(target=contador, args=(250000000,) )
    b = Process(target=contador, args=(250000000,) )
    c = Process(target=contador, args=(250000000,) )
    d = Process(target=contador, args=(250000000,) )
    # e = Process(target=contador, args=(166666666,) )
    # f = Process(target=contador, args=(166666666,) )
    
    
    
    a.start()
    b.start()
    c.start()
    d.start()
    # e.start()
    # f.start()
    
    a.join()
    b.join()
    c.join()
    d.join()
    # e.join()
    # f.join()
    
    fin = time.perf_counter()
    
    tiempo = fin - iniciar
    
    print(f'Se tardó {round(tiempo, 2)} segundos en ejecutar')
    print(f'Número de CPUs disponibles: {cpu_count()}')
    
if __name__ == '__main__':
    main()