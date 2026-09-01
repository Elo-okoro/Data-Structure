import numpy as np 
# from array import array
numbers = np.linspace(0, 9, 10)
print(numbers)
new_array = numbers.copy()
new_array[numbers % 2 != 0] = -1
print(new_array)
new_2d_array = np.vstack((numbers, numbers))
print(new_2d_array)
total  = 0
for i in numbers:
    if i % 2 == 0:
        total += i
print("The Total Is:", total)
