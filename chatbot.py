import re
from nltk.tokenize import word_tokenize
import longresponses
import meanings
from namelist import name_list

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)


    for word in message:
        if word in meanings.word_meanings:
            response(meanings.get_word_meaning(word), [word], required_words=[word], single_response=True)

    response("Hello!", ["hello", "hi", "sup", "hey", "heyo"], required_words=["hello", "hi", "sup", "hey", "heyo"],  single_response=True)
    response("I'm doing fine, and you?", ["how", "are", "you", "doing", "what's", "up"], required_words=["how"])
    response("Thank you!", ["i", "love", "code", "palace"], required_words=["code", "palace"])
    response("Okay", ["good", "very well", "well", "not bad", "great", "fine", "all right"], required_words=["good", "very well", "well", "not bad", "great", "fine", "all right"], single_response=True)
    response("How can I cheer you up? You can select - Funny joke or cheerful song", ["lonely", "bad", "sad", "not okay", "depressed", "not great", "unhappy", "down", "blue", "disheartened", "miserable"], required_words=["lonely", "feeling bad", "sad", "not okay", "depressed", "not great"], single_response=True)
    response("Goodbye! See you later!", ["bye", "goodbye", "bye-bye"], required_words=["bye", "goodbye", "bye-bye"], single_response=True)
    response("I'm just a chatbot created to assist you.", ["name", "who are you", "what's your name", "your name"], required_words=["name"], single_response=True)
    response("I recommend copying and pasting the same text on google 😊", ["i", "wanted", "an", "advice"], required_words=["Advice", "Guidance", "Recommendation", "Suggestion", "Tip"], single_response=True)
    response("Sure! I am a chatbot. I was made on 13th November, 2023 😊", ["give", "me", "information", "about", "you"], required_words=["information", "about", "you"])
    response("👍", ["okay"], required_words=["okay"])
    response(longresponses.R_EATING, ["what", "you", "like"], required_words=["you", "like"])
    joke = longresponses.get_joke()
    response(joke, ["joke"], required_words=["joke"])
    song = longresponses.get_song()
    response(song, ["song"], required_words=["cheerful", "song"])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    
    return longresponses.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = word_tokenize(user_input.lower())

    split_message = re.findall(r'\b\w+\b|[.,;?!]', ' '.join(split_message))

    new_msg = []
    for word in split_message:
        for wrd in name_list:
            if word in wrd:
                new_msg.append(wrd)
                continue

    new_msg = new_msg if len(new_msg) > 0 else split_message
            
    response = check_all_messages(new_msg)
    #response = check_all_messages(split_message)
    return response

while True:
    user_input = input('You: ')
    response = get_response(user_input)
    print("Bot: " + response)
    if response.lower() == "goodbye! see you later!":
        break
