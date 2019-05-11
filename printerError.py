        # My solution

            # def printer_error(s):
            #
            #   ind = 0
            #   for x in s :
            #       if x  in "nopqrstuvwxyz" :
            #           ind = ind + 1
            #   aou = f"{ind}/{len(s)}"
            #   return aou

#  solution from codewars , learn how work re :)
from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))
