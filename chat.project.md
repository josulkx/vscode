#cod
import openai

openai.api_key = 'sua-chave-de-api-aqui'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ['sair', 'exit', 'quit']:
            break
        response = chat_with_gpt(user_input)
        print(f"GPT: {response}")

#redmi
# Chatbot Project

This project is a simple chatbot that utilizes the OpenAI API to respond to user inputs. The chatbot continuously accepts user input and generates responses based on the provided prompts.

## Project Structure

```
chatbot-project
├── src
│   ├── chatbot.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chatbot-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set your OpenAI API key in the `chatbot.py` file.
2. Run the chatbot:
   ```
   python src/chatbot.py
   ```

3. Start chatting with the bot! Type your messages and receive responses. Type 'sair', 'exit', or 'quit' to end the chat.

## Requirements

- Python 3.x
- OpenAI Python library

## License

This project is licensed under the MIT License.

openai==0.27.0
