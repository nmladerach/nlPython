my_origin_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_origin_list)

my_list = [i for i in range(7)]
print(my_list)

my_range = range(8)
print(list(my_range))

my_list = [i for i in range(8)]
print(my_list)

def sum_five(number):
        return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)