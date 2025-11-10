import os
import json
import logging
import sys
from dotenv import load_dotenv
from deepagents import create_deep_agent
from langchain_openai import ChatOpenAI
from tools import *

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
RECURSION_LIMIT = int(os.getenv("RECURSION_LIMIT", 25))

# Define model
load_dotenv()
OPENAI_MODEL=os.getenv("OPENAI_MODEL", "gpt-5-mini")
model= ChatOpenAI(model=OPENAI_MODEL)

# Define Tools
tools=[get_stock_price, get_financial_statements, get_technical_indicators]

if web_search:
  tools.extend([search_financial_news, search_market_trends])
  logging.info("Web search enabled")
else:
  logging.info("Web search disabled")
  
# Load Core Instructions
with open("instructions.md","r") as file:
    CORE_INSTRUCTIONS = file.read()

# Load subagents
with open("subagents.json", "r") as file:
    subagents_config = json.load(file)
fundamental_analyst = subagents_config["fundamental_analyst"]
technical_analyst = subagents_config["technical_analyst"]
risk_analyst = subagents_config["risk_analyst"]

# Create Main agent
agent=create_deep_agent(
    model=model,
    tools=tools,
    subagents=[fundamental_analyst, technical_analyst, risk_analyst],
    instructions=CORE_INSTRUCTIONS, # ?? Workflow-level prompt file
).with_config({"recursion_limit": RECURSION_LIMIT}) # Prevents infinite recursive calls in DeepAgents/LangGraph graphs

# system_prompt	- Role/personality for single-agent chains	-  Use for plain OpenAI/LangChain
# instructions - Workflow-level prompt file - Keep if using DeepAgents; move to system_prompt otherwise