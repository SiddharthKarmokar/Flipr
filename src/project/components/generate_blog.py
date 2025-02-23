from src.project.components.agents import blog_writer
from src.project.components.logging import logger
from deep_translator import GoogleTranslator
from src.project.components.config import INDIAN_LANGUAGES

def generate_blog(summary, topic, sources, language="en"):
    logger.info(f"Generating blog for topic: {topic}")

    try:
        blog_prompt = f"Write a blog post on '{topic}' using this summary:\n\n{summary}"
        response = blog_writer.run(blog_prompt)
        blog_content = getattr(response, "content", str(response))

        if language in INDIAN_LANGUAGES:
            blog_content = GoogleTranslator(source="auto", target=language).translate(blog_content)
            logger.info(f"Translated blog content to {language}")

        logger.info("Blog successfully generated")
        return blog_content
    except Exception as e:
        logger.error(f"Error generating blog: {e}", exc_info=True)
        return "Failed to generate blog."
