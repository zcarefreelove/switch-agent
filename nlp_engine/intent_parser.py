from langchain import PromptTemplate

class IntentParser:
    def __init__(self):
        self.template = """
        你是交换机运维助手，请分析用户指令提取操作意图。
        当前交换机型号：{model}
        ACL规则约束：{acl_rules}
        用户指令：{input}
        操作意图：
        """
        
    def parse_intent(self, model: str, acl_rules: str, input_text: str) -> str:
        prompt = self.template.format(
            model=model,
            acl_rules=acl_rules,
            input=input_text
        )
        # 实际开发时替换为大模型调用
        print("生成的Prompt:", prompt)
        return "reload"  # 示例返回值