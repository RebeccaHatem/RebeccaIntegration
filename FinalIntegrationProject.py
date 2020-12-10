"""This is my Integration Project"""
"""This program helps the user decide what movie to watch in theaters and
                         calculate the price"""
__author__ = "Rebecca Hatem"
#Did not use any outside source only the POGILS and their corresponding code


print("Hello! If you're interested in finding the right movie in theaters"
      " then you've come to the right place!")
name = input("First can I please have your name?: ")
#Prints name three times and compliments it
print(name * 3 + ", what a nice name!")
birthday = int(input("As you know some shows/movies are limited to people"
         " under certain age ranges\ncan you please enter your birth year: "))
year = 2020
age = year - birthday

#Defines each genre different movies that fit in it and spaces it out
def action():
    """Lists all movies under the genre Action"""
    print("Your options are:\nTenent\nThe Empire Strikes Back\nAva")
def thriller():
    """Lists all movies under the genre Thriller"""
    print("Your options are:\nInfidel\nTenent\nUnhinged\nThe Secrets We "
          "Keep\nAva")
def mystery():
    """Lists all movies under the genre Mystery"""
    print("Your options are:\nInfidel\nUnhinged")
def scifi():
    """Lists all movies under the genre Sci-fi"""
    print("Your options are:\nThe Empire Strikes Back\nBill & Ted Face the "
          "Music")
def romance():
    """Lists all movies under the genre Romance"""
    print("Your options are:\nThe Broken Hearts Gallery")
def comedy():
    """Lists all movies under the genre Comedy"""
    print("Your options are:\nThe Last Shift\nBill & Ted Face the Music")
def crime():
    """Lists all movies under the genre Crime"""
    print("Your options are:\nKijillonaire")
def drama():
    """Lists all movies under the genre Drama"""
    print("Your options are:\nThe Secrets We Keep\nKijillonaire")
#Confirms user is using the right code
movie_theater = int(input("Are you interested in watching something in "
                    "theaters?\n1 = yes\n2 = no\n"))

num_people = int(input("\nPlease enter the number of people "
                              "attending: "))
if movie_theater == 1:
    #Asks for the number of people attending so the total price can be
    # calculated later
    print("Before we get to the prices lets pick a movie shall we?\n")
    print("What genre are you most interested in watching?")
#Asks which genre the user want to watch and gives different options to select
    # the right genre
    movieTheater_genre = int(input("Action = 1\nThriller = 2\nMystery = 3"
            "\nSci-fi = 4\nRomance = 5\nComedy = 6\nCrime = 7\nDrama = 8\n"))
    #age_range = int(input("\nWhat are the ages of people attending?\n))
#Prints out the movie options in relation to the genre the user picked
    if movieTheater_genre == 1:
        #Lists movies under this genre
        action()

#Asks each person for age and if underage tells what they can not watch
        for x in range(num_people - 1):
            age_range = int(input("\nWhat are the ages of people attending?\n"
                                  ))
            if age_range or age <= 17:
                print("\nOne or more people in your group can't watch Ava\n")
            else:
                print("Your group can watch all of the movies listed above!")
    elif movieTheater_genre == 2:
        # Lists movies under this genre
        thriller()
        for x in range(num_people - 1):
            age_range = int(input("\nWhat are the ages of people attending?\n"
                                  ))
            if age_range or age <= 17:
                print("\nDue to the ages of one or more people in your group"
                      " you can only watch Tenent\n")
            else:
                print("Your group can watch all of the movies listed above!")
    elif movieTheater_genre == 3:
        # Lists movies under this genre
        mystery()
        for x in range(num_people - 1):
            age_range = int(input("\nWhat are the ages of people attending?\n"
                                  ))
            if age_range or age <= 17:
                print("\nDue to the ages of one or more people in your group"
                      " you can't watch any movies in this genre. Sorry!\n")
            else:
                print("Your group can watch all of the movies listed above!")
    elif movieTheater_genre == 4:
        # Lists movies under this genre
        scifi()
    elif movieTheater_genre == 5:
        # Lists movies under this genre
        romance()
    elif movieTheater_genre == 6:
        # Lists movies under this genre
        comedy()
        for x in range(num_people - 1):
            age_range = int(input("\nWhat are the ages of people attending?\n"
                                  ))
            if age_range or age <= 17:
                print("\nDue to the ages of one or more people in your group"
                      " you can only watch Bill & Ted Face the Music\n")
            else:
                print("Your group can watch all of the movies listed above!")
    elif movieTheater_genre == 7:
        # Lists movies under this genre
        crime()
        for x in range(num_people - 1):
            age_range = int(input("\nWhat are the ages of people attending?\n"
                                  ))
            if age_range or age <= 17:
                print("\nDue to the ages of one or more people in your group"
                      " you can't watch any movies in this genre. Sorry!\n")
            else:
                print("Your group can watch all of the movies listed above!")
    elif movieTheater_genre == 8:
        # Lists movies under this genre
        drama()
        for x in range(num_people - 1):
            age_range = int(input("\nWhat are the ages of people attending?\n"
                                  ))
            if age_range or age <= 17:
                print("\nDue to the ages of one or more people in your group"
                      " you can't watch any movies in this genre. Sorry!\n")
            else:
                print("Your group can watch all of the movies listed above!")
#If wrong input doesnt give any movie options and moves on
    else:
        print("Sorry, these are the only genres available right now!")
    print("In addition to recommending you a movie we will also help you"
          " calculate the total cost!")
    print("\nAs you know prices change slightly depending on the location;"
         " however, we should be able to give you a pretty accurate estimate!")
#Asks the user if they want popcorn so it can be used in the calculation
    popcorn = int(input("Will you be buying popcorn?\n1 = yes\n2 = no\n"))
#Assigns a price depending on what size the user chooses
    if popcorn == 1:
        pop_size = int(input("What size?\n1 for Small\n2 for Medium\n3 for"
                             " Large\n: "))
        if pop_size == 1:
            pop_price = 6
        elif pop_size == 2:
            pop_price = 7
        elif pop_size == 3:
            pop_price = 8
        else:
            print("Sorry that is not an option!")
            pop_price = 0
    else:
        print("Okay!")
        pop_price = 0
##Asks the user if they want drinks so it can be used in the calculation
    drink = int(input("Will you be buying any drinks?\n1 = yes\n2 = no\n"))
#Assigns a price depending on what size the user chooses
    if drink == 1:
        drink_size = float(input("What size?\n1 for Small\n2 for Medium\n3 for"
                                 " Large\n: "))
        if drink_size == 1:
            drink_price = 4.99
        elif drink_size == 2:
            drink_price = 5.50
        elif drink_size == 3:
            drink_price = 5.99
        else:
            print("Sorry that is not an option!")
            drink_price = 0
    elif drink < 2:
        print("Sorry, that is not an option!")
        drink_price = 0
    else:
        print("Okay!")
        drink_price = 0
    #A cheap way to demonstrate I know how to use exponents and shortcut
    # operators
    print("\nBefore I calculate the price id like to double check and make "
          "sure everything will come out correctly\n")
    test1 = 5 ** 2
    test2_p1 = 5
    test2_p1 += 5
#Prints the two numbers without weird spacing
    print(test1, "\n", test2_p1, sep="")
    check = int(input("Are the two numbers above the correct answers for"
                      " 5^2 and 5+5 respectively?\n1 = yes\n2 = no\n"))
#Repeats the equation until the user selects yes for the correct solutions
    # being shown
    while check != 1:
        check = int(input("Are the two numbers the correct answers for 5^2"
                          " and 5+5 respectively?\n1 = yes\n2 = no\n"))
#Thanks the reader for confirming and move on with the code
    while check == 1:
        try:
            print("Perfect!\nCalculating your total price now...")
            break
        except ValueError:
            print("Error. Must be a whole number.")
#Assigns am equation for calculating the price without tax
    initial_cost = float((9 * num_people) + pop_price + drink_price)
#Assigns am equation to find tax
    tax = float((initial_cost * 6) / 100)
#Assigns an equation to calculate total cost
    total_cost = float((9 * num_people) + pop_price + drink_price + tax)
#Asks the user if they want to round up
    round_up = float(input("Would you like to round up and donate the extra"
                           " cents to charity?\n1 = yes\n2 = no\n"))
#Calculates the price if the user does want to round up and prints the total
    # cost rounded up
#Also calculates the price donated to charity and displays the amount for the
    # user
    if round_up == 1:
        print("Thank you for donating $", format((total_cost // 1 + 1) -
                    total_cost, "0.2f") + "!\n" "Total cost: $",
              format(total_cost // 1 + 1, "0.2f"), sep="")
#Calculated the total price without rounding up
    else:
        print("You're total cost will be: $", format(total_cost, "0.2f"),
              sep="")
    print("Thank you for using me, have a great day!")
elif movie_theater == 2:
    print("That's all I can do right now so have a good day!")
elif not movie_theater == 1 and 2:
    print("Okay!")
