# agents/tiktok_agent.py

from ai_engine.content_generator import generate_text
from datetime import datetime
import os

def run_tiktok_agent(topic: str, tone: str = "fun and energetic") -> str:
    prompt = f"""
Create a TikTok content pack for the topic: "{topic}" with the following parts:

1. 🎬 **Script**: Write a short spoken script (under 100 words) structured as:
   - Hook (3 seconds)
   - Body
   - Call to Action
   Write each spoken line as a separate subtitle-friendly line.

2. ✍️ **Caption**: Write a catchy caption that explains the video content briefly.

3. 🔖 **Hashtags**: Suggest 5 relevant hashtags that help this reach business owners or tech enthusiasts.

Format everything clearly under headers: [Script], [Caption], [Hashtags]
"""

    result = generate_text(prompt, system_msg="You're a viral TikTok content creator.")

    # Save to outbox
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outbox/{timestamp}_tiktok_full.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"🎬 TikTok content saved to: {filename}")
    return result

# Test run
if __name__ == "__main__":
    run_tiktok_agent("AI automation for online businesses")
