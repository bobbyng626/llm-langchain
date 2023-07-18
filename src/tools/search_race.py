from langchain.tools import Tool
from langchain.llms import AzureOpenAI

class Search_Race_Tool:
  @classmethod
  def get_tool(cls):
    tool = Tool.from_function(
        name="Search race",
        func=Search_Race_Tool.search_race,
        description="If you don't have race date or race number, use this tool to get race date and number of race for each race date."
    )
    return tool
  
  @classmethod
  def search_race(cls, query: str = "") -> str:
      
      llm = AzureOpenAI(
          deployment_name="gpt-35-turbo",  # text-davinci-003 gpt-35-turbo
          temperature=0
      )
      print("\n===== get_race_overview =====")
      json_data = {"2023-04-02": 9, "2023-04-06": 9, "2023-04-09": 11, "2023-04-12": 9, "2023-03-29": 8, "2023-03-26": 10, "2023-03-22": 9, "2023-03-19": 10, "2023-03-15": 9, "2023-03-11": 10, "2023-03-08": 9, "2023-03-05": 10, "2023-03-01": 9, "2023-02-26": 10, "2022-05-04": 5, "2022-05-03": 5, "2022-05-22": 11, "2022-06-01": 9, "2022-05-11": 9, "2022-06-08": 9, "2022-05-25": 9, "2022-05-29": 10, "2022-06-12": 11, "2022-05-18": 9, "2022-05-15": 10, "2022-06-05": 10, "2022-06-19": 10, "2022-06-22": 9, "2022-06-25": 10, "2022-06-28": 8, "2022-07-01": 10, "2022-07-06": 9, "2022-07-10": 10, "2022-07-13": 9, "2022-07-16": 11, "2022-09-11": 10, "2022-09-14": 8, "2022-09-18": 10, "2022-09-21": 8, "2022-09-25": 10, "2022-09-28": 8, "2022-10-01": 10, "2022-10-05": 9, "2022-10-09": 10, "2022-10-12": 9, "2022-10-16": 10, "2022-10-19": 8, "2022-10-23": 10, "2022-10-26": 9, "2022-10-30": 10, "2022-11-02": 8, "2022-11-06": 10, "2022-11-09": 9, "2022-11-12": 10,
                  "2022-11-16": 9, "2022-11-20": 10, "2022-11-23": 8, "2022-11-27": 10, "2022-11-30": 8, "2022-12-04": 10, "2022-12-07": 9, "2022-12-11": 10, "2022-12-14": 9, "2022-12-18": 10, "2022-12-21": 9, "2022-12-24": 10, "2022-12-28": 9, "2023-01-01": 11, "2023-01-04": 9, "2023-01-08": 11, "2023-01-11": 9, "2023-01-15": 10, "2023-01-18": 8, "2023-01-21": 10, "2023-01-24": 11, "2023-01-29": 10, "2023-02-01": 9, "2023-02-05": 10, "2023-02-08": 9, "2023-02-12": 10, "2023-02-15": 9, "2023-02-19": 10, "2023-02-22": 9, "2023-04-15": 10, "2023-04-19": 9, "2023-04-23": 10, "2023-04-26": 9, "2023-04-30": 10, "2023-05-03": 9, "2023-05-07": 11, "2023-05-10": 8, "2023-05-13": 10, "2023-05-17": 9, "2023-05-21": 10, "2023-05-24": 9, "2023-05-28": 11, "2023-05-31": 9, "2023-06-04": 10, "2023-06-07": 9, "2023-06-10": 10, "2023-06-14": 9, "2023-06-18": 11, "2023-06-25": 10, "2023-06-28": 9, "2023-07-01": 10, "2023-07-03": 8, "2023-07-06": 9, "2023-07-09": 11, "2023-07-12": 9, "2023-07-16": 11}
      prompt = f"""You are a helpful AI assistant trained to answer user queries from API responses.
  You attempted to call an API, which resulted in:
  API_RESPONSE: {json_data}

  JSON format:
  1. Each key is a race date in YYYY-MM-DD
  2. value is number of race at that race date

  If the API_RESPONSE can answer the USER_COMMENT respond with the following markdown json block:
  Response: ```json
  {{"response": "Human-understandable synthesis of the API_RESPONSE"}}
  ```

  Otherwise respond with the following markdown json block:
  Response Error: ```json
  {{"response": "What you did and a concise statement of the resulting error. If it can be easily fixed, provide a suggestion."}}
  ```

  You MUST respond as a markdown json code block. The person you are responding to CANNOT see the API_RESPONSE, so if there is any relevant information there you must include it in your response.

  Begin:
  ---
  {query}
  """
      # print(llm(prompt))

      return llm(prompt)
