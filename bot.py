import os
from groq import Groq

# PASTE THE GROQ_API_KEY HERE.
GROQ_API_KEY = ''

HISTORY = [
    {"role": "system", "content": "You are a helpful coding assistant. Give max answer in 120 words and try to be short and smooth."},
]

# def update_history(role: str, content: str):
#     HISTORY.append({'role': role, 'content': content})
#     if len(HISTORY)>6:
#         HISTORY.pop(1)

def line_end():
    print('*'*50)
    print('\n\n')

def main(question: str):
    client = Groq(
        api_key=GROQ_API_KEY,
    )

    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {"role": "system", "content": "You are a helpful coding assistant."},
    #         {"role": "user", "content": question},
    #     ],
    #     model="llama-3.3-70b-versatile",
    # )

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant. Give max answer in 120 words and try to be short and smooth."},
            {'role': 'user', 'content': question}
        ],
        model="openai/gpt-oss-120b",
        temperature=0.7
    )

    # update_history('assistant', chat_completion.choices[0].message.content)
    
    print(chat_completion.choices[0].message.content)

    line_end()

if __name__ == "__main__":
    os.system("cls")
    print("enter q or quit to exit\n")
    while True:
        question = input("what U wanna ask??\n-\t")
        if question.strip().lower() == "q" or question.strip().lower() == "quit":
            break
        # update_history('user', question)
        main(question)
