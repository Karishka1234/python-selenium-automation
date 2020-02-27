string1 = input("Enter a string: ")


# answer with strings
def delete_spaces(string):
    string2 = string.split(" ")
    string3=""
    #string2.strip()   // not working
    #string2.replace(" ", "")      // not working too
    for i in string2:
        if i != '':
            string3 += i + ' '
    return string3


print(delete_spaces(string1))


# answer with arrays
#def delete_spaces(string):
#    string2 = string.split(" ")
 #   array = []
  #  for i in string2:
   #     if i != '':
    #        array.append(i)
    #return ' '.join(array)


#print(delete_spaces(string1))