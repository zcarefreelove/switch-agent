import gradio as gr

with gr.Blocks(css=".user-msg {background-color: #DCF8C6} .bot-msg {background-color: #E9E9E9}") as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    
    def respond(message, chat_history):
        bot_message = "Echo: " + message
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()