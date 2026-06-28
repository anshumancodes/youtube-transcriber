from yt_dlp import YoutubeDL


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
    if video__info["captions"]:
        print("Manual captions available")
        return video__info["captions"].keys()

    elif video__info["auto_captions"]:
        print("Auto captions available")
        
        for caption in video__info["auto_captions"][language]:
            if caption["ext"] == "srt":
                return caption["url"]

    else:
        return "No captions"
