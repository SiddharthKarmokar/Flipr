import os
from dotenv import load_dotenv
import random

load_dotenv()

API_KEY = os.getenv("HASHNODE_API_KEY")
PUBLICATION_ID = os.getenv("BLOG_ID")
POSTGRES_URL = os.getenv("POSTGRES_URL")
HASHNODE_API_URL = "https://gql.hashnode.com/"

INDIAN_LANGUAGES = ["hi", "bn", "te", "mr", "ta", "ur", "gu", "kn", "ml", "pa", "en"]

CITIES_AND_TOPICS = {
    "Mumbai": "Stock Market Trends",
    "Bangalore": "Tech Startups Growth",
    "Hyderabad": "AI & Machine Learning Innovations",
    "Chennai": "Cyclone Preparedness & Impact",
    "Kolkata": "Heritage Preservation Challenges",
    "Pune": "EV Adoption in India",
    "Jaipur": "Tourism & Cultural Festivals",
    "Ahmedabad": "Smart City Developments",
    "Lucknow": "Food & Street Cuisine Culture",
    "Delhi": "Crime in the city",
}

def get_random_topic():
    return random.choice(list(CITIES_AND_TOPICS.items()))
