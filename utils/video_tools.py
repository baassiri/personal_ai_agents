from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
import os
def generate_tiktok_video(script_lines, input_video_path, output_path, voice_path=None):
    from moviepy.editor import AudioFileClip, VideoFileClip, TextClip, CompositeVideoClip
    import os

    # Load the video and clip it to 15 seconds max
    video = VideoFileClip(input_video_path).subclip(0, min(15, VideoFileClip(input_video_path).duration))
    clips = [video]

    # Calculate subtitle timing
    duration_per_line = video.duration / len(script_lines)

    for i, line in enumerate(script_lines):
        txt = TextClip(
            line,
            fontsize=48,
            font="Arial-Bold",
            color="white",
            bg_color="black",
            size=(video.w, None),
            method='caption'
        ).set_position(("center", "bottom")).set_duration(duration_per_line).set_start(i * duration_per_line)

        clips.append(txt)

    final = CompositeVideoClip(clips)

    if voice_path:
        audio = AudioFileClip(voice_path).set_duration(final.duration)
        final = final.set_audio(audio.volumex(1.5))

        temp_video = output_path.replace(".mp4", "_temp.mp4")
        final.write_videofile(temp_video, codec='libx264', audio=False)

        # Then mux in the real audio
        force_mux_audio(temp_video, voice_path, output_path)

        # Clean temp if you want
        os.remove(temp_video)

import subprocess

def force_mux_audio(video_path, audio_path, output_path):
    command = [
        "ffmpeg",
        "-y",  # overwrite
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-map", "0:v:0",
        "-map", "1:a:0",
        output_path
    ]
    subprocess.run(command, shell=True)
    print(f"🔊 Muxed audio into video: {output_path}")


from TTS.api import TTS
from datetime import datetime
import os

def generate_voiceover_from_script(script_lines, output_audio_path=None):
    text = " ".join(script_lines)

    # Initialize TTS (change model if needed)
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

    if not output_audio_path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_audio_path = f"media/voiceovers/voice_{timestamp}.wav"

    os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)

    # Generate and save voice
    tts.tts_to_file(text=text, file_path=output_audio_path)
    print(f"🗣️ Voiceover saved to: {output_audio_path}")
    return output_audio_path





def extract_sections_from_script(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    def extract(tag):
        if f"[{tag}]" not in content:
            return ""
        return content.split(f"[{tag}]")[-1].split("\n[")[0].strip()

    script_lines = [
    line.split(":", 1)[-1].strip().strip('"')
    for line in extract("Script").split("\n")
    if line.strip()
]


    caption = extract("Caption")
    hashtags = extract("Hashtags")

    return script_lines, caption, hashtags
