from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt

def add_effect(filepath, outpath):
    img_orig = Image.open(filepath)
    img_orig.putalpha(255)

    array_orig = np.array(img_orig)
    array_r = np.copy(array_orig)
    array_r[:,:,1:3] = 0
    image_r = Image.fromarray(array_r)

    array_gb = np.copy(array_orig)
    array_gb[:,:,0] = 0
    image_gb = Image.fromarray(array_gb)

    canvas_r = Image.new("RGB", img_orig.size, color=(0,0,0))
    canvas_r.paste(image_r, (5, 5), image_r)
    canvas_gb = Image.new("RGB", img_orig.size, color=(0,0,0))
    canvas_gb.paste(image_gb, (0,0), image_gb)
    result_array = np.array(canvas_r) + np.array(canvas_gb)
    result = Image.fromarray(result_array)
    result = result.crop((5, 5, img_orig.size[0], img_orig.size[1]))
    result.save(outpath)

def text_to_img(txt, outpath):
    fnt = ImageFont.truetype('/Library/Fonts/Tahoma Bold.ttf', 100)
    text1 = Image.new("RGBA", (300, 200), color=(0, 0, 0, 255))
    text2 = Image.new("RGBA", (300, 200), color=(0, 0, 0, 255))
    textdraw1 = ImageDraw.ImageDraw(text1, "RGBA")
    textdraw2 = ImageDraw.ImageDraw(text2, "RGBA")
    textdraw1.text((23, 23), txt, font=fnt, fill=(255, 0, 0, 230))
    textdraw2.text((18, 18), txt, font=fnt, fill=(0, 255, 255, 230))
    array1 = np.array(text1)
    array2 = np.array(text2)
    result_array = array1 + array2
    result = Image.fromarray(result_array)
    result.save(outpath)
