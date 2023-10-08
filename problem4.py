import time

def first_method(thickness, times):
    start_time = time.time()
    r = ((thickness * (2 ** times))/1000)
    elapsed = time.time() - start_time
    return r, elapsed

def second_method(thickness, times):
    start_time = time.time()
    a = 1
    for i in range(0, times):
        a = 2 * a
    r = (thickness*a)/1000
    elapsed = time.time()-start_time
    return r, elapsed


thickness = float(input("Insert the thickness of the paper to be folded: "))
times = int(input("how many times should the paper to be folded?: "))

result_method1, elapsed1 = first_method(thickness, times)
result_method2, elapsed2 = second_method(thickness, times)

print(f'''
*The first method(problem2) gave the following result {result_method1}, with
 in the following time {elapsed1}
*The second method(problem3) gave the following result {result_method2}, with
 in the following time {elapsed2}

''')

