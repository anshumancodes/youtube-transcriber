import argparse
from downloader import get_video_info, get_video_caption_url, download_caption
from formatter import parse_srt, save_text
from pprint import pprint


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

   # downloading the caption from the caption url (in srt format)
    if not caption_url:
        print("no caption available")
    print("caption url :  ", caption_url)
    srt_output_path = download_caption(
        caption_url=caption_url, output_dir=args.output)

    # then i will pass it to srt parser
    # to parse the srt we are saving
    segments = parse_srt(srt_output_path)

    # saving parsed srt segements's text in transcripts.txt
    transcript_txt = save_text(segments=segments, output_dir=arg.output)


if __name__ == "__main__":
    main()
