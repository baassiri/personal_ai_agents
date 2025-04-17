# agents/cold_email_agent.py

from ai_engine.content_generator import generate_text
from datetime import datetime
import os

def run_cold_email_agent(service: str, recipient_type: str = "business owner") -> str:
    prompt = f"""
Write a professional cold email introducing a service: "{service}".
Target audience: {recipient_type}.
Tone: Helpful, clear, and persuasive.
Keep it short and direct. End with a CTA.
"""
    email = generate_text(prompt, system_msg="You are an expert cold email copywriter.")

    # Save to outbox
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outbox/{timestamp}_cold_email.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(email)

    print(f"📧 Cold email saved to: {filename}")
    return email

# Example
if __name__ == "__main__":
    run_cold_email_agent("AI automation for restaurant order management", recipient_type="restaurant manager")
