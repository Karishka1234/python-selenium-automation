string = input("Enter a string: ")


def count_letters(string1):
    string2 = string1.split(" ")
    print(string2)
    longest = ''
    length = 0
    for i in string2:
        if length < len(i):
            length = len(i)
            longest = i
    return longest

print(count_letters(string))