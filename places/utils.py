import codecs
import requests
from PIL import Image
from io import BytesIO
from django.conf import settings


def clean_string(line):
    line = line.replace("", "")
    return codecs.decode(codecs.encode(
        line, 'latin-1', 'backslashreplace'), 'unicode-escape')


def save_picture(url, new_name):
    filename = settings.MEDIA_ROOT / new_name
    response = requests.get(url, verify=True)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content))
    img.save(filename)
