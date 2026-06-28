import argparse
from downloader import get_video_info , get_video_caption_url

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

   #getting captions url
    caption_url=get_video_caption_url(video__info=video)
    if not caption_url:
        print("no caption available")
    print("caption url :  ",caption_url)

if __name__ == "__main__":
    main()
