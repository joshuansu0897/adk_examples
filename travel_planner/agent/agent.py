from google.adk.agents import Agent

AGENT_MODEL = "gemini-2.5-flash"

root_agent = Agent(
    name="travel_planner",
    model=AGENT_MODEL,
    description="A travel planner agent that helps users plan their trips and provides recommendations.",
    instruction="""You are a travel planner agent that helps users plan their trips and provides recommendations. You can assist with finding flights, hotels, and activities based on user preferences. You can also provide travel tips and advice.""",
)
