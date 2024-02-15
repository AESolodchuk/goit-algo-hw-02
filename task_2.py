from collections import deque

examples = ["level", "R A dar", "RaceCar", "GoIT","not palindrome"]

def palindrome_check(word):
    formated_word = word.replace(" ","").lower()
    dr = deque() 

    for char in formated_word:
        dr.extendleft(char)
    
    return formated_word == "".join(dr,)

for example in examples:
    print(palindrome_check(example))
