# First version
    # import math
    # def is_square(n):
    #   n = int(n)
    #   if n < 0 :
    #     print(f"{n}: Negative numbers cannot be square numbers")
    #     return False
    #   if n == 0 :
    #     print(f"{n} is a square number")
    #     return True
    #   sqrtly = math.sqrt(n)
    #   temporary = str(sqrtly)
    #   intSqrt = int(sqrtly)
    #   if f"{intSqrt}.0" in temporary :
    #       if len(str(sqrtly)) == len(str(intSqrt))+2 :
    #           print(f"{sqrtly} Da sie ulozyc kwadrat")
    #           return True
    #
    #   return False
    #

#   version for codewars
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;
