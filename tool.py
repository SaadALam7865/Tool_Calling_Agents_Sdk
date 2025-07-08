from agents import Agent, Runner, function_tool
from main import config
import os
from dotenv import load_dotenv
import requests

load_dotenv()
weather_api_key = os.getenv('WEATHER_API_KEY')

# use tool to run the agent with a specific agent n input
@function_tool
def get_weather(city: str):
    response = requests.get(f'https://api.weatherstack.com/current?access_key={weather_api_key}&query={city}')
    data = response.json()
    if 'current' in data and 'temperature' in data['current']:
        return f'The current temperature in {city} is {data['current']['temperature']}°C. with weather description: {data['current']['weather_descriptions'][0]}.'
    else:
        return f'Could not retrieve weather data for {city}. Please check the city name or try again later.'
    
# use the tool in the agent 
agent = Agent(name='personal assistant', 
             instructions='you are a helpful assistant, your task is to help the user with their queries..',
             tools=[get_weather])

# run the agent with the input and config
res = Runner.run_sync(
    agent,
    input='what are the currnten weather in Indonesia  Jakarta?',
    run_config=config
    
)
print(res.final_output)