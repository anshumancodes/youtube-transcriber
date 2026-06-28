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

    caption_source = video__info["captions"] or video__info["auto_captions"]
    if caption_source:
        print(
            f"Using {'manual' if video__info['captions'] else 'auto'} captions")
        for caption in caption_source[language]:
            if caption["ext"] == "srt":
                return caption["url"]

    else:
        return None
