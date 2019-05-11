# my version

# def convert(list):
#
#     s = [str(i) for i in list]
#     res = int("".join(s))
#     return(res)
#
# def Descending_Order(num):
#     num = str(num)
#     num = list(num)
#     numbers = []
#     for number in range(len(num)) :
#         number = int(number)
#         numbers.append(int(num[number]))
#
#
#     for num in range(len(numbers)):
#         tmp = numbers[0]
#         inUse = 0
#         for num in range(len(numbers)) :
#             inUse = numbers[num]
#             if tmp > inUse :
#                 numbers[num] = tmp
#                 numbers[num-1] = inUse
#             else :
#                 tmp = inUse
#     numbers = convert(numbers[::-1])
#
#
#
#     return numbers


def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


print(Descending_Order(5741179))
