sentence = input("Enter a sentence ") 
for letter in sentence:
    if letter. lower() == "r":
        print('\033[31m', end ='')
    elif letter. lower() == "g":
        print('\033[32m', end ='')
    elif letter. lower() == "b":
        print('\033[34m', end ='')
    elif letter. lower() == "p":
        print('\033[35m', end ='')
    elif letter. lower() == "y":
        print('\033[33m', end ='')

    print(letter, end ='')
    print('\033[0m', end='')
  
