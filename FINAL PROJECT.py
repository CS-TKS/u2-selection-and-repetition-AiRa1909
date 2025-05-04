#start by importing all needed modules
# will be needing random for deciding a random budget for the user
# will be needing regular expressions for the computer to recognize a pattern to remove from a list of user answers, so that when answers are printed at the end, they are aesthetically pleasing
import random
import re

#variable that decides whether or not the game will run again
again = True

#everything under the following while loop is considered "the game"
while again:
    #determine all "setting" data types/variables that need to exist in the first place before the game begins to operate
    user_choices = []
    choices = []
    sust_score = 0
    budget = random.randint(400,900)
    spent = 0
    seperator = "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"

    #create a list of dictionaries : each dictionary presents a "scenario" (a stage) the user will have to be in. The user can move through a maximum of 5 scenarios to build their city.
    #Each scenario has their type (energy, housing etc.), the options the user can make, the points and costs associated with each option, and a comment associated with each option
    #costs are based on real-world research on what these investments may cost
    #points are based off of how sustainable these costs are
    stages = [
        {
            "scenario": "What energy system is best for your city?",
            "options": ["1. Wind", "2. Solar", "3. Geothermal", "4. Biomass", "5. Hydropower", "6. Thermal"],
            "points": ["50", "60", "20", "10", "30", "40"],
            "costs": ["120", "140", "190", "145", "110", "160"],
            "comment": ["Onshore wind farms are among the two cheapest options in all these choices! It is also very highly supportive of SDG 7! We are going to kill a lot of birds on accident too!",
                        "Solar! The most sustainable option by far in support of SDG 7! I just hope your city doesn't experience many cloudy days :D",
                        "Pretty good choice. Geothermal has low emissions, but there are far better options that won't risk causing earthquakes!",
                        "The least sustainable option amongst all the available options! Biomass? You are going to kill a lot of animals, and burn through our wood too!",
                        "Hydropower! Very efficient! It'll last you 50-100 years. That is, at some fish migration disruptions.",
                        "Thermal? Concentrated solar power emits nearly zero emissions! However it is very energy intensive, and requires a ton of water! I wonder, why you picked thermal when Geothermal is an option right beside it?"]
        },
        {
            "scenario": "What housing systems should we invest in?",
            "options": ["1. Green Roof Houses", "2. Tiny houses", "3. Recycled Shipping Containers", "4. Prefabricated homes", "5. Normal Apartment Complexes", "5. Bungalow Neighborhoods"],
            "points": ["60","50","40","30","20","10"],
            "costs": ["180","60","90","120","160","140",],
            "comment": ["The best option in support of SDG 11 for Sustainable Communities! Turning the tops of our city green (literally)",
                        "Tiny houses are actually an amazing option for sustainability, and aren't as tiny as you think! Great job!",
                        "This is actually becoming a real, and well-working option! Interesting choice!",
                        "These homes are made first, before being plopped into their place, saving energy and emissions! Good choice, but there are better options!",
                        "... I guess we're cramming everyone into stacked floors! What happened to considering sustainability?",
                        "Really beautiful. But really expensive. Really high maintenance and with a ton of emissions too! You can do better!"]

        },
        {
            "scenario": "Let's get rid of 60 Million for bike pathways everywhere! 1. Yay or 2. Nay?",
            "options": ["", ""],
            "points": ["60", "0"],
            "costs": ["60", "0"],
            "comment": ["Money well spent! Bike pathways are well in support of SDG 11 towards building sustainable communities!",
                        "Oh well. 60 Million kept in the savings then."]
        },
        {
            "scenario":"You're the president! Let's start making some rules!",
            "options":["1. Mandatory Flood Protection", "2. Tourism 'Green Tax'", "3. Charging for littering", "4. Banning plastic", "5. Creating ZERO EMISSION zones", "6. Mandatory green roofs", "7. Carbon taxes"],
            "points": ["10","20","30","40","50","60","70"],
            "costs": ["30","150","90","50","15","20", "12"],
            "comment":["Will save us in many dire situations! However, are there better policies for sustainable communities perhaps?",
                       "Very low cost policy that will reap us a lot of money! \n ... In the name of sustainability, of course",
                       "Very low cost, and will create clean communities very quickly! But is clean the same as sustainable?",
                       "Very effective in reducing plastic use. However, there are many in our city that depend on plastic!",
                       "This was established elsewhere, and created amazing zones for more sustainable communities! Great idea!",
                       "Very very expensive! But is a great policy, that will make a lot of people's lives more difficult...",
                       "Let's charge people for being unsustainable! A great idea, actually. Great job on achieving SDG 11!"]
        },
        {
            "scenario":"What transport technology shall we invest in?",
            "options":["1. Trains", "2. Buses", "3. Biodiesel for cars", "4. Hybrid/Electric Cars"],
            "points": ["50", "30", "20", "10"],
            "costs": ["150", "40", "10", "10"],
            "comment": ["Trains actually reduce emissions by a ton, and stands as one of the best transport options for sustainability! We'll just deal with a lot of crowds daily.",
                        "Just like trains, with less crowds and chaos! A great option in support of SDG 12!",
                        "A very experimentative choice, that can work really well at low costs. But are there better options?",
                        "Very experimentative. However, are there better options?"]
        }
    ]

# begin operating the game: welcome message, + setting some variables
    print("\n You are a sustainable city planner in 2025, and you have", budget, "million dollars to create city that is in line with all 17 United Nations SDG Goals. \n Through 17 choices, attempt to obtain the highest score, and be awarded for your efforts! \n")
    name = input("Enter name: ")
    city_name = input("Enter city name to start: ")
    print(f"{seperator} \n")

# beginning iterating over all the dictionaries in our list of stages (all the scenarios in our collection of scenarios/stages).
    for i in stages:
        #print the scenario message (introduce the type)
        print("\n", i["scenario"])
        #print out the list of options. .join is used to make the list look more pretty
        print(" ".join(i["options"]), "\n")
        #collect the user's choice
        choice = input()
        #only begin allowing the game to run as long as the user inputs a "valid" choice: their choice is a number AND their choice is within the range of available options
        #not being "in range" could include trying to input negative values, or trying to input a number greater than the total number of options that exist
        if choice.isnumeric() != True or (int(choice) < 0 or int(choice) > len(i["options"])):
            print("Please re-enter a number, or a valid answer!")
            choice = input()
            if choice.isnumeric() != True or (int(choice) < 0 or int(choice) > len(i["options"])):
                print("Please re-enter a number, or a valid answer!")
                choice = input()
                # give the user three chances to input valid answers, otherwise, stop moving through all the stages that come after, and skip to the game ending.
                if choice.isnumeric() != True or (int(choice) < 0 or int(choice) > len(i["options"])):
                    print("That's it! We will be ending the game now!")
                    break
        #if their answer is valid, add their answer to a list of user answers, and caculate the user's current sustainability score and money left, based off of associated points and costs
        #calculate how much money they have left by subtracting our budget by associated costs, but also add the same value of that cost to an empty variable: in the end we can use this to know how much money the user spent
        #then print the associated feedback that aligns with the choice they made
        user_choices.append(i["options"][int(choice) - 1])
        sust_score += int(i["points"][int(choice) - 1])
        budget -= int(i["costs"][int(choice) - 1])
        spent += int(i["costs"][int(choice) - 1])
        print(i["comment"][int(choice) - 1])
        #now check their budget value. If they still have money left, continue with the game and print out their current score and the money they have left
        #if not, tell the user they ran out of money, stop moving through all stages that come after and skip to the end.
        if budget <= 0:
            print(f"\n {seperator} \n Ran out of money!")
            break
        print(" Score =", sust_score, "\n Money Left =", budget)

    #now check if the user made any choices at all.
    #if they have no choices, we can assume that the user skipped to the end because they kept inputting invalid answers repeatedly from the beginning
    # in such a case, add to their user choices "NOTHING!" so that later, in the end message, the user will be told that they spent money on "NOTHING!"
    if len(user_choices)< 1:
        choices.append("NOTHING")
    #otherwise, check through all the choices in user choices, and remove the pattern of a number and a punctuation mark coming before an actual option, so that numbers and punctuation marks are not printed out at the end.
    else:
        for i in user_choices:
            res = (re.sub(r"\d.", "", i)).lower()
            choices.append(res.strip())

    #now join the list of choices so that we can print it out when we use formatting
    a = " and ".join(choices)

    #use formatting to print out the end message
    print(f"{seperator} \n You have reached the end of your planning! \n You spent a total of ${spent}M for {a}. \n Overall, your sustainability score is {sust_score}. \n")

    #now check the user's sustainability score
    #there are five offered ranges
    #recognize which range the user's sust. score falls under, and print the associated message. Use the user's name, and city name.
    if sust_score == 300:
        print(f"You picked all the best options {name}! Absolutely amazing. {city_name} complies with SDG 7, 11, 12 and 9! Complete Success!")
    elif sust_score < 300 and sust_score >= 235:
        print(f"You did an amazing job {name}! {city_name} complies with a multitude of Sustainable Development Goals!")
    elif sust_score >= 170:
        print(f"Good job {name}! {city_name} complies with enough sustainable goals to pass!")
    elif sust_score >= 105:
        print(f"Okay, {name}! {city_name} complies with a few sustainable development goals. However, you can do better! Maybe reconsider different choices for next time?")
    else:
        print(f"Fail! {city_name} barely reaches any sustainable development goals! You can do way better {name}!")

#Ask the user if they would like to play again. Use upper to collect the most accurate answers.
    x = input("Would you like to play again? ").upper()

#the user can input various forms of saying "yes" to continue the game. Otherwise, anything they say other than these forms of "yes" will print a goodbye message, and suspend the game by changing the again boolean.
    if x == "YES" or x == "YEAH" or x == "SURE" or x == "OKAY" or x == "YEA" or x=="OK":
        pass
    else:
        print("Oh well. Goodbye!")
        again = False