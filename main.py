import streamlit as st
from src.project.components.fetch_news import fetch_news
from src.project.components.generate_blog import generate_blog
from src.project.components.generate_image import generate_image
from src.project.components.publish_blog import publish_to_hashnode
from src.project.components.config import INDIAN_LANGUAGES, get_random_topic
from src.project.components.logging import logger

st.title("📰 AI-Powered News Blog Generator")

city = st.text_input("Enter Region")
topic = st.text_input("Enter a topic to fetch news")
language = st.selectbox("Select language", ["en"] + INDIAN_LANGUAGES)

if st.button("Generate & Publish Blog"):
    logger.info("Blog generation started")

    if not city and not topic:
        st.write("### Selecting a random city and topic...")
        city, topic = get_random_topic()

    logger.info(f"Selected city: {city}, Topic: {topic}")
    st.success(f"Selected: {city} | Topic: {topic}")

    st.write("### Fetching news...")
    news_summary = fetch_news(city + " " + topic, language)
    st.success("News Retrieved!")

    st.write("### Generating blog post...")
    blog_content = generate_blog(news_summary, topic, [], language)

    st.write("## 📝 Generated Blog Post")
    st.markdown(blog_content, unsafe_allow_html=True)

    st.write("### Generating image...")
    image_url = generate_image(topic)
    st.image(image_url, caption="Generated Image")

    st.write("### Publishing to Hashnode...")
    published_url = publish_to_hashnode(city + " " + topic, blog_content, image_url)

    if "Failed" not in published_url:
        st.success(f"✅ Blog Published! [Read here]({published_url})")
    else:
        st.error("❌ Blog publishing failed.")

    logger.info("Blog generation completed")
