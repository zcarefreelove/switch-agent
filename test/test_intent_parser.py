import unittest
from nlp_engine.intent_parser import IntentParser

class TestIntentParser(unittest.TestCase):
    def setUp(self):
        self.parser = IntentParser()
        
    def test_parse_intent(self):
        # 测试正常意图识别
        intent = self.parser.parse_intent(
            "Cisco Catalyst 9200",
            "禁止在高峰时段修改ACL",
            "请重启192.168.1.1设备"
        )
        self.assertEqual(intent, "reload")
        
    def test_unsupported_intent(self):
        # 测试不支持的意图类型
        with self.assertRaises(ValueError):
            self.parser.parse_intent(
                "Cisco Catalyst 9200",
                "禁止在高峰时段修改ACL",
                "请执行未知操作"
            )

if __name__ == '__main__':
    unittest.main()