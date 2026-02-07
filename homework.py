import re
import datetime

def clean_input(text):
    """Basic input cleaning (NLP-ready)"""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    return text

def get_time():
    return datetime.datetime.now().strftime("%H:%M")

def get_date():
    return datetime.datetime.now().strftime("%d %B %Y")

def chatbot_response(user_input):
    user_input = clean_input(user_input)

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"

    # Name
    elif "your name" in user_input:
        return "I am a rule-based chatbot created in Python."

    # Time
    elif "time" in user_input:
        return f"The current time is {get_time()}."

    # Date
    elif "date" in user_input:
        return f"Today's date is {get_date()}."

    # Help
    elif "help" in user_input:
        return (
            "You can ask me about:\n"
            "- My name\n"
            "- Current time\n"
            "- Current date\n"
            "- Basic greetings\n"
            "- Type 'exit' to quit"
        )

    # Exit
    elif user_input in ["exit", "quit", "bye"]:
        return "Goodbye! Have a nice day."

    # Default response
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."

def main():
    print("🤖 Rule-Based Chatbot (Terminal)")
    print("Type 'help' to see options")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)
        print("Bot:", response)

        if clean_input(user_input) in ["exit", "quit", "bye"]:
            break

if __name__ == "__main__":
    main()
