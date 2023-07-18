from langchain.tools import Tool
from langchain.prompts import PromptTemplate
from current_race_data import CurrentRaceData
from prompt_template import PromptTemplateConstructor
from langchain.llms import AzureOpenAI

class Generate_Ranking_Tool:
  @classmethod
  def get_tool(cls):
    tool = Tool.from_function(
        name="Generate ranking",
        func=Generate_Ranking_Tool.generate_ranking,
        description="Generate the ranking of all horse in the race"
    )
    return tool
  @classmethod
  def generate_ranking(cls, query: str = " ") -> str:
      print("Queryyyyy", query)
      llm = AzureOpenAI(
          deployment_name="gpt-35-turbo",  # text-davinci-003 gpt-35-turbo
          temperature=0
      )
      print("\n===== generate_ranking =====")
      current_record = CurrentRaceData.current_race_version1
      horse_num = "14"
      prompt = PromptTemplate.from_template(PromptTemplateConstructor.prompt_template_version1)
      formatted_prompt = prompt.format(current_record=current_record, horse_num=horse_num)

      return llm(formatted_prompt)
    