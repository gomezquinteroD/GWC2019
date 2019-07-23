# --- Define your functions below! ---
def intro():
    print("Hello user! Welcome to Charlie's Chatbot :)")
    print("Type a message to start a conversation. ")

def process_input(answer):
    if answer == "hi":
        greeting()
    else:
        say_default()

def greeting():
    print("Hello there friend! I hope your day is going well :)")

def say_default():
    print("Wow who would have thought.")

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)
        print("That's cool!")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
