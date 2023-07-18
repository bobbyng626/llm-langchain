# IHR Data source
from prompt_template import PromptTemplateConstructor
from current_race_data import CurrentRaceData
# Langchain
from langchain import ConversationChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import get_openai_callback
from langchain.llms import AzureOpenAI
from tools.generate_ranking import Generate_Ranking_Tool
from tools.search_race import Search_Race_Tool
from tools.get_race_detail import Get_Race_Detail_Tool
from dotenv import load_dotenv
import os

load_dotenv('.env')
os.environ["OPENAI_API_KEY"] = "5e6932d5b7e443609491cc0fdc9abc06"
def construct_prompt():
  ### TODO: Load from VectorDB / User Input
  current_record = CurrentRaceData.current_race_version1
  horse_num = "14"
  prompt = PromptTemplate.from_template(PromptTemplateConstructor.prompt_template_version1)
  formatted_prompt = prompt.format(current_record=current_record, horse_num=horse_num)
  return formatted_prompt

def create_llm():
  llm = AzureOpenAI(
      deployment_name="text-davinci-003",  # text-davinci-003 gpt-35-turbo
      temperature=0
  )
  return llm

def start_conversation():
  llm = create_llm()
  conversation = ConversationChain(llm=llm, verbose=True)
  conversation_result = conversation.run(construct_prompt())
  print(conversation_result)

def ranking_agent():
  llm = create_llm()
  tools = [
          Generate_Ranking_Tool.get_tool(),
           Search_Race_Tool.get_tool(),
           Get_Race_Detail_Tool.get_tool()]
  agent = initialize_agent(
      tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
  )
  with get_openai_callback() as cb:
      agent.run("Can I have a generated ranking for 2023-07-16 race 1?")
# start_conversation()
ranking_agent()