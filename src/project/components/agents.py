from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.storage.agent.postgres import PgAgentStorage
from phi.model.groq import Groq
from src.project.components.config import POSTGRES_URL

news_storage = PgAgentStorage(table_name="news_agent", db_url=POSTGRES_URL)
blog_storage = PgAgentStorage(table_name="blog_writer", db_url=POSTGRES_URL)

news_agent = Agent(
    name="News Scraper",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    storage=news_storage,
    instructions=["Fetch and summarize the latest news articles on a given topic, and provide source links."],
    show_tool_calls=True,
    markdown=True,
)

blog_writer = Agent(
    name="Blog Writer",
    model=Groq(id="llama-3.3-70b-versatile"),
    storage=blog_storage,
    instructions=[
        "Write a well-structured blog post on the given topic using the provided summary and sources.",
        "Ensure the blog includes an introduction, key takeaways, and a conclusion.",
        "Ensure to add a section of source links of the News from where the data has been taken.",
    ],
    markdown=True,
)
