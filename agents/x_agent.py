import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_engine.content_generator import generate_text
from datetime import datetime
from utils.x_poster import post_to_x  # Unofficial posting via Selenium
from dotenv import load_dotenv

def run_x_agent(topic: str, style: str = "informative", language: str = "english") -> str:
    lang_text = f"in {language}" if language != "bilingual" else "in both English and Arabic"
    
    prompt = f"""
Write a {style} tweet about "{topic}" {lang_text}.
Max 280 characters.
Make it attention-grabbing and relevant to automation, AI, or software development.
Add 2–3 relevant hashtags at the end.
"""

    tweet = generate_text(prompt, system_msg="You're a clever tech influencer on X.")

    # ✅ Save tweet to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outbox/{timestamp}_x_post.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(tweet)

    print(f"🐦 X.com post saved to: {filename}")

    # ✅ Auto-post via Selenium
    post_to_x(tweet)

    return tweet

# ✅ Direct run for testing
if __name__ == "__main__":
    run_x_agent("using AI to save time for small businesses", language="bilingual")
