import random

def restaurant_sort(list, start, end, comparison_function):
  if start >= end:
    return
  pivot_ind = random.randrange(start, end + 1)
  pivot_element = list[pivot_ind]
  list[end], list[pivot_ind] = list[pivot_ind], list[end]
  less_than_pointer = start
  for i in range(start, end):
    if comparison_function(pivot_element,list[i]):
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  restaurant_sort(list, start, less_than_pointer - 1, comparison_function)
  restaurant_sort(list, less_than_pointer + 1, end, comparison_function)