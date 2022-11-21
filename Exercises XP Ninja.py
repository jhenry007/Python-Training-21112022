#Exercise 4 : How many characters in a sentence
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
lenmytext = len(my_text)
print(lenmytext)

#Exercise 5: Longest word without a specific character
#Instructions
#Keep asking the user to input the longest sentence they can without the character “A”.
#Each time a user successfully sets a new longest sentence, print a congratulations message.
inputbox = str(input("Please input your longest word here, without the character A : "))

print("A" in inputbox)
i = ("A" in inputbox)
while i == False:
    print("Congratulation, you have selected the longest sentence without A")
    break
else:
    str(input("Your sentence contains the character A, please select another sentence : "))

