# agents/post_agent.py

from agents.caption_agent import run_caption_agent
from datetime import datetime
import os

def run_post_agent(topic: str, style: str = "professional"):
    caption = run_caption_agent(topic, style)

    # Save to /outbox
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outbox/{timestamp}_post.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(caption)

    print(f"✅ Post saved to: {filename}")

# Example
if __name__ == "__main__":
    run_post_agent("AI chatbots for customer support", style="engaging")
