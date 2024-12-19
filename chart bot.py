import re

# Function to get a response based on user input
def chatbot_response(user_input):
    # Convert input to lowercase for easier matching
    user_input = user_input.lower()
    
    # Define simple rule-based responses
    if re.search(r'\b(hello|hi|hey)\b', user_input):
        return "Hello! How can I help you today?"
    elif re.search(r'\b(how are you|how\'s it going|how are you doing)\b', user_input):
        return "I'm just a chatbot, but I'm doing great! How about you?"
    elif re.search(r'\b(what is your name|who are you)\b', user_input):
        return "I'm ChatBot, your friendly assistant!"
    elif re.search(r'\bbye\b', user_input):
        return "Goodbye! Have a great day!"
    elif re.search(r'\b(what is|define|meaning of)\b', user_input):
        return "Could you please clarify what you'd like me to define?"
    elif re.search(r'\b(help)\b', user_input):
        return "I can assist with answering basic questions. Try asking about my name or say 'bye' to exit."
    else:
        return "Sorry, I didn't quite understand that. Can you rephrase?"

# Main loop for chatbot interaction
def chat():
    print("ChatBot: Hi there! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if re.search(r'\bbye\b', user_input.lower()):
            print("ChatBot: Goodbye!")
            break
        
        # Get the chatbot's response
        response = chatbot_response(user_input)
        print("ChatBot:", response)

# Start the chatbot
chat()
