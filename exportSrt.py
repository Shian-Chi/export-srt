import os
import subprocess

fileName = "/home/ubuntu/大疆影片/0132/DJI_0132"

video_path = f'{fileName}.MP4'
output_srt = f'{fileName}srt'

def extract_subtitle(video_path, output_srt):
    """
    Extract subtitle from the given video and save it as an .srt file.
    """
    # Use ffmpeg to extract subtitles
    command = [
        'ffmpeg', '-i', video_path, '-map', '0:s:0',
        output_srt, '-y'
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f'Subtitle successfully extracted to: {output_srt}')
    except subprocess.CalledProcessError as e:
        print(f'Error extracting subtitle: {e}')
    except FileNotFoundError:
        print("Error: Ensure ffmpeg is installed and in PATH.")

if __name__ == "__main__":
    # Check if the video file exists
    if os.path.exists(video_path):
        extract_subtitle(video_path, output_srt)
    else:
        print(f"Error: Video file '{video_path}' not found.")

