import argparse
from douyin_image.converter import add_effect

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", help="path of image to add effect", dest="image")
    parser.add_argument("--out", help="path of output image", dest="out")
    args = parser.parse_args()

    if args.image is None:
        parser.error("please specify or --image")

    out = args.out if args.out is not None else "out.jpeg"
    add_effect(args.image, out)
