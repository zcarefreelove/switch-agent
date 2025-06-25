import unittest
from web_interface.app import SwitchChatbot

class TestSystemIntegration(unittest.TestCase):
    def setUp(self):
        self.bot = SwitchChatbot()
        
    def test_full_flow(self):
        # 模拟用户输入
        message = "请重启192.168.1.1设备"
        chat_history = []
        
        # 执行对话流程
        _, updated_history = self.bot.respond(message, chat_history)
        
        # 验证结果
        self.assertEqual(len(updated_history), 1)
        user_msg, bot_msg = updated_history[0]
        self.assertEqual(user_msg, message)
        self.assertIn("执行命令: reload 192.168.1.1", bot_msg)
        self.assertIn("结果: success", bot_msg)

if __name__ == '__main__':
    unittest.main()