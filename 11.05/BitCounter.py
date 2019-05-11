    # First Version :)
        # def countBits(n):
        #     result = 0
        #     binNum = bin(n)
        #     for x in binNum :
        #         if x == "1" :
        #             result += 1
        #     return result


def countBits(n):
    return bin(n).count("1")


# Check def

print(countBits(11))
