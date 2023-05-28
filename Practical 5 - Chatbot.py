#Name :- Anurag Avinash Shevale
#Roll No :- 20
#Assignment :- 5 - Implementation Of Chatbot For Mental Health

import random

# Possible responses for the chatbot
responses = {
    "hello": ["Hello! How are you ?",
              "Hi there! I hope you are having good day.",
              "Hey! Its me your virtual friend."],

    "how_are_you": ["I'm doing well, thank you for asking.",
                    "I'm feeling great today!",
                    "I'm doing alright."],

    "goodbye": ["Goodbye!",
                "See you later!",
                "Take care."],

    "who_created_you": [
        "Anurag Shevale Created Me Using Python Version 3.11"
    ],

    "anxiety": ["It's important to take care of your mental health. Have you been practicing self-care?"],

    "depression": ["Remember that it's okay to not be okay. Have you talked to anyone about how you're feeling?"],

    "mental_health": ["There's no shame in seeking help for your mental health. Have you considered therapy?"],

    "default": ["I'm sorry, I don't understand. Could you rephrase that?",
                "Could you say that again?",
                "I'm not sure what you mean."],

    "thank_you": ["Have a great day !"]
}

# Function to generate a response based on user input
def generate_response(input_text):
    input_text = input_text.lower()
    if "hello" in input_text:
        return random.choice(responses["hello"])
    elif "how are you" in input_text:
        return random.choice(responses["how_are_you"])
    elif "goodbye" in input_text:
        return random.choice(responses["goodbye"])
    elif "anxiety" in input_text:
        return random.choice(responses["anxiety"])
    elif "depression" in input_text:
        return random.choice(responses["depression"])
    elif "mental health" in input_text:
        return random.choice(responses["mental_health"])
    elif "who created you" in input_text:
        return random.choice(responses["who_created_you"])
    elif "thank you" in input_text:
        return random.choice(responses["thank_you"])

    else:
        return random.choice(responses["default"])

# Main function to handle the conversation
def main():
    print("Welcome To MentalHealthMattersBot. What can I do for you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print(random.choice(responses["goodbye"]))
            break
        response = generate_response(user_input)
        print("MENTALHEALTHMATTERS: " + response)

if __name__ == "__main__":
    main()
