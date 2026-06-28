import argparse
from downloader import get_video_info
def parse_args():
    parser=argparse.ArgumentParser(
        description="Generate transcripts from youtube videos"
    )
    # url is mandatory , because without it we cant do anytbing really
    parser.add_argument(
        "--url",
        required=True,
        help="Yt video Url"
    )
    #output dir argurement 
    parser.add_argument(
        "--output",
        default="outputs",
        help="output directory , default directory is set to `outputs`"
    )
    return parser.parse_args()

def main():
    args=parse_args()

    print("youtube transriber")
    print ("url: ",args.url)
    print(" output dir :",args.output)
    info=get_video_info(url=args.url)
    print("information about the video: ",info)

if __name__== "__main__":
    main()