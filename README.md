## YouTube Transcript Pipeline

A Python CLI tool that generates transcripts from YouTube videos. The application first attempts to fetch existing captions. If captions are unavailable, it downloads the video, extracts the audio using FFmpeg, and transcribes it locally using faster-whisper

![workflow](workflow.png)

### workflow

The pipeline begins by taking a YouTube URL and fetching the video's metadata to determine whether captions are available. If captions exist, the SRT subtitle file is downloaded and parsed. Otherwise, the video is downloaded, its audio is extracted, and a speech-to-text model is used to generate the transcript. Regardless of the path taken, the transcript is normalized into a structured segments array, where each segment contains the text along with its corresponding timestamps. Finally, the processed transcript is stored in both plain text (transcript.txt) and structured JSON (transcript.json) formats for downstream processing and retrieval.

### Tech stack

- python
- ffmpeg
- faster_whisper
- yt-dlp

## How to Run

### 1. Create a virtual environment

```bash
python3 -m venv venv
```

### 2. Activate the virtual environment

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows (Command Prompt)**

```cmd
venv\Scripts\activate
```

**Windows (PowerShell)**

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python3 main.py --url <youtube_video_url>
```

For example:

```bash
python3 main.py --url "https://youtu.be/jNQXAC9IVRw?si=-fcBEgeyhDUJw47M"
```
