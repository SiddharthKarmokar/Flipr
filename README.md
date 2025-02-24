# Agentic AI News Blog Generator
This repository contains a Streamlit-based application that fetches news, generates blog posts, creates relevant images, and publishes them to Hashnode. The application supports multiple Indian languages and allows users to input a city and topic to generate a blog post automatically.

## 🔗 Deployed Link On AWS (Available for 1 week)
[Agentic AI](http://34.235.166.71:8501)
## 📺 Demo Video
[![Agentic AI News Blog Generator Demo](https://img.youtube.com/vi/muD9uB3_1ao/0.jpg)](https://www.youtube.com/watch?v=muD9uB3_1ao)

Click the image above to watch the demo video!

---
## 📂 Project Structure
```
.
├── Dockerfile                # Configuration for containerization
├── LICENSE                   # License file
├── README.md                # Project documentation (this file)
├── app.py                    # Alternative entry point for the application
├── logs/                      # Stores log files
│   ├── continuous_logs.log    # Log file for debugging and tracking
├── main.py                   # Main script to run the Streamlit app
├── requirements.txt           # List of dependencies
├── src/                       # Source code directory
│   ├── **init**.py            # Marks src as a package
│   ├── project/               # Core project module
│   │   ├── **init**.py        # Marks project as a package
│   │   ├── components/        # Contains all major components of the app
│   │   │   ├── **init**.py    # Marks components as a package
│   │   │   ├── agents.py      # News agent and Blog writer agent
│   │   │   ├── config/        # Configuration files
│   │   │   │   ├── **init**.py
│   │   │   ├── fetch_news.py  # Functionality for fetching news
│   │   │   ├── generate_blog.py # Generates blog posts using fetched news
│   │   │   ├── generate_image.py # Generates images for blogs
│   │   │   ├── logging/       # Logging utility
│   │   │   │   ├── **init**.py
│   │   │   ├── publish_blog.py # Publishes the blog to Hashnode
│   │   ├── **pycache**/       # Cached compiled Python files
│   ├── **pycache**/          # Cached compiled Python files
├── template.py               # Template script (possibly unused)
```
---
## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/SiddharthKarmokar/Flipr.git
cd your-repo
```
### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```
### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 4️⃣ Set Up PostgreSQL with pgvector (Required)
Before running the application, ensure PostgreSQL with pgvector is running:
```sh
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  phidata/pgvector:16
```
### 5️⃣ Set Up Environment Variables
Ensure you have the necessary API keys under the name "GROQ_API_KEY", "POSTGRES_URL", "HASHNODE_API_KEY", "BLOG_ID". Store them in a `.env` file or configure them in your environment.
### 6️⃣ Run the Application
```sh
streamlit run main.py
```
---
## 🛠 Usage Guide
1. Open the Streamlit app in your browser.
2. Enter a region (city) and topic for news.
3. Select a language from the dropdown.
4. Click "Generate & Publish Blog" to fetch news, generate a blog post, and publish it.
5. The generated blog will be displayed with an AI-generated image.
6. A success message will provide a link to the published blog on Hashnode.
---
## 🐳 Running with Docker (Optional)
If you want to containerize and run the app using Docker:
```sh
docker build -t ai-news-blog .
docker run -p 8501:8501 ai-news-blog
```
Then, access the application at `http://localhost:8501/`.
---
## 📜 License
This project is licensed under the terms of the `LICENSE` file included in the repository.
---
## 🤝 Contributions
Feel free to open issues or create pull requests to improve the project!
### Contributors
- Siddharth Karmokar
- Nilesh Sharma
