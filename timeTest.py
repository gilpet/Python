if __name__ == '__main__':
    import time
    normal_time = 0
    list_comp_time = 0
    def runFuncs():
        global normal_time
        global list_comp_time
        def fizzNormal():
            global normal_time
            start = time.time()
            for num in range(1,100):
                if num%3==0 and num%5==0:
                    print("FizzBuzz")
                elif num%3==0:
                    print("Fizz")
                elif num%5==0:
                    print("Buzz")
                else:
                    print(num)
            end = time.time()
            normal_time = (end - start)
        def fizzListComp():
            global list_comp_time
            start = time.time()
            print(*['fizzbuzz' if num%3==0 and num%5==0 else 'fizz' if num%3==0 else 'buzz' if num%5==0 else num for num in range(1,100)], sep='\n')
            end = time.time()
            list_comp_time = (end - start)
        fizzNormal()
        fizzListComp()
        print('Normal for loop: %.10f'%(normal_time))
        print('Fancy list comprehension: %.10f'%(list_comp_time))
    runFuncs()
