# from langchain.tools import Tool
# from langchain.prompts import PromptTemplate
# from current_race_data import CurrentRaceData
# from prompt_template import PromptTemplateConstructor
# from langchain.llms import AzureOpenAI

# class Race_Prompt_Tool:
#   @classmethod
#   def get_tool(cls):
#     tool = Tool.from_function(
#         name="Construct race prompt",
#         func=Race_Prompt_Tool.construct_prompt,
#         description="Take race detail to generate prompt for ranking"
#     )
#     return tool
#   @classmethod
#   def construct_prompt(cls, query: str = " ") -> str:
#       print("\n Prompt Query: ", query)
#       llm = AzureOpenAI(
#           deployment_name="gpt-35-turbo",  # text-davinci-003 gpt-35-turbo
#           temperature=0
#       )
#       print("\n===== construct_prompt =====")
#       prompt = PromptTemplate.from_template(PromptTemplateConstructor.prompt_template_version1)
#       formatted_prompt = prompt.format(current_record=current_record, horse_num=horse_num)

#       return llm(formatted_prompt)
    