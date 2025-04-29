import random
import re

again = True

while again:
    user_choices = []
    choices = []
    sust_score = 0
    budget = random.randint(400,900)
    spent = 0
    seperator = "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"

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
                        "Really beautiful. But really expensive. Really high maintenance, with a ton of emissions! You can do better!"]

        },
        {
            "scenario": "Let's get rid of 60 Million for bike pathways everywhere! 1. Yay or 2. Nay?",
            "options": ["", ""],
            "points": ["60", "0"],
            "costs": ["60", "0"],
            "comment": ["Money well spent! In support of SDG 11 sustainable communities!",
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

    print("\n You are a sustainable city planner in 2025, and you have", budget, "million dollars to create city that is in line with all 17 United Nations SDG Goals. \n Through 17 choices, attempt to obtain the highest score, and be awarded for your efforts! \n")
    name = input("Enter name: ")
    city_name = input("Enter city name to start: ")
    print(f"{seperator} \n")

    for i in stages:
        print("\n", i["scenario"])
        print(" ".join(i["options"]), "\n")
        choice = int(input())
        user_choices.append(i["options"][choice - 1])
        sust_score += int(i["points"][choice - 1])
        budget -= int(i["costs"][choice - 1])
        spent += int(i["costs"][choice - 1])
        print(i["comment"][choice - 1])
        if budget <= 0:
            print(f"\n {seperator} \n Ran out of money!")
            break
        print(" Score =", sust_score, "\n Money Left =", budget)

    for i in user_choices:
        res = (re.sub(r"\d.","",i)).lower()
        choices.append(res.strip())
    a = " and ".join(choices)
    print(f"{seperator} \n You have reached the end of your planning! \n You spent a total of ${spent}M for {a}. \n Overall, your sustainability score is {sust_score}. \n")

    if sust_score == 300:
        print(f"You picked all the best options {name}! Absolutely amazing. {city_name} complies with SDG 7, 11, 12 and 9! Complete Success!")
    elif sust_score < 300 and sust_score >= 235:
        print(f"You did an amazing job {name}! {city_name} complies with a multitude of Sustainable Development Goals!")
    elif sust_score >= 170:
        print(f"Good job {name}! {city_name} complies with enough sustainable goals to pass!")
    elif sust_score >= 105:
        print(f"Okay, {name} {city_name} complies a few sustainable development goals. You can do better")
    else:
        print(f"Fail! {city_name} barely reaches any sustainable development goals! You can do way better {name}!")

    x = input("Would you like to play again? ").upper()

    if x == "NO" or x == "NOPE" or x == "NAH" or x == "NEIN" or x == "NAY":
        print("Oh well. Goodbye!")
        again = False
    else:
        pass