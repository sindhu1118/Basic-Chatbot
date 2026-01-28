def display_welcome():
    print("=" * 50)
    print("🤖 Welcome to the Rule-Based Chatbot")
    print("You can try typing:")
    print("hello | how are you | help | bye")
    print("=" * 50)


def get_user_input():
    return input("You: ").strip().lower()


def generate_response(user_input):
    responses = {
        "hello": "Hi! Nice to meet you 😊",
        "how are you": "I'm doing well, thanks for asking!",
        "help": "You can say hello, ask how I am, or type bye to exit.",
        "bye": "Goodbye! Have a great day 🌟"
    }

    if user_input in responses:
        return responses[user_input]
    else:
        return "Sorry, I didn't understand that. Type 'help' to see options."


def start_chatbot():
    display_welcome()

    while True:
        user_input = get_user_input()
        response = generate_response(user_input)
        print("🤖 Chatbot:", response)

        if user_input == "bye":
            break


start_chatbot()
