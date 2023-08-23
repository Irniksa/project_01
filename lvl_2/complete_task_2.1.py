# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!
l1 = [4,6,2,1,9,63,-134,566]
l2= [-52, 56, 30, 29, -54, 0, -110]
l3= [42, 54, 65, 87, 0]
l4= [5]
def minimum(arr):
    min_ = arr[0]
    for ele in arr:
        if ele < min_:
            min_ = ele
    return min_
    pass

def maximum(arr):
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
           max_ = ele
    return max_


min = minimum(l1)
max = maximum(l1)
print (f'max ={max}, min= {min}')

min = minimum(l2)
max = maximum(l2)
print (f'max ={max}, min= {min}')

min = minimum(l3)
max = maximum(l3)
print (f'max ={max}, min= {min}')

min = minimum(l4)
max = maximum(l4)
print (f'max ={max}, min= {min}')