#
#  Subscribe: https://youtube.com/@codewithyub
#

import gradio as gr

def chat_bot_logic(message: str, converstion: list) -> str:

    message = message.lower()

    default_response = "Hello, I am code with yubraj chatbot. How can I help you?"

    if message in ["what is your name", "tell me your name", "what can i call you"]:
        return default_response
    
    elif message in ["hello", "hi", "hiiii"]:
        return default_response
    
    elif message in ["how can i subscribe your channel", "your channel handle"]:
        return "You can subscribe code with yubraj using https://youtube.com/@codewithyub."
    
    else:
        return "Sorry, I can't process you as of now. Try again."


if __name__ == "__main__":
    chat_bot = gr.ChatInterface(
        chat_bot_logic,
        title="Chat bot of code with yubraj",
        description="This chatbot is awesome"
    )

    chat_bot.launch()