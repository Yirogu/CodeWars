# My version

# def binary_array_to_number(arr):
#     result = 0
#     arr = arr[::-1]
#     for x in range(len(arr)) :
#
#         print(arr[x])
#         if arr[x] == 1 :
#             result = result + (2 ** x)
#     return result
# #
 # best codewars version wow xD,sprawdzic jak to dokladnie dziala

def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)
