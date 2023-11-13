import re
import longresponses

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

    response("Hello!", ["hello", "hi", "sup", "hey", "heyo"], required_words=["hello", "hi", "sup", "hey", "heyo"],  single_response=True)
    response("I'm doing fine, and you?", ["how", "are", "you", "doing"], required_words=["how"])
    response("Thank you!", ["i", "love", "code", "palace"], required_words=["code", "palace"])
    response("Okay", ["good", "very well", "well", "not bad", "great", "fine", "all right"], required_words=["good", "very well", "well", "not bad", "great", "fine", "all right"], single_response=True)
    response("How can I cheer you up? You can select from the following list - Funny jokes or cheerful song", ["lonely", "feeling bad", "sad", "not okay", "depressed", "not great", "unhappy", "down", "blue", "disheartened", "miserable"], required_words=["lonely", "feeling bad", "sad", "not okay", "depressed", "not great"], single_response=True)
    response(longresponses.R_EATING, ["what", "you", "eat"], required_words=["you", "eat"])
    joke = longresponses.get_joke()
    response(longresponses.get_joke(), ["joke"], required_words=["joke"])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    
    return longresponses.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

while True:
    print("Bot: " + get_response(input('You: ')))
