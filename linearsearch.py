# numbers = [11,22,33,44,55,66,77,88,99]
# # key_value = 88
# # found = False

# # for i in numbers:
# #     if numbers[i] == key_value:
# #         found = True
# #         break

# # if found is True:
# #     print(f"element {key_value} found")
# # else:
# #     print(f"element {key_value} not found")

# def binary_search(numbers, key_value):
#     start_index = 0
#     end_index = len(numbers)-1

#     while start_index <= end_index:
#         mid = (start_index+end_index) // 2
#         mid_value  = numbers[mid]

#         if mid_value == key_value:
#             return mid
        
#         elif key_value > mid_value:
#             start_index = mid + 1

#         elif key_value < mid_value:
#             end_index = mid - 1

#     return -1        

# key_value = 88
# print(f"element {key_value} found at pos {binary_search(numbers,key_value)}")

# def binary_search_recursive(numbers, key_value, start_index, end_index):
#     # Base case: not found
#     if start_index > end_index:
#         return -1

#     mid = (start_index + end_index) // 2
#     mid_value = numbers[mid]

#     if mid_value == key_value:
#         return mid
#     elif key_value > mid_value:
#         return binary_search_recursive(numbers, key_value, mid + 1, end_index)
#     else:
#         return binary_search_recursive(numbers, key_value, start_index, mid - 1)

# # Example usage:
# numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]
# key_value = 88
# position = binary_search_recursive(numbers, key_value, 0, len(numbers) - 1)

# if position != -1:
#     print(f"element {key_value} found at pos {position}")
# else:
#     print(f"element {key_value} not found")
