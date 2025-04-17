# agents/caption_agent.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
load_dotenv()
from ai_engine.content_generator import generate_text

def run_caption_agent(topic: str, style: str = "professional", bilingual: bool = True) -> str:
    prompt = f"""
Write a {style} social media caption about "{topic}" in both English and Arabic.
Make it catchy and suitable for Instagram and TikTok.
Start with English, then Arabic.
"""
    caption = generate_text(prompt, system_msg="You are a creative social media expert.")
    return caption

# Test
if __name__ == "__main__":
    result = run_caption_agent("AI automation for businesses")
    print("📝 Generated Caption:\n", result)
from ai_engine.content_generator import ask_gpt
from datetime import datetime

def generate_tiktok_script(topic: str) -> str:
    prompt = f"""Generate a TikTok script for the topic: "{topic}"

Return it in this exact format:

[Script]
- Hook: ...
- Body: ...
- Call to Action: ...

[Caption]
...

[Hashtags]
..."""

    result = ask_gpt(prompt)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outbox/{timestamp}_tiktok_full.txt"
    
    os.makedirs("outbox", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(result.strip())

    return filename
