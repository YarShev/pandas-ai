"""Example of using PandasAI with a Parquet file."""

from pandasai import Agent
from pandasai.llm import OpenAI

llm = OpenAI()

agent = Agent(["examples/data/Loan payments data.parquet"], config={"llm": llm})
response = agent.chat("How many loans are from men and have been paid off?")
print(response)
# Output: 247 loans have been paid off by men.
