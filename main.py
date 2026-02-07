import re, random

destinations = {
    'beaches' : ['bali', 'maldives', 'phuket'],
    "mountain" : ["Swiss alps", "rocky mountain"],
    "cities": ['tokyo', 'paris', "new york"]
}

jokes = [
    "why programmers like nature? too many bugs"
    "why did the computer go to the doctor?, he got a virus"
    "why do travellers always feell warm?, because of all their hot spots"
]

def normailize_input(text):
    return re.sub(r'\s', " ", text.strip().lower())

def recommend():
    print("travel bot:" \
    "beaches", 'mountains', 'or' 'cities')
    preference = input("you: ")
    preference = normailize_input(preference)

    if preference in destinations:
        suggestions = random.choice(destinations[preference])
        print(f"Travel bot: how about {suggestions}!")
        print("Travel bot: do you like it")
        answer = input("you: ").lower()
        if answer == 'yes':
            print(f"Travelbot: awesome! enjoy {suggestions}" )
        elif answer == "no":
            print("Travelbot: Let's try another.")
            recommend()
        else:
            print("Travelbot; I'll suggest again.")
            recommend()
    else:
        print("Travelbot: sorry, i dont have more suggestions") 
    show_help()

def packing_tips():
    print("travelbot: where to?")
    location = normailize_input(input("you: "))
    print("travelbot: how many days")
    days = input("you: ")

    print(f"Travelbot: packing tips for {days} days in {location}:")
    print("- Pack versatile cloches.")
    print("bring chargers, adapters")
    print("check weather")

def tell_joke():
    print(f"Travelbot: {random.choice(jokes)}")

def show_help():
    print("\n I can : ")
    print(" - suggest travel spots (say 'recomendatation')")
    print("- Offer packing tips (say 'packing')")
    print("- Tell a joke (say 'joke')")
    print("Type 'exit' or 'bye' to end. \n")
def chat():
    print("hello! i am travelbot")
    name = input("you name")
    print(f"nice to meet you{name}")

    show_help()

    while True:
        user_input = input(f"{name}")
        user_input = normailize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input :
            packing_tips()
        elif "joke" in user_input:
            tell_joke()
        elif "exit" in user_input:
            show_help()
            break
        elif 'Help' in user_input:
            show_help()
        else:
            print("travelbot: could you rephrase")
if __name__ == "__main__":
    chat()
