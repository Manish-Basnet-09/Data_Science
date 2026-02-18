# Setup your API Key
import google.generativeai as genai
import os

# Set your API key (get it from: https://aistudio.google.com/app/apikey)
os.environ["GEMINI_API_KEY"] = "AIzaSyAe81a1B7EGMuBnlgU-m5mS7kmwdDkg3es"  
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

print("😎 Fun Friend Bot Started!")
print("Type 'exit' to stop.\n")

STYLE_PROMPT = """
You are a funny, friendly best friend.
Rules:
- Keep replies under 2 sentences
- Be casual and witty
- Add light humor
- No long explanations
- Talk like a chill buddy
"""

# ✅ start chat session (this adds memory)
chat = model.start_chat()

# send style once so it sticks
chat.send_message(STYLE_PROMPT)

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Bye Buddy! Don’t forget me when you become famous 😌")
        break

    try:
        response = chat.send_message(
            user_input,
            generation_config={
                "temperature": 0.9,
                "max_output_tokens": 120
            }
        )

        print("Bot:", response.text)

    except Exception as e:
        print("Error:", e)