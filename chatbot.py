import google.generativeai as genai

# 1. Configure the API with your unique key
# Replace 'YOUR_API_KEY_HERE' with the actual key you copied from Google AI Studio
API_KEY = "YOUR_API_KEY_HERE"
genai.configure(api_key=API_KEY)

# 2. Initialize the latest text model (gemini-2.5-flash or gemini-1.5-flash)
# Note: 'gemini-pro' is legacy; flash models are standard for fast text chats
model = genai.GenerativeModel("gemini-1.5-flash")

# 3. Start a chat session to maintain conversation history
chat = model.start_chat(history=[])

print("🤖 Chatbot Initialized! Type 'exit' or 'quit' to stop.\n")

# 4. Create the continuous interaction loop
while True:
    # Get input from the user
    user_input = input("You: ")
    
    # Check if the user wants to break out of the loop
    if user_input.lower() in ['exit', 'quit']:
        print("Chatbot: Goodbye!")
        break
        
    # Send the message to the model with streaming enabled for chunk responses
    try:
        response = chat.send_message(user_input, stream=True)
        
        print("AI: ", end="")
        # Print response chunks as they arrive for a smooth typing effect
        for chunk in response:
            print(chunk.text, end="", flush=True)
        print("\n") # Print a newline for the next turn
        
    except Exception as e:
        print(f"\nAn error occurred: {e}\n")
