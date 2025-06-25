import gradio as gr
from nlp_engine.intent_parser import IntentParser
from command_generator.command_generator import CommandGenerator
from ssh_connector.ssh_client import SSHClient

class SwitchChatbot:
    def __init__(self):
        self.intent_parser = IntentParser()
        self.command_generator = CommandGenerator()
        self.ssh_client = SSHClient("192.168.1.1", "admin", "password")
        
    async def respond(self, message, chat_history):
        # 解析ACL规则（示例）
        acl_rules = "禁止在高峰时段修改ACL"
        
        # 提取意图
        intent = self.intent_parser.parse_intent("Cisco Catalyst 9200", acl_rules, message)
        
        # 生成命令
        command = self.command_generator.generate_command(intent, {"ip": "192.168.1.1"})
        
        # 执行命令
        result = self.ssh_client.execute(command)
        
        # 返回结果
        bot_message = f"执行命令: {command}\n结果: {result}"
        chat_history.append((message, bot_message))
        return "", chat_history

# 创建界面
with gr.Blocks(css=".user-msg {background-color: #DCF8C6} .bot-msg {background-color: #E9E9E9}") as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    
    bot = SwitchChatbot()
    msg.submit(bot.respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()