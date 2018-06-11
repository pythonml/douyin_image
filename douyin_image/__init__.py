import argparse
from douyin_image.converter import add_effect, text_to_img

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", help="text to add effect", dest="text")
    parser.add_argument("--image", help="path of image to add effect", dest="image")
    parser.add_argument("--out", help="path of output image", dest="out")
    args = parser.parse_args()

    if args.text is None and args.image is None:
        parser.error("please specify --text or --image")

    out = args.out if args.out is not None else "out.jpeg"
    if args.text:
        text_to_img(args.text, out)
    if args.image:
        add_effect(args.image, out)
