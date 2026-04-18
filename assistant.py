import ollama

# ====================== CONFIG ======================
MODEL = "llama3.2"   # Change later to other models you pull

SYSTEM_PROMPT = "You are a helpful, friendly AI assistant. Be concise and accurate."

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

print(f"🤖 AI Assistant ready! (Running {MODEL} locally with Ollama)")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    # Call Ollama (exactly same format as OpenAI!)
    response = ollama.chat(
        model=MODEL,
        messages=messages
    )

    assistant_reply = response['message']['content']
    print(f"AI: {assistant_reply}\n")

    messages.append({"role": "assistant", "content": assistant_reply})