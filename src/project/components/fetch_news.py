from src.project.components.agents import news_agent
from src.project.components.logging import logger
from deep_translator import GoogleTranslator
from src.project.components.config import INDIAN_LANGUAGES


def fetch_news(topic, language="en"):
    logger.info(f"Fetching news for topic: {topic} in language: {language}")

    try:
        response = news_agent.run(f"Find the latest news articles about {topic} and summarize them. Include sources.")
        news_content = getattr(response, "content", str(response))

        if language in INDIAN_LANGUAGES:
            news_content = GoogleTranslator(source="auto", target=language).translate(news_content)
            logger.info(f"Translated news content to {language}")

        logger.info("Successfully fetched and processed news")
        return news_content
    except Exception as e:
        logger.error(f"Error fetching news: {e}", exc_info=True)
        return "Failed to fetch news."
