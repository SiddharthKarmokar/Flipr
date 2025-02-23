import requests
from src.project.components.config import API_KEY, PUBLICATION_ID, HASHNODE_API_URL
from src.project.components.logging import logger

PUBLISH_POST_MUTATION = """
mutation PublishPost($input: PublishPostInput!) {
    publishPost(input: $input) {
        post {
            id
            title
            slug
            url
        }
    }
}
"""

def publish_to_hashnode(title, content, image_url):
    logger.info(f"Publishing blog: {title}")

    headers = {
        "Content-Type": "application/json",
        "Authorization": API_KEY,
    }
    payload = {
        "query": PUBLISH_POST_MUTATION,
        "variables": {
            "input": {
                "publicationId": PUBLICATION_ID,
                "title": title,
                "contentMarkdown": content,
                "coverImageOptions": {"coverImageURL": image_url.rstrip("\\/").replace(" ", "")},
                "disableComments": False
            }
        },
    }

    try:
        response = requests.post(HASHNODE_API_URL, json=payload, headers=headers)
        if response.status_code == 200:
            blog_url = response.json().get("data", {}).get("publishPost", {}).get("post", {}).get("url", "Error")
            logger.info(f"Blog successfully published: {blog_url}")
            return blog_url
        else:
            logger.error(f"Failed to publish blog: {response.text}")
            return "Failed to publish blog."
    except Exception as e:
        logger.error(f"Error publishing blog: {e}", exc_info=True)
        return "Error in publishing."
