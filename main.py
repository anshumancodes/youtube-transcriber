import argparse
from downloader import get_video_info, get_video_caption_url, download_caption, download_video
from formatter import parse_srt, save_text, save_json
from audio import extract_audio
from pprint import pprint
from transcriber import transcribe_audio


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate transcripts from youtube videos"
    )
    # url is mandatory , because without it we cant do anytbing really
    parser.add_argument(
        "--url",
        required=True,
        help="Yt video Url"
    )
    # output dir argurement
    parser.add_argument(
        "--output",
        default="outputs",
        help="output directory , default directory is set to `outputs`"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    print("youtube transriber")
    print("url: ", args.url)
    print(" output dir :", args.output)

    # getting video info from downloader get_video_info fucntion
    video = get_video_info(url=args.url)

   # getting captions url
    caption_url = get_video_caption_url(video__info=video)

    if not caption_url:
        print("no caption available")
        print("proceeding to fallback....")
        # if captions or auto captions not found then will :

        # will get downloaded video path
        downloaded_video_path = download_video(args.url, args.output)

        # extracting  audio
        extracted_audio = extract_audio(downloaded_video_path, args.output)

        # pass the audio to transcriber so it changes into segements

        segments_from_transcriber = transcribe_audio(extracted_audio)

        # saving to text
        transcript_txt = save_text(
            segments=segments_from_transcriber, output_dir=args.output)

        # saving to json
        transcript_json = save_json(
            segments=segments_from_transcriber, output_dir=args.output)

    print("caption url :  ", caption_url)
    # downloading the caption from the caption url (in srt format)
    srt_output_path = download_caption(
        caption_url=caption_url, output_dir=args.output)

    # then i will pass it to srt parser
    # to parse the srt we are saving
    segments = parse_srt(srt_output_path)

    # saving parsed srt segements's text in transcripts.txt
    transcript_txt = save_text(segments=segments, output_dir=args.output)

    # saving parsed srt segements's text in transcripts.json
    transcript_json = save_json(segments=segments, output_dir=args.output)

    args = parse_args()

    print("youtube transcriber")
    print("url:", args.url)
    print("output dir:", args.output)

    # Get video metadata
    video = get_video_info(url=args.url)

    # Get caption URL (still fetched, but ignored for testing)
    caption_url = get_video_caption_url(video__info=video)

    # ----------------------------
    # TEMPORARY: Force fallback
    # ----------------------------
    if True:
        print("Testing fallback pipeline...")

        # Download video
        downloaded_video_path = download_video(args.url, args.output)

        # Extract audio
        extracted_audio = extract_audio(
            downloaded_video_path,
            args.output
        )

        # Transcribe locally
        segments = transcribe_audio(extracted_audio)

    else:
        print("Caption URL:", caption_url)

        # Download captions
        srt_output_path = download_caption(
            caption_url=caption_url,
            output_dir=args.output
        )

        # Parse SRT
        segments = parse_srt(srt_output_path)

    # Common output logic
    transcript_txt = save_text(
        segments=segments,
        output_dir=args.output,
    )

    transcript_json = save_json(
        segments=segments,
        output_dir=args.output,
    )

    print("Done!")


if __name__ == "__main__":
    main()
