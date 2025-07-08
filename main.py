from agents import Agent, Runner
from connection import config
import os

# define individual translator agent

urdu_agent = Agent(
    name='Urdu agent',
    instructions='translate any English text into Urdu.',
    
)

italian_agent = Agent(
    name='Italian agent',
    instructions='translate any english  text into Italian..'

)

arabic_Agent = Agent(
    name='Arabic agent',
    instructions='translate any english text into Arabic.'
)

# define a main agent that will use the individual translator agents
main_agent = Agent(
    name='Translator Router',
    instructions="""
You are a translator router agent. Your task is to route the translation request to the appropriate translator agent based on the language specified in the input.
You have three translator agents: Urdu agent, Italian agent, and Arabic agent. Each agent is specialized in translating English text into a specific language.
When you receive a translation request, you should determine
the language specified in the input and route the request to the appropriate translator agent.
""",
    tools=[
        # convert this agent into as a  tool so that it can be used in the main agent
         urdu_agent.as_tool(
             tool_name='translate_to_urdu',
             tool_description='Translate the user input into Urdu.'
         ),
         italian_agent.as_tool(
             tool_name='translate_to_italian',
             tool_description='Translate the user input into Italian.'
         ),
         arabic_Agent.as_tool(
             tool_name='translate_to_arabic',
             tool_description='Translate the user input into Arabic.'
         )
    ]
)

# run the main agent with the input and config
res = Runner.run_sync(
    arabic_Agent,
    input='translate this text into Arabic: Hello, how are you?',
    run_config=config
    
)
# print the result
print(res.final_output)