def second_max(lst):
    max_value = max(lst)
    second_max_value = float('-inf')
    for i in range(len(lst)):
        if lst[i] > second_max_value and lst[i] != max_value:
            second_max_value = lst[i]
    return second_max_value

list_num = int(input())
input_numbers = input()
my_list = input_numbers.split()
numbers_list = [int(num) for num in my_list]  # convert strings to integers
#print("Input numbers:", numbers_list)
second_max_value = second_max(numbers_list)
print( second_max_value)
