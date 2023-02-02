
"""
Print every number between 1 and 100 as follows:  For every multiple of 3 print "Three".
                                                  For every multiple of 5 print "Five".
                                                  And for every multiple of both 3 and 5 print "ThreeFive"
return : None

"""
def exercise_one():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
        elif i % 3 == 0:
            print("Three")
        elif i % 5 == 0:
            print("Five")
        else:
            print(i)
    return None

"""
Determine whether a positive integer number is colorful or not.
param n:(int) a positive number 
return :(bool) <True> if the number is colorful  and <False> if not.
"""

def is_colorful(n):
    # Convert the integer to a string to obtain its digits
    digits = str(n)
    # Create an empty set to store the products
    products = set()
    # Iterate through the digits and subsets of digits
    for i in range(len(digits)):
        for j in range(i, len(digits)):
            subset = [int(d) for d in digits[i:j+1]]
            product = 1
            # Compute the product of the subset
            for num in subset:
                product *= num
            # Check if the product is already in the set
            if product in products:
                return False
            products.add(product)
    return True

"""

Takes a list of strings a returns the sum of the list items that represents an integer (skipping the other items).
param lst:(String) a list of strings.
return :(int or Bool) the result of the calculation.

"""
def calculate(lst):
    if type(lst) != list:
        return False
    total = 0
    for item in lst:
        if type(item) != str:
            pass
        else:
            try:
                num = int(item)
                total += num
            except ValueError:
                # item is not digit
                pass
    return total




"""
Finds all the anagrams of a word from a list.
param word:(String) a word that we searching anagrams for.
param word_list:(List(String)) the list of the words that can potentially be anagrams.
return :(List(String)) the list of the anagrams of the word (it can be empty).
"""
def anagrams(word, word_list):
    result = list()
    for w in word_list:
        if sorted(w) == sorted(word):
            result.append(w)
    return result


