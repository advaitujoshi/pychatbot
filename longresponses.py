import random

R_EATING = ("I don't like eating anything beacause I am a bot obviously!")



def unknown():
    response = ["Could you please re-phrase that?",
            "...",
            "Sounds about right",
            "What does that mean"] [random.randrange(4)]
    return response 
      


import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "How do you organize a space party? You planet!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What did one ocean say to the other ocean? Nothing, they just waved!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "What do you call a fish wearing a crown? A kingfish!",
    "How do you catch a squirrel? Climb a tree and act like a nut!"
]

joke_index = 0

def get_joke():
    global joke_index
    joke = jokes[joke_index]
    joke_index = (joke_index + 1) % len(jokes)
    return joke

def process_user_input(user_input):
    if any(keyword in user_input.lower() for keyword in ["one more joke", "another joke", "tell me a joke", "funny joke"]):
        return get_joke()
    else:
        return "Could you please rephrase that?"

