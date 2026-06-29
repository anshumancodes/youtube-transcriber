from faster_whisper import WhisperModel
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8",
)


def transcribe_audio(audio_path):
    whisper_segments, info = model.transcribe(audio_path, vad_filter=True)

    print("Detected language '%s' with probability %f" %
          (info.language, info.language_probability))

    # storing parsed sgement from whisper's sent segments here
    parsed_segments = []

    for segment in whisper_segments:
        parsed_segments.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text.strip()
        })

    return parsed_segments
