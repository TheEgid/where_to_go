import codecs
import requests
from PIL import Image
from io import BytesIO
from django.conf import settings


def clean_string(line):
    line = line.replace("", "")
    return codecs.decode(codecs.encode(
        line, 'latin-1', 'backslashreplace'), 'unicode-escape')


def resize_sides(width, height, max_size=99):
    if width > height:
        resized_width = max_size
        resized_height = int(
            round((max_size / float(width)) * height))
    else:
        resized_height = max_size
        resized_width = int(
            round((max_size / float(height)) * width))
    return resized_width, resized_height


def save_picture(url, new_name):
    filename = settings.MEDIA_ROOT / new_name
    response = requests.get(url, verify=True)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content))
    img.save(filename)
