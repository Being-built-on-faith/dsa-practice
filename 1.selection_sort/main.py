my_array = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(my_array)
for i in range(n-1):
    min_index = i          
    for j in range(i+1, n):
        if my_array[j]< my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)
if __name__ == "__main__":        
    print(f"sorted array: {my_array}")
    
    
# class SelectionSorter:
#     def __init__(self, input_array):
#         self.array = input_array

#     def sort(self):
#         array_length = len(self.array)

#         for current_index in range(array_length - 1):
#             minimum_index = current_index

#             for search_index in range(current_index + 1, array_length):
#                 if self.array[search_index] < self.array[minimum_index]:
#                     minimum_index = search_index

#             # Swap only once AFTER inner loop
#             self._swap(current_index, minimum_index)

#         return self.array

#     def _swap(self, index_one, index_two):
#         self.array[index_one], self.array[index_two] = (
#             self.array[index_two],
#             self.array[index_one],
#         )


# if __name__ == "__main__":
#     input_array = [64, 34, 25, 5, 22, 11, 90, 12]

#     sorter = SelectionSorter(input_array)
#     sorted_array = sorter.sort()

#     print(f"Sorted array: {sorted_array}")