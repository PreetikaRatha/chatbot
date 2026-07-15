!pip install -q google-generativeai
import google.generativeai as genai

# Configure your API key
API_KEY = "YOUR_API_KEY_HERE"
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-2.5-flash")

# Start a chat
chat = model.start_chat(history=[])

print("🤖 Chatbot Initialized! Type 'exit' or 'quit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    try:
        response = chat.send_message(user_input, stream=True)

        print("AI: ", end="")

        for chunk in response:
            print(chunk.text, end="", flush=True)

        print("\n")

    except Exception as e:
        print(f"\nAn error occurred: {e}\n")
