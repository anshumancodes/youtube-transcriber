from yt_dlp import YoutubeDL
import httpx
from pathlib import Path


def get_video_info(url: str):
    options = {
        "quiet": True,
        "skip_download": True,
    }
    with YoutubeDL(options) as ydl:

        info = ydl.extract_info(url=url, download=False)
        data = {
            "video_id": info["id"],
            "title": info["title"],
            "description": info.get("description"),
            "uploader": info.get("uploader"),
            "duration": info.get("duration"),
            "source_url": url,
            "captions": info.get("subtitles"),
            "auto_captions": info.get("automatic_captions"),
        }
    return data


def get_video_caption_url(video__info, language="en"):

    caption_source = video__info["captions"] or video__info["auto_captions"]
    if caption_source:
        print(
            f"Using {'manual' if video__info['captions'] else 'auto'} captions")
        for caption in caption_source[language]:
            if caption["ext"] == "srt":
                return caption["url"]

    else:
        return None


def download_caption(caption_url, output_dir):
    # hitting the url
    response = httpx.get(caption_url)

    print(response.status_code)

    output_path = Path(output_dir) / "transcript.srt"
    # writing the caption to a file
    with open(output_path, "w", encoding="utf-8") as f:

        f.write(response.text)
        print(
            f"downloading caption is completed sucessfully!, see the file at {output_path}")
        return output_path


# we will download the video if no captions are avialble

def download_video(url, output_dir):
    options = {
        "quiet": True,
        "skip_download": False,
        "outtmpl": str(Path(output_dir) / "video.%(ext)s"),
    }
    with YoutubeDL(options) as ydl:
        ydl.download([url])
        video_info = ydl.extract_info(url=url, download=True)
        video_path = ydl.prepare_filename(video_info)
        
    return video_path
