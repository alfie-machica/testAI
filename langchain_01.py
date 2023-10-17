##workaround
import os
os.environ['OPENAI_API_KEY'] = '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'

print ("discontinued since API key is not free")
##https://python.langchain.com/docs/modules/agents/
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0)

from langchain.agents import tool

@tool
def get_word_length(word: str) -> int:
    """Returns the length of the given word"""
    return len(word)

# print (get_word_length("test"))
tools = [get_word_length]

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are very powerful assistant, but bad at calculating lengths of words."),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

from langchain.tools.render import format_tool_to_openai_function
llm_with_tools = llm.bind(
    functions=[format_tool_to_openai_function(t) for t in tools]
)

from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
agent = {
    "input": lambda x: x["input"],
    "agent_scratchpad": lambda x: format_to_openai_functions(x['intermediate_steps'])
} | prompt | llm_with_tools | OpenAIFunctionsAgentOutputParser()

agent.invoke({
    "input": "how many letters in the word educa?",
    "intermediate_steps": []
})

print ("done")