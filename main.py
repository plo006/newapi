import os
import brain

def run_chatbot():
    print("Hello! I'm your chatbot. Ask me anything.")
    while True:
        try:
            user_input = input("You: ")
            response = brain.get_response(user_input)
            print(f"Bot: {response}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    run_chatbot()
