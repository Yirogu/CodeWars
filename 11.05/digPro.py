#        Noobie version
        # def dig_pow(n, p):
        #     k = 0
        #     result= 0
        #     Nstring = str(n)
        #     for x in Nstring:
        #         result += int(x)**(p)
        #         p += 1
        #     k = result / n
        #     if not k % 1 != 0:
        #         return k
        #     else :
        #         return -1
        # 

 #  version from codevars
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1


print(dig_pow(695,2))
