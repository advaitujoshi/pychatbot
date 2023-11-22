import random

R_EATING = "I don't like anything because I am a bot, obviously!"

def unknown():
    response = random.choice([
        "Could you please re-phrase that?",
        "...",
        "Sounds about right",
        "What does that mean"
    ])
    return response

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
    if any(keyword in user_input.lower() for keyword in ["one more joke", "another joke", "tell me a joke", "funny joke", "funny jokes"]):
        return get_joke()
    else:
        return unknown()

songs = [
    "https://www.youtube.com/watch?v=cmCDqX3ngfA",
    "https://www.youtube.com/watch?v=VUdeIFQtDYU",
    "https://www.youtube.com/watch?v=68vZX2uUKKA",
    "https://www.youtube.com/watch?v=qK5KhQG06xU",
    "https://www.youtube.com/watch?v=ipii7KbbJLY",
    "https://www.youtube.com/watch?v=8xG7mH8i-WE"
]

song_index = 0

def get_song():
    global song_index
    song = songs[song_index]
    song_index = (song_index + 1) % len(songs)
    return song

def process_user_input(user_input):
    if any(keyword in user_input.lower() for keyword in ["one more cheerful song", "another cheerful song", "tell me a cheerful song", "cheerful song"]):
        return get_song()
    else:
        return unknown()
