    # My version
        # def disemvowel(string):
        #     vowels = ["a", "e", "i", "o", "u", "y"]
        #     newString = ""
        #     i = 0
        #
        #     for x in range(1,len(string) +1) :
        #
        #         if  string[i].lower() not in vowels :
        #             newString += string[i]
        #
        #         i+=1
        #
        #     return newString
        #
        # print(disemvowel("we Look at"))
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")



print(disemvowel("we Look at"))
