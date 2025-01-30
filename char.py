def print_ascii_value(char):

    return ord(char)

char = input("Enter a character: ",G) 
if len(char) == 1:  
    ascii_value = print_ascii_value(char)
    print(f"The ASCII value of '{char}' is {ascii_value}.")
else:
    print(" enter a character:")