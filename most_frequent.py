#WAP to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.

def most_frequent(string):
    d = {}
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

x = input('Enter a string : ')
print (most_frequent(x))
