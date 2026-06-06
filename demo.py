"""
Hermes Agent Python Wrapper Demo
================================
这是一个展示如何通过 Python 程序化调用 Hermes Agent 的示例代码。
注意：Hermes Agent 主要通过 CLI 使用，此示例展示 API 调用模式。

This is a demo showing how to programmatically interact with Hermes Agent.
Note: Hermes Agent is primarily CLI-based; this demo shows the API calling pattern.
"""

import json
import subprocess
import sys
from typing import Optional, List, Dict, Any


class HermesAgent:
    """
    Hermes Agent Python 封装类
    用于通过 Python 代码与 Hermes Agent 进行交互
    
    Hermes Agent Python Wrapper
    For interacting with Hermes Agent via Python code.
    """
    
    def __init__(self, model: str = "openai:gpt-4o", provider: Optional[str] = None):
        """
        初始化 Hermes Agent
        
        Args:
            model: 模型名称，格式为 provider:model_name
                  Model name in format provider:model_name
                  示例 / examples: "openai:gpt-4o", "openrouter:anthropic/claude-3-5-sonnet"
            provider: 可选，提供者名称（已在模型中指定则无需填写）
                     Optional provider name (not needed if specified in model)
        """
        self.model = model
        self.provider = provider
        self.conversation_history: List[Dict[str, str]] = []
    
    def chat(self, message: str, tools: Optional[List[str]] = None) -> str:
        """
       发送消息并获取回复
        Send a message and get a response.
        
        Args:
            message: 用户消息 / User message
            tools: 可选，启用的工具列表 / Optional list of enabled tools
            
        Returns:
            Agent 的回复文本 / Agent's response text
        """
        # 构建命令
        cmd = ["hermes", "chat", "--model", self.model]
        
        if tools:
            cmd.extend(["--tools", ",".join(tools)])
        
        try:
            # 执行命令并获取输出
            result = subprocess.run(
                cmd,
                input=message,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode != 0:
                return f"Error: {result.stderr}"
            
            return result.stdout.strip()
        
        except subprocess.TimeoutExpired:
            return "Error: Request timed out"
        except FileNotFoundError:
            return "Error: Hermes not installed. Run: curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def set_model(self, model: str) -> None:
        """
        切换模型
        Switch the active model.
        
        Args:
            model: 新的模型名称 / New model name
        """
        self.model = model
    
    def reset(self) -> None:
        """
        重置对话历史
        Reset conversation history.
        """
        self.conversation_history = []
    
    def get_history(self) -> List[Dict[str, str]]:
        """
        获取对话历史
        Get conversation history.
        
        Returns:
            对话历史列表 / List of conversation history
        """
        return self.conversation_history


def demo_basic_chat():
    """
    基础对话演示
    Basic chat demo.
    """
    print("=" * 60)
    print("Hermes Agent - 基础对话演示 / Basic Chat Demo")
    print("=" * 60)
    
    agent = HermesAgent(model="openai:gpt-4o")
    
    messages = [
        "你好，请用一句话介绍自己",
        "你支持哪些模型提供商？",
        "用 Python 写一个快速排序算法"
    ]
    
    for msg in messages:
        print(f"\n👤 用户: {msg}")
        print("🤖 Agent: ", end="")
        response = agent.chat(msg)
        print(response[:200] + "..." if len(response) > 200 else response)


def demo_tool_usage():
    """
    工具使用演示
    Tool usage demo.
    """
    print("\n" + "=" * 60)
    print("Hermes Agent - 工具使用演示 / Tool Usage Demo")
    print("=" * 60)
    
    agent = HermesAgent(model="openai:gpt-4o")
    
    print("\n👤 用户: 帮我搜索今天的热点新闻")
    print("🤖 Agent: ", end="")
    
    response = agent.chat(
        "帮我搜索今天的热点新闻",
        tools=["web_search"]
    )
    print(response[:300] + "..." if len(response) > 300 else response)


def demo_model_switch():
    """
    模型切换演示
    Model switching demo.
    """
    print("\n" + "=" * 60)
    print("Hermes Agent - 模型切换演示 / Model Switch Demo")
    print("=" * 60)
    
    models = [
        ("openai:gpt-4o", "OpenAI GPT-4o"),
        ("openrouter:anthropic/claude-3-5-sonnet", "Anthropic via OpenRouter"),
    ]
    
    for model_id, model_name in models:
        agent = HermesAgent(model=model_id)
        print(f"\n🔄切换到 / Switched to: {model_name}")
       print("👤 用户: 你好")
        print("🤖 Agent: ", end="")
        response = agent.chat("用一句话介绍自己")
        print(response[:100] + "..." if len(response) > 100 else response)


def demo_batch_processing():
    """
    批量处理演示
    Batch processing demo.
    """
    print("\n" + "=" * 60)
    print("Hermes Agent - 批量处理演示 / Batch Processing Demo")
    print("=" * 60)
    
    agent = HermesAgent(model="openai:gpt-4o")
    
    tasks = [
        "解释什么是递归算法",
        "用 Python 写一个斐波那契数列函数",
        "推荐三本程序员必读的书籍"
    ]
    
    print("\n📋 批量任务列表 / Batch Task List:")
    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task}")
    
    print("\n🚀 开始批量处理 / Starting batch processing...")
    results = []
    
    for i, task in enumerate(tasks, 1):
        print(f"\n[{i}/{len(tasks)}] 处理中 / Processing: {task[:30]}...")
        response = agent.chat(task)
        results.append({"task": task, "response": response})
        print(f"✅ 完成 / Done")
    
    print("\n" + "-" * 60)
    print("📊 批量处理结果 / Batch Results:")
    print("-" * 60)
    
    for i, result in enumerate(results, 1):
        print(f"\n任务 {i}: {result['task']}")
        print(f"回复: {result['response'][:150]}...")


def demo_skill_creation():
    """
    技能创建演示
    Skill creation demo.
    """
    print("\n" + "=" * 60)
    print("Hermes Agent - 技能创建演示 / Skill Creation Demo")
    print("=" * 60)
    
    print("""
Hermes Agent 支持用户自定义技能（Skills）。
Hermes Agent supports user-defined skills.

技能示例 / Skill Example:
---
name: code-reviewer
description: 自动化代码审查技能
triggers:
  - "/review"
  - "帮我审查代码"
actions:
  - type: python
    script: |
      # 代码审查逻辑
      pass
---
    """)
    
    print("\n📝 创建技能 / Creating a skill:")
    print("""
# 在 CLI 中使用以下命令创建技能
# Use the following CLI command to create a skill:
hermes skills create code-reviewer

# 查看所有技能 / View all skills:
hermes skills list

# 使用技能 / Use a skill:
hermes /code-reviewer
    """)


def main():
    """
    主函数 - 运行所有演示
    Main function - Run all demos.
    """
    print("""
╔══════════════════════════════════════════════════════════╗
║           Hermes Agent Python Wrapper Demo              ║
║           Hermes Agent Python 封装示例║
╚══════════════════════════════════════════════════════════╝
    """)
    
    print("⚠️  注意: 请确保已安装 Hermes Agent")
    print("⚠️  Note: Please ensure Hermes Agent is installed")
    print("    安装命令 / Install: curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash\n")
    
    try:
        # 检查 Hermes 是否已安装
        result = subprocess.run(
            ["hermes", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print(f"✅ Hermes 已安装 / Hermes installed: {result.stdout.strip()}\n")
        else:
            print("⚠️  Hermes 未安装，将显示模拟输出 / Hermes not installed, showing mock output\n")
    except FileNotFoundError:
        print("⚠️  Hermes 未找到，请先安装 / Hermes not found, please install first\n")
       print("📋 以下演示将显示模拟输出 / Following demos will show mock output\n")
    
    # 运行演示
    demo_basic_chat()
    demo_tool_usage()
    demo_model_switch()
    demo_batch_processing()
    demo_skill_creation()
    
    print("\n" + "=" * 60)
    print("演示完成！了解更多请访问：")
    print("Demo complete! Learn more at:")
    print("https://hermes-agent.nousresearch.com/docs/")
    print("=" * 60)


if __name__ == "__main__":
    main()