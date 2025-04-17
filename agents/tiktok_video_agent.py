import sys
import os
import random
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.video_tools import (
    generate_tiktok_video,
    generate_voiceover_from_script,
    extract_sections_from_script
)

def run_tiktok_video_agent(script_file):
    print("🎬 Loading script...")
    script_lines, caption, hashtags = extract_sections_from_script(script_file)

    # Pick a random raw clip
    raw_clips_folder = "media/raw_clips"
    video_file = random.choice([
        os.path.join(raw_clips_folder, f)
        for f in os.listdir(raw_clips_folder)
        if f.endswith(".mp4")
    ])
    print(f"🎞️ Using clip: {os.path.basename(video_file)}")

    # Timestamp for output naming
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Voice path
    voice_path = f"media/voiceovers/voice_{timestamp}.mp3"
    voice_path = generate_voiceover_from_script(script_lines, output_audio_path=voice_path)

    # Output video
    output_video_path = f"media/generated/final_{timestamp}.mp4"
    generate_tiktok_video(script_lines, video_file, output_video_path, voice_path)
    print(f"✅ Video saved to: {output_video_path}")

    # Save caption + hashtags separately
    caption_file = os.path.join("outbox", f"{timestamp}_caption.txt")
    with open(caption_file, "w", encoding="utf-8") as f:
        f.write(caption + "\n\n" + hashtags)
    print(f"📝 Caption saved to: {caption_file}")

if __name__ == "__main__":
    run_tiktok_video_agent("outbox/20250416_133746_tiktok_full.txt")
