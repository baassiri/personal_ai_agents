import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.x_agent import run_x_agent
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import random
from dotenv import load_dotenv
scheduler = BlockingScheduler()

topics = [
    "how AI chatbots can help small businesses",
    "using automation to boost productivity",
    "AI tools saving time for startups",
    "automating sales pipelines with AI",
    "chatbot benefits for Lebanese restaurants",
    "automation and AI for gym memberships"
]

styles = ["informative", "witty", "promotional", "clever", "funny"]

def scheduled_post():
    topic = topics[datetime.now().hour % len(topics)]
    style = random.choice(styles)
    print(f"\n📅 Generating X.com post\n📌 Topic: {topic}\n🧠 Style: {style}")
    run_x_agent(topic, style=style, language="bilingual")

scheduler.add_job(scheduled_post, 'interval', hours=3)

if __name__ == "__main__":
    print("📆 X Scheduler started.")
    scheduled_post()  # Initial post on script run
    scheduler.start()
