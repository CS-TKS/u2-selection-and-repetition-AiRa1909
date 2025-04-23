again = True

while again:

    user_choices = []
    stages = [
        {
            "scenario": "Choose an energy system! ",
            "options": ["1. Fossil Fuels", "2. Wind Power", "3. Solar Energy", "4. Hydropower", "5. Nuclear Plants"],
            "points": ["10", "20", "30", "40" , "50"],
            "comment": ["... On the bones of the dead!", "To the skies!", "Reap the sun!", "Fish, live no more!", "Ah yes, smoke."]
        },
        {
            "scenario": "What policy should we enforce? ",
            "options": ["1. Banning plastic bags", "2. Charging for littering", "3. Tourism /'Green Tax/'"],
            "points": ["20", "50", "45"],
            "comment": ["Dependency exists.", "Keep the streets clean!", "Sustainable travel!"]

        },
        {
            "scenario": "Pick a main housing system! ",
            "options": ["1. Skyscrapers/Apartments", "2. FREE RANGE"],
            "points": ["40, 10"],
            "comment": ["A high achiever, I see", "... ANARCHY!"]
        },
    ]

    print("You are a sustainable city planner in 2025, creating a city that is in line with all 17 United Nations SDG Goals. \n Through 17 choices, attempt to obtain the highest score, and be awarded for your efforts! \n")
    name = input("Enter name: ")
    city_name = input("Enter city name to start: ")

    for i in stages:
        print(i["scenario"])
        print(" ".join(i["options"]), "\n")
        choice = int(input())
        user_choices.append(choice)
        print(i["comment"][choice-1], "\n")


    X = input("Would you like to play again? ")