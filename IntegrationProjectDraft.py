#Hatem, Rebecca
#This program helps the user decide what movie to watch in theaters and calculate the price
#Did not use any outside source only the POGILS and the corresponding code for them

import random
print("Hello! If youre interested in finding the right movie in theaters then youve come to the right place!")
name = input("First can I please have your name?: ")
#Prints name three times and compliments it
print(name * 3 + ", what a nice name!")
birthday = int(input("As you know some shows/movies are limited to people under certain age ranges\ncan you please enter your birth year: "))
year = 2020
age = year - birthday
#Defines each genre (variable) differenct movies that fit in it and spaces it out like a list
def action():
    print("Your options are:\nTenent\nThe Empire Strikes Back\nAva")
def thriller():
    print("Your options are:\nInfidel\nTenent\nUnhinged\nThe Secrets We Keep\nAva")
def mystery():
    print("Your options are:\nInfidel\nUnhinged")
def scifi():
    print("Your options are:\nThe Empire Strikes Back\nBill & Ted Face the Music")
def romance():
    print("Your options are:\nThe Broken Hearts Gallery")
def comedy():
    print("Your options are:\nThe Last Shift\nBill & Ted Face the Music")
def crime():
    print("Your options are:\nKijillonaire")
def drama():
    print("Your options are:\nThe Secrets We Keep\nKijillonaire")
#Confirms user is using the right code
movie_theater = int(input("Are you interested in watching something in theaters?\n1 = yes\n2 = no\n"))
num_people = int(input("\nPlease enter the number of people attending: "))
if movie_theater == 1:
    #Asks for the number of people attending so the total price can be calculated later
    print("Before we get to the prices lets pick a movie shall we?\n")
    print("What genre are you most interested in watching?")
#Asks which genre the user want to watch and gives different options to select the right genre
    movieTheater_genre = int(input("Action = 1\nThriller = 2\nMystery = 3\nSci-fi = 4\nRomance = 5\nComedy = 6\nCrime = 7\nDrama = 8\n"))
#Prints out the movie options in relation to the genre the user picked
    if movieTheater_genre == 1:
        action()
#Asks each person for ago and if unerage tells what they can not watch
        for x in range(num_people):
            age_range = int(input("\nWhat are the ages of people attending?\n"))
            if age_range <= 17:
                print("This person can't watch Ava")
    elif movieTheater_genre == 2:
        thriller()
        for x in range(num_people):
            if age_range <= 17:
                print("This person can't watch Infidel, Unhinged, The Secrets We Keep, and Ava")
    elif movieTheater_genre == 3:
        mystery()
        for x in range(num_people):
            if age_range <= 17:
                print("This person can't watch any of the movies out right now. Sorry!")
    elif movieTheater_genre == 4:
        scifi()
    elif movieTheater_genre == 5:
        romance()
    elif movieTheater_genre == 6:
        comedy()
        for x in range(num_people):
            if age_range <= 17:
                print("This person can't watch The Last Shift")
    elif movieTheater_genre == 7:
        crime()
        for x in range(num_people):
            if age_range <= 17:
                print("This person can't watch any of the movies out right now. Sorry!")
    elif movieTheater_genre == 8:
        drama()
        for x in range(num_people):
            if age_range <= 17:
                print("This person can't watch any of the movies out right now. Sorry!")
#If wrong input doesnt give any movie options and moves on
    else:
        print("Sorry, these are the only genres available right now!")
    print("In adition to recommending you a movie we will also help you calculate the total cost!")
    print("\nAs you know prices change slightly depending on the location; however, we should be able to give you a pretty accurate estimate!")
#Asks the user if they want popcorn so it can be used in the calculation
    popcorn = int(input("Will you be buying popcorn?\n1 = yes\n2 = no\n"))
#Assigns a price depending on what size the user chooses
    if popcorn == 1:
        pop_size = int(input("What size?\n1 for Small\n2 for Medium\n3 for Large\n: "))
        if pop_size == 1:
            pop_price = 6
        elif pop_size == 2:
            pop_price = 7
        elif pop_size == 3:
            pop_price = 8
    else:
        print("Okay!")
##Asks the user if they want drinks so it can be used in the calculation
    drink = int(input("Will you be buying any drinks?\n1 = yes\n2 = no\n"))
#Assigns a price depending on what size the user chooses
    if drink == 1:
        drink_size = float(input("What size?\n1 for Small\n2 for Medium\n3 for Large\n: "))
        if drink_size == 1:
            drink_price = 4.99
        elif drink_size == 2:
            drink_price = 5.50
        elif drink_size == 3:
            drink_price = 5.99
    elif drink == 2 or drink > 1:
        print("Okay!")
#A cheap way to demonstrate I know how to use exponents and shortcut operators
    print("\nBefore I calculate the price id like to double check and make sure everything will come out correctly\n")
    test1 = 5 ** 2
    test2_p1 = 5
    test2_p1 += 5
#Prints the two numbers without weird spacing
    print(test1, "\n", test2_p1, sep="")
    check = int(input("Are the two numbers above the correct answers for 5^2 and 5+5 respectively?\n1 = yes\n2 = no\n"))
#Repeats the equation until the user selects yes for the correct solutions being shown
    while check != 1:
        check = int(input("Are the two numbers the correct answers for 5^2 and 5+5 respectively?\n1 = yes\n2 = no\n"))
#Thanks the reader for confirming and move on with the code
    if(check == 1):
        print("Perfect!\nCalculating your total price now...")
#Assigns am equation for calculating the price without tax
    initial_cost = float((9 * num_people) + pop_price + drink_price)
#Assigns am equation to find tax
    tax = float((initial_cost * 6) / 100)
#Assigns an equation to calculate total cost
    total_cost = float((9 * num_people) + pop_price + drink_price + tax)
#Asks the user if they want to round up
    round_up = float(input("Would you like to round up and donate the extra cents to charity?\n1 = yes\n2 = no\n"))
#Calculates the price if the user does want to round up and prints the total cost rounded up
#Also calculates the price donated to charity and displays the amount for the user
    if round_up == 1:
        print("Thank you for donating $", format((total_cost // 1 + 1) - total_cost, "0.2f") + "!\n" "Total cost: $", format(total_cost // 1 + 1, "0.2f"), sep="")
#Calculated the total price without rounding up
    else:
        print("Youre total cost will be: $", format(total_cost, "0.2f"), sep="")
    print("Thank you for using me, have a great day!")
elif movie_theater == 2:
    print("Thats all I can do right now so have a good day!")
elif not movie_theater == 1 and 2:
    print("Okay!")
    
    

                       
      

