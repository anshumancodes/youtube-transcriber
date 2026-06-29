from pathlib import Path
import json

def parse_srt(output_path):
    with open(output_path, "r", encoding="utf-8") as f:
        content = f.read()
        blocks = content.strip().split("\n\n")
        # segement array
        segments = []
        for block in blocks:
            lines = block.split("\n")
            if len(lines) < 3:
                continue
            # extracting start and end
            start, end = lines[1].split(" --> ")
            # to join every line after the timestamp into one string.
            text = " ".join(lines[2:])
            # created a segnent out of it

            segment = {
                "start": start,
                "end": end,
                "text": text,
            }
            segments.append(segment)

        return segments


def save_text(segments, output_dir):

    output_path = Path(output_dir) / "transcript.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        for segment in segments:
            f.write(segment.get("text") + "\n")
    print(f"sucessfully created transcript.txt at {output_path}")
    return output_path


def save_json(segments, output_dir):
    output_path = Path(output_dir)/"transcripts.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(segments, f, indent=4, ensure_ascii=False)
        print(f"sucessfully created transcript.json at {output_path}")
    return output_path
