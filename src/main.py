from dotenv import load_dotenv
import os
load_dotenv(".env")
from langchain import ConversationChain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import AgentType, initialize_agent, load_tools

### Pratice 1: Use OPENAI Query
def task1_openai():
  llm = OpenAI(temperature=0.9)
  llm_result = llm.predict("What would be a good company name for a company that makes colorful socks?")
  print(llm_result)
  # >> Feetful of Fun

def task2_chat():
  chat = ChatOpenAI(temperature=0)
  chat_result = chat.predict_messages([HumanMessage(content="Translate this sentence from English to French. I love programming.")])
  print(chat_result)
  # >> AIMessage(content="J'aime programmer.", additional_kwargs={})

def task3_prompt():
  prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
  prompt.format(product="colorful socks")
  print(prompt.template)

def task4_chains():
  prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
  prompt.format(product="colorful socks")
  llm = OpenAI(temperature=0.9)
  chain = LLMChain(llm=llm, prompt=prompt)
  chain.run("colorful socks")
  print(chain)

def task5_agents():
  # The language model we're going to use to control the agent.
  llm = OpenAI(temperature=0)

  # The tools we'll give the Agent access to. Note that the 'llm-math' tool uses an LLM, so we need to pass that in.
  tools = load_tools(["serpapi", "llm-math"], llm=llm)

  # Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
  agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

  # Let's test it out!
  agent_result = agent.run("What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?")
  print(agent_result)

def task6_memory():
  llm = OpenAI(temperature=0)
  conversation = ConversationChain(llm=llm, verbose=True)

  conversation_result = conversation.run("Hi there!")
  print(conversation_result) #str

# print("========Task 1=======")
# task1_openai()
# print("========Task 2=======")
# task2_chat()
# print("========Task 3=======")
# task3_prompt()
# print("========Task 4=======")
# task4_chains()
print("========Task 5=======")
task5_agents()
print("========Task 6=======")
task6_memory()