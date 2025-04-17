# scheduler/scheduler_agent.py

from apscheduler.schedulers.blocking import BlockingScheduler
from agents.post_agent import run_post_agent
from agents.x_agent import run_x_agent
from agents.tiktok_agent import run_tiktok_agent
from agents.marketing_agent import run_marketing_agent

def schedule_all():
    scheduler = BlockingScheduler()

    scheduler.add_job(lambda: run_post_agent("AI solutions for businesses"), 'cron', hour=9)
    scheduler.add_job(lambda: run_x_agent("AI tools for small businesses", language="bilingual"), 'cron', hour=10)
    scheduler.add_job(lambda: run_tiktok_agent("How AI saves time for teams"), 'cron', hour=11)
    scheduler.add_job(lambda: run_marketing_agent("AI automation for agencies"), 'cron', hour=12)

    print("✅ Scheduler started... Ctrl+C to stop.")
    scheduler.start()

if __name__ == "__main__":
    schedule_all()
