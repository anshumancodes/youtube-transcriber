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
