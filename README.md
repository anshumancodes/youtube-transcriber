## YouTube Transcript Pipeline

A Python CLI tool that generates transcripts from YouTube videos. The application first attempts to fetch existing captions. If captions are unavailable, it downloads the video, extracts the audio using FFmpeg, and transcribes it locally using faster-whisper