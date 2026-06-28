

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
