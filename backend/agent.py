"""
Pannu AI Agent - The Core Brain
Handles prompts, reasoning, and tool execution
"""

import json
import logging
from datetime import datetime
from typing import Any, Dict, List
from backend.tools import get_tool

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PannuAgent:
    """
    Simple AI Agent that:
    1. Receives a prompt from user
    2. Understands what to do
    3. Executes actions (tools)
    4. Returns results
    """
    
    def __init__(self, name: str = "Pannu"):
        """
        Initialize the agent
        
        Args:
            name: Agent name
        """
        self.name = name
        self.memory = []  # Store conversation history
        logger.info(f"✅ {self.name} Agent initialized")
        
    def add_memory(self, role: str, content: str) -> None:
        """
        Store conversation in memory
        
        Args:
            role: "user" or "agent"
            content: The message
        """
        memory_entry = {
            "timestamp": datetime.now().isoformat(),
            "role": role,
            "content": content
        }
        self.memory.append(memory_entry)
        
    def understand_prompt(self, prompt: str) -> Dict[str, Any]:
        """
        Analyze the user's prompt and decide what to do
        
        Args:
            prompt: User's input text
            
        Returns:
            Dictionary with analysis
        """
        prompt_lower = prompt.lower()
        
        analysis = {
            "original_prompt": prompt,
            "timestamp": datetime.now().isoformat(),
            "tool_needed": None
        }
        
        # Check what the user wants to do using keywords
        if any(word in prompt_lower for word in ["calculate", "math", "add", "subtract", "multiply", "divide", "plus", "minus", "times"]):
            analysis["tool_needed"] = "calculator"
            
        elif any(word in prompt_lower for word in ["search", "google", "find", "info about", "look for"]):
            analysis["tool_needed"] = "search"
            
        elif any(word in prompt_lower for word in ["create file", "write file", "save", "new file"]):
            analysis["tool_needed"] = "file_creator"
            
        elif any(word in prompt_lower for word in ["hello", "hi", "hey", "how are you", "who are you", "what are you"]):
            analysis["tool_needed"] = "conversation"
            
        else:
            analysis["tool_needed"] = "general"
            
        logger.info(f"📊 Tool needed: {analysis['tool_needed']}")
        return analysis
        
    def execute_tool(self, tool_name: str, prompt: str) -> str:
        """
        Execute a tool
        
        Args:
            tool_name: Name of the tool to execute
            prompt: The user's prompt to pass to the tool
            
        Returns:
            Result from the tool
        """
        try:
            logger.info(f"🔨 Executing tool: {tool_name}")
            tool_function = get_tool(tool_name)
            result = tool_function(prompt)
            return result
        except Exception as e:
            logger.error(f"❌ Tool execution failed: {str(e)}")
            return f"Error executing tool: {str(e)}"
    
    def process_prompt(self, user_prompt: str) -> str:
        """
        Main function: Process user prompt and return response
        
        Args:
            user_prompt: What the user asks
            
        Returns:
            Response from agent
        """
        logger.info(f"👤 User: {user_prompt}")
        
        # Add to memory
        self.add_memory("user", user_prompt)
        
        # Understand the prompt
        analysis = self.understand_prompt(user_prompt)
        
        # Execute the appropriate tool
        tool_needed = analysis["tool_needed"]
        result = self.execute_tool(tool_needed, user_prompt)
        
        # Add response to memory
        self.add_memory("agent", result)
        
        logger.info(f"🤖 Agent: {result}")
        return result
    
    def get_memory(self) -> List[Dict]:
        """Get all stored conversations"""
        return self.memory
    
    def clear_memory(self) -> None:
        """Clear conversation history"""
        self.memory = []
        logger.info("🧹 Memory cleared")
    
    def save_memory(self, filename: str = "memory.json") -> None:
        """
        Save memory to a JSON file
        
        Args:
            filename: Where to save
        """
        try:
            with open(filename, "w") as f:
                json.dump(self.memory, f, indent=2)
            logger.info(f"💾 Memory saved to {filename}")
        except Exception as e:
            logger.error(f"❌ Error saving memory: {str(e)}")


if __name__ == "__main__":
    # Simple test
    agent = PannuAgent()
    print(agent.process_prompt("Hi!"))
