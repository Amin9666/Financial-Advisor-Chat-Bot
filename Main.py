import ollama
import openai

openai.api_key = "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"

def chat_main(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )
    return response.choices[0].messages.content.strip()
if __name__ == "__main__":
    while(True):
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        
        response = chat_main(user_input)
        print("Chat: ", response)
    