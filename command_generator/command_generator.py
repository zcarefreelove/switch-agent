class CommandGenerator:
    def __init__(self):
        self.rule_templates = {
            "reload": "确认执行设备重启操作吗？{device_ip}"
        }
    
    def generate_command(self, intent: str, device_info: dict) -> str:
        # 根据意图生成具体命令
        if intent == "reload":
            return f"reload {device_info['ip']}"
        raise ValueError(f"不支持的意图类型: {intent}")

    def apply_network_rules(self, command: str, rules: str) -> str:
        # 应用网络操作规则
        if "backup" in rules and "reload" in command:
            return f"copy running-config startup-config\n{command}"
        return command