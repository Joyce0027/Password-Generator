#Random Password Generator 

#Random module: generates random numbers, shuffle lists and pick random characters 
import random 

#Shuffle all the characters of string 
def shuffle(string):
    tempList = list(string)  #converts string into list 
    random.shuffle(tempList) #rearranges the items 
    return ''.join(tempList) #joins it back into a string 
    
print("Here's your generated passowrd:")

#Main program starts here (uses ASCII code)
uppercaseLetter1 = chr(random.randint(65,90)) #Generates random UpperCase letter
uppercaseLetter2 = chr(random.randint(65,90))
lowercaseLetter3 = chr(random.randint(97,122)) #Generate random Lowercase letter
digit = chr(random.randint(48,57)) #Generates random numbers
symbol1 = chr(random.randint (48,57))
uppercaseLetter4 = chr(random.randint(65,90))
lowercaseLetter5= chr(random.randint(97,122))
lowercaseLetter6 = chr(random.randint(97,122))
digit = chr(random.randint(48,57))
symbol2 = chr(random.randint (48,57))
uppercaseLetter7 = chr(random.randint(65,90))
lowercaseLetter8 = chr(random.randint(97,122))


#Generate Password 
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter3 + digit + symbol1 + uppercaseLetter4 + lowercaseLetter5 + lowercaseLetter6 + digit + symbol2 + uppercaseLetter7 + lowercaseLetter8
password = shuffle(password)

#Print 
print(password)
