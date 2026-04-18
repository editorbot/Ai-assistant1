import os
from dotenv import load_dotenv
from openai import OpenAI

# ====================== CONFIG ======================
load_dotenv()

# Load and CLEAN the key (removes any spaces or hidden characters)
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ ERROR: OPENAI_API_KEY not found in .env file!")
    print("   → Make sure the file exists in the ai-assistant folder")
    exit()
else:
    cleaned_key = api_key.strip()          # ← This removes trailing spaces
    print(f"✅ .env loaded (key length: {len(cleaned_key)})")

client = OpenAI(api_key=cleaned_key)   # Use the cleaned key

SYSTEM_PROMPT = "You are a helpful, friendly AI assistant. Be concise and accurate."

messages = [{"role": "system", "content": SYSTEM_PROMPT}]

print("🤖 AI Assistant ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )

    assistant_reply = response.choices[0].message.content
    print(f"AI: {assistant_reply}\n")

    messages.append({"role": "assistant", "content": assistant_reply})