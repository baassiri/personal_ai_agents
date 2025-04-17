# agents/marketing_agent.py

from ai_engine.content_generator import generate_text
from datetime import datetime
import os

def run_marketing_agent(topic: str, tone: str = "confident", lang: str = "bilingual") -> str:
    lang_prompt = "in both English and Arabic" if lang == "bilingual" else f"in {lang}"
    
    prompt = f"""
Write a {tone} marketing paragraph about "{topic}" {lang_prompt}.
Make it suitable for a website or professional sales message.
"""
    text = generate_text(prompt, system_msg="You are a professional B2B marketer.")

    # Save to outbox
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outbox/{timestamp}_marketing.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✅ Marketing text saved to: {filename}")
    return text

# Example usage
if __name__ == "__main__":
    run_marketing_agent("custom AI software for logistics companies")
