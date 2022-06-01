from time import time, sleep
from threading import Thread
import concurrent.futures


def factorize(*number):
    timer = time()
    
    for i in number:
        set_of_output_numbers = []

        for j in range(1, i+1):
            if i % j == 0:
                set_of_output_numbers.append(j)
              
        print(f'Done for {i} number in {time() - timer} seconds.')
        print(f'Numbers are {set_of_output_numbers}')
            
    return set_of_output_numbers  
    raise NotImplementedError()   
    

if __name__ == '__main__':
    set_of_raw_numbers = [128, 255, 99999, 10651060]
    
    for number in set_of_raw_numbers:
        factorize(number)

    print ('')
    print ('waiting...threads will start')
    print ('')    
    sleep(6)
    
    for number in set_of_raw_numbers:
        thread = Thread(target=factorize, args=(number, ))
        thread.start()
        thread.join()
    
    print ('')
    print ('waiting...processes will start')
    print ('')
    sleep(6)

    with concurrent.futures.ProcessPoolExecutor(2) as executor:
        executor.map(factorize, set_of_raw_numbers)
        
