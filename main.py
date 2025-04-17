from agents.post_agent import run_post_agent
from agents.marketing_agent import run_marketing_agent
from agents.cold_email_agent import run_cold_email_agent
from agents.x_agent import run_x_agent
from agents.caption_agent import generate_tiktok_script
from agents.tiktok_video_agent import run_tiktok_video_agent
from dotenv import load_dotenv

def display_menu():
    print("🤖 Arzisoft Automation Hub\n")
    print("1. Generate Social Post")
    print("2. Generate Marketing Text")
    print("3. Generate Cold Email")
    print("4. Generate TikTok Content")
    print("5. Generate X.com Post")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nSelect an option: ")

        if choice == "1":
            topic = input("Enter a topic for the social post: ")
            run_post_agent(topic)

        elif choice == "2":
            topic = input("Enter a topic for the marketing text: ")
            run_marketing_agent(topic)

        elif choice == "3":
            service = input("Describe the service: ")
            recipient = input("Who's the target (e.g., dentist, startup founder)?: ")
            run_cold_email_agent(service, recipient)

        elif choice == "4":
            topic = input("Enter the TikTok topic: ")
            path = generate_tiktok_script(topic)
            print(f"🎬 TikTok content saved to: {path}")
            run_tiktok_video_agent(path)

        elif choice == "5":
            topic = input("Enter the X.com post topic: ")
            style = input("Style (e.g., informative, witty, promotional): ").strip() or "informative"
            lang = input("Language? (english / arabic / bilingual): ").strip().lower() or "english"
            run_x_agent(topic, style=style, language=lang)

        elif choice == "0":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid option.\n")

if __name__ == "__main__":
    main()
