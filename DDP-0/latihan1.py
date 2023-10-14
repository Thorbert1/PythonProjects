"""
Buatlah sebuah program yang menerima input integer n
untuk menampilkan bilangan2 ganjil diantara n (inclusive) dan 3n (exclusive)
"""

import time

input_num = int(input("Input a number: "))
"""
start_time = time.time()

n = input_num
while n < 3 * input_num:
    if n % 2 == 1:
        print(n)
    n += 1

end_time = time.time()
print(f"{end_time - start_time:.10f}")
"""
start_time_2 = time.time()
n = input_num
if n % 2 == 0:
    n += 1
for i in range(n, input_num * 3, 2):
    print(i)


end_time_2 = time.time()
print(f"{end_time_2 - start_time_2:.10f}")
