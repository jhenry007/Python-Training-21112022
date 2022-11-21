#Hello World-I love Python
#Print the following output in one line of code:
print(("Hello World\n"*4)+("I love python\n"*4))

#Exercise 2 : What Is The Season ?
#Ask the user to input a month (1 to 12).
#Display the season of the month received :
#Spring runs from March (3) to May (5)
#Summer runs from June (6) to August (8)
#Autumn runs from September (9) to November (11)
#Winter runs from December (12) to February (2)

season = input("What is the actual month ? ")
if season == "January" or season == "February" or season == "December":
    print("Winter runs from December (12) to February (2)")
elif season == "March" or season == "April" or season == "May":
    print("Spring runs from March (3) to May (5)")
elif season == "June" or season == "July" or season == "August":
    print("Summer runs from June (6) to August (8)")
elif season == "September" or season == "October" or season == "November":
    print("#Autumn runs from September (9) to November (11)")

