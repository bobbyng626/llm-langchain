from langchain.tools import Tool
from langchain.prompts import PromptTemplate
from current_race_data import CurrentRaceData
from prompt_template import PromptTemplateConstructor
from langchain.llms import AzureOpenAI
from langchain.chains import APIChain

class Get_Race_Detail_Tool:
  @classmethod
  def get_tool(cls):
    tool = Tool.from_function(
        name="Get race details",
        func=Get_Race_Detail_Tool.get_race_detail,
        description="If you have race date and race number, use this tool to get race details. Input should be a search query."
    )
    return tool
  @classmethod
  def get_race_detail(cls, query: str = " ") -> str:
    print("Query here: ", query)
    llm = AzureOpenAI(
        deployment_name="gpt-35-turbo",  # text-davinci-003 gpt-35-turbo
        temperature=0
    )
    RACE_DOC = """API documentation:
    Endpoint: https://api-rke-hkjc.agileexlab.net
    GET /race/v3/api/races

    This API is for searching horse race, including race date and number of race, or details of each race.

    Query parameters table:
    Parameter | Type | Description | Required
    ----------|------|-------------|---------
    race_date | string | Race date in YYYY-MM-DD format | Yes
    race_num | integer | Race number | Yes

    =======
    Below is how to read the response of this API. DO NOT put in API query parameter.

    API Response schema (JSON object, field not mentioned is not unless):
    Key | Type | Description
    ----|------|------------
    payload | JSON object | Response payload

    API Response payload schema (JSON object, field not mentioned is unless):
    Key | Type | Description
    ----|------|------------
    raceTime | string | Race time in datetime ISO format
    venue | string | Venue of the race
    raceClass | string | Race class
    distance | integer | Distance of the race
    totalNumOfHorses | integer | Total number of horses in the race
    results | JSON object | Results of the race

    API Results schema (JSON object, field not mentioned is unless):
    Key | Type | Description
    ----|------|------------
    [win|place|quinella|quinellaPlace|forecast|tierce|trio|firstFour|quartet|double] | JSON object | Result for race of each pool and their winning odds
    =======
    EXAMPLE of results and how to read it:
    ```json
    {"place": {"5": 1.45,"6": 1.65,"8": 2.7,"9": 2.85},"tierce": [{"combination": [9,8,5],"odds": 193.5},{"combination": [9,8,6],"odds": 247.6}]}'
    ```
    1. In "place", each key is horse number and value is the winning odds.
    In the example, horse number 5 has winning odds of 1.45, horse number 6 has winning odds of 1.65, and so on.
    2. In "tierce", the element is a list of JSON object with "combination" (a list of horse number) and "odds" fields for each winning combination.
    In the example, horse number 9, 8, 5 has winning odds of 193.5, horse number 9, 8, 6 has winning odds of 247.6.
    """
    
    chain_new = APIChain.from_llm_and_api_docs(llm, RACE_DOC, verbose=True)

    return chain_new.run(query)

    