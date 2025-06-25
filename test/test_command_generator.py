import unittest
from command_generator.command_generator import CommandGenerator

class TestCommandGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = CommandGenerator()
        
    def test_generate_reload_command(self):
        # 测试生成重启命令
        command = self.generator.generate_command(
            "reload",
            {"ip": "192.168.1.1"}
        )
        self.assertEqual(command, "reload 192.168.1.1")
        
    def test_apply_network_rules(self):
        # 测试应用网络规则（备份配置）
        enhanced_cmd = self.generator.apply_network_rules(
            "reload 192.168.1.1",
            "变更前需进行配置备份"
        )
        expected = "copy running-config startup-config\nreload 192.168.1.1"
        self.assertEqual(enhanced_cmd, expected)

if __name__ == '__main__':
    unittest.main()