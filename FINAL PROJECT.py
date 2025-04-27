import random

again = True

while again:
    user_choices = []
    sust_score = 0
    budget = random.randint(200,800)
    spent = 0

    stages = [
        {
            "scenario": "Choose an energy system! ",
            "options": ["1. Fossil Fuels", "2. Wind Power", "3. Solar Energy", "4. Hydropower", "5. Nuclear Plants"],
            "points": ["10", "20", "30", "40" , "50"],
            "costs": ["50", "200","150","125","100"],
            "comment": ["... On the bones of the dead!", "To the skies!", "Reap the sun!", "Fish, live no more!", "Ah yes, smoke."]
        },
        {
            "scenario": "What policy should we enforce? ",
            "options": ["1. Banning plastic bags", "2. Charging for littering", "3. Tourism 'Green Tax'"],
            "points": ["20", "50", "45"],
            "costs": ["50", "200", "500"],
            "comment": ["Dependency exists.", "Keep the streets clean!", "Sustainable travel!"]

        },
        {
            "scenario": "Pick a main housing system! ",
            "options": ["1. Skyscrapers/Apartments", "2. FREE RANGE Housing"],
            "points": ["40", "10"],
            "costs": ["200", "50"],
            "comment": ["A high achiever, I see", "... ANARCHY!"]
        },
    ]

    print("\n You are a sustainable city planner in 2025, and you have", budget, "million dollars to create city that is in line with all 17 United Nations SDG Goals. \n Through 17 choices, attempt to obtain the highest score, and be awarded for your efforts! \n")
    name = input("Enter name: ")
    city_name = input("Enter city name to start: ")
    seperator = "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"

    for i in stages:
        print(i["scenario"])
        print(" ".join(i["options"]), "\n")
        choice = int(input())
        user_choices.append(i["options"][choice - 1])
        sust_score += int(i["points"][choice - 1])
        budget -= int(i["costs"][choice - 1])
        spent += int(i["costs"][choice - 1])
        print(i["comment"][choice - 1])
        if budget <= 0:
            print(f"\n {seperator} \n Ran out of money! \n")
            break
        print(" Score =", sust_score, "\n Money Left =", budget, "\n")

    print(user_choices)
    for i in user_choices:
        for letter in i:
            if letter isnumeric():
                i.replace(letter, "")
            elif letter ==
                i.replace(letter,"")
            else:
                pass
        print(user_choices)
    a = " and ".join(user_choices)
    print(f"\n {seperator} \n You have reached the end of your planning! \n You spent a total of ${spent}M for {a}. \n Overall, your sustainability score is {sust_score}. \n")

    if sust_score >= 75:
        print(f"You did an amazing job {name}! {city_name} complies with a multitude of Sustainable Development Goals! Success!")
    elif sust_score >= 50:
        print(f"Good job {name}! {city_name} complies with enough sustainable goals to pass!")
    elif sust_score >= 25:
        print(f"Okay, {name} {city_name} complies a few sustainable development goals. You can do better")
    else:
        print(f"Fail! {city_name} barely reaches any sustainable development goals! You can do way better {name}!")

    x = input("Would you like to play again? ").upper()

    if x == "NO" or x == "NOPE" or x == "NAH" or x == "NEIN" or x == "NAY":
        print("Oh well. Goodbye!")
        again = False
    elif:
        if x.find("not") == 1
    else:
        pass