"""
Configuration file for Pannu AI Agent
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Agent Settings
AGENT_NAME = "Pannu"
AGENT_VERSION = "0.1.0"

# Paths
DATA_DIR = "data"
LOG_DIR = "logs"

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Memory
MEMORY_ENABLED = True
MAX_MEMORY_ITEMS = 100

print("✅ Config loaded successfully!")
