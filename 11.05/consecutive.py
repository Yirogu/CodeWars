# def longest_consec(strarr, k):
#     result = ""
#     if len(strarr) == 0 or int(k) >len(strarr) or int(k) <= 0:
#             return ""
#     strarr.sort(key=len,reverse=True)
#     result = [str(strarr[x]) for x in range(k)]
#     return "".join(result)
def longest_consec(strarr, k):
    result = ""
    if len(strarr) == 0 or int(k) >len(strarr) or int(k) <= 0:
            return ""
    maxElement = max(strarr,key=len)
    postion = int(strarr.index(maxElement)) +1
    # lenStrarr = postion + k  if postion + k <= len(strarr) else postion + ((postion+k) -len(strarr))
    strarrEnd = postion + ((postion+k) -len(strarr)) + 1
    #             5 + 8 - 7 = 6 (7)
    strarrStart = postion - k
    #             5 - 3 = 2 (3)

    return [strarr[x] for x in range(strarrStart,strarrEnd)]





# print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 1))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz","biega","niedziala","hwdsasdassaddasd"], 3))
# ixoyx3452zzzzzzzzzzzz
# longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2)
# wlwsasphmxxowiaxujylentrklctozmymu
