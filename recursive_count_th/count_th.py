'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur
within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # TBC
    # count = 0
    # this is working
    # for i in range(len(word)):
    #     if word[i] == "t" and word[i+1] == "h":
    #         count += 1
    # return count

    return count_th_in_word(word)


def count_th_in_word(word, char=0):
    if not word:
        return char
    elif word[0:2] == 'th':
        char += 1
        # get all but not the first 2 char using a slice
        return count_th_in_word(word[2:], char)
    else:

        return count_th_in_word(word[1:], char)


print(count_th("ththth"))
