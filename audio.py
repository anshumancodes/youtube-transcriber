import subprocess
from pathlib import Path


def extract_audio(video_path, output_dir):
    # vn flag is to remove video stream
    output_path = Path(output_dir)/'audio.wav'
    command = [
        'ffmpeg',
        "-y"
        '-i', video_path,
        '-vn',
        "-ac", "1",            # mono audio
        "-ar", "16000",        # 16 KHZ sample rate output
        str(output_path)


    ]
    try:
        subprocess.run(command,
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.PIPE,
                       check=True)
        print("audio extracted sucessfully!")
        return output_path

    except FileNotFoundError:
        raise RuntimeError(
            "FFmpeg is not installed or is not available in your PATH."
        )

    except subprocess.CalledProcessError as error:
        print(f"error occured while converting vid to audio : {error}")
