"""
Tests for Pannu AI Agent
"""

import unittest
from backend.agent import PannuAgent
from backend.tools import (
    CalculatorTool, 
    SearchTool, 
    FileCreatorTool, 
    ConversationTool
)


class TestAgent(unittest.TestCase):
    """Test the main agent"""
    
    def setUp(self):
        """Setup before each test"""
        self.agent = PannuAgent()
    
    def test_agent_initialization(self):
        """Test agent initializes correctly"""
        self.assertEqual(self.agent.name, "Pannu")
        self.assertEqual(len(self.agent.memory), 0)
    
    def test_memory_storage(self):
        """Test that memory stores correctly"""
        self.agent.add_memory("user", "Test message")
        self.assertEqual(len(self.agent.memory), 1)
        self.assertEqual(self.agent.memory[0]["role"], "user")
    
    def test_understand_calculator_prompt(self):
        """Test prompt understanding for calculator"""
        analysis = self.agent.understand_prompt("calculate 5 + 3")
        self.assertEqual(analysis["tool_needed"], "calculator")
    
    def test_understand_search_prompt(self):
        """Test prompt understanding for search"""
        analysis = self.agent.understand_prompt("search Python")
        self.assertEqual(analysis["tool_needed"], "search")
    
    def test_understand_conversation_prompt(self):
        """Test prompt understanding for conversation"""
        analysis = self.agent.understand_prompt("Hello")
        self.assertEqual(analysis["tool_needed"], "conversation")


class TestCalculatorTool(unittest.TestCase):
    """Test calculator tool"""
    
    def test_simple_addition(self):
        """Test simple addition"""
        result = CalculatorTool.execute("calculate 5 + 3")
        self.assertIn("8", result)
    
    def test_multiplication(self):
        """Test multiplication"""
        result = CalculatorTool.execute("calculate 10 * 2")
        self.assertIn("20", result)
    
    def test_invalid_calculation(self):
        """Test invalid calculation returns error"""
        result = CalculatorTool.execute("calculate abc + def")
        self.assertIn("couldn't calculate", result.lower())


class TestConversationTool(unittest.TestCase):
    """Test conversation tool"""
    
    def test_hello_response(self):
        """Test hello response"""
        result = ConversationTool.execute("Hello")
        self.assertIn("Hi", result)
    
    def test_who_are_you_response(self):
        """Test who are you response"""
        result = ConversationTool.execute("Who are you?")
        self.assertIn("Pannu", result)


if __name__ == "__main__":
    unittest.main()
