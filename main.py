"""
Pannu AI Agent - Main CLI Interface
Simple command-line interface to interact with the agent
"""

import sys
import logging
from backend.agent import PannuAgent
from backend.config import AGENT_NAME, AGENT_VERSION

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def print_banner():
    """Print welcome banner"""
    banner = f"""
╔════════════════════════════════════════╗
║         🤖 {AGENT_NAME} AI Agent v{AGENT_VERSION}        ║
║                                        ║
║  Your intelligent digital companion   ║
╚════════════════════════════════════════╝
    """
    print(banner)


def print_help():
    """Print help information"""
    help_text = """
📚 Commands:
  help       - Show this help message
  memory     - Show conversation history
  clear      - Clear conversation memory
  save       - Save memory to file
  exit/quit  - Close the agent

💡 Try these:
  "Hi Pannu"
  "Calculate 5 + 3"
  "Search Python"
  "Create file test.txt with content Hello"
    """
    print(help_text)


def main():
    """Main function - Run the agent"""
    print_banner()
    print("Type 'help' for commands or just talk to me!\n")
    
    # Initialize agent
    agent = PannuAgent(name=AGENT_NAME)
    
    # Main loop
    while True:
        try:
            # Get user input
            user_input = input("👤 You: ").strip()
            
            # Empty input
            if not user_input:
                continue
            
            # Handle special commands
            if user_input.lower() in ["exit", "quit"]:
                print("\n👋 Goodbye! Thanks for using Pannu!\n")
                break
                
            elif user_input.lower() == "help":
                print_help()
                continue
                
            elif user_input.lower() == "memory":
                print("\n📝 Conversation Memory:")
                print("=" * 50)
                for entry in agent.get_memory():
                    print(f"{entry['role'].upper()}: {entry['content']}")
                print("=" * 50 + "\n")
                continue
                
            elif user_input.lower() == "clear":
                agent.clear_memory()
                print("✅ Memory cleared!\n")
                continue
                
            elif user_input.lower() == "save":
                agent.save_memory("memory.json")
                print("✅ Memory saved to memory.json!\n")
                continue
            
            # Process prompt
            response = agent.process_prompt(user_input)
            print(f"🤖 Pannu: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!\n")
            break
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            print(f"❌ Error: {str(e)}\n")


if __name__ == "__main__":
    main()
